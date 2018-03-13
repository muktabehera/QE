"""Common QE, PathFinder (QED) and PFE helper functions."""
import pytest

import copy  # noqa: F401
from collections import OrderedDict  # noqa: F401
import datetime  # noqa: F401
from functools import wraps
import logging
import os
import pytz  # noqa: F401
import sys
import time  # noqa: F401

from box import Box
from faker import Factory  # noqa: F401
from tenacity import retry, stop_after_delay, stop_after_attempt, wait_fixed, retry_if_result

from grappa import expect  # noqa: F401
from grappa import should  # noqa: F401

import better_exceptions  # noqa: F401
# from flaky import flaky  # noqa: F401


# Python 2 & 3 compatability imports
try:
    from urlparse import urlparse  # noqa: F401
except ImportError:
    from urllib.parse import urlparse  # noqa: F401

from bravado.exception import *  # noqa: F401


def init_logger():
    """Common logger configuration."""
    # Set logging level:
    # DEBUG will show also plumbum logs
    # INFO for local DEBUG
    # ERROR for production environment
    DEBUG_LEVEL = logging.INFO  # 'CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'INFO'

    # Logger configuration
    logging.basicConfig(level=DEBUG_LEVEL)
    logger = logging.getLogger(__name__)
    # Uncomment for remote syslog:
    # handler = logging.handlers.SysLogHandler(address=(helperServer, 514))
    # logger.addHandler(handler)
    return logger


global logger
logger = init_logger()


def init_allure():
    """Allure replacement for non-pytest execution."""
    # Make this code work, even when it is not called from pytest
    # This will not work across multiple tests or for tests requiring prior info
    pytest.allure = C()
    pytest.allure.story = stub
    pytest.allure.feature = stub
    pytest.allure.issue = stub
    pytest.allure.link = stub


def init_context():
    """Context fixture replacement for non-pytest execution."""
    context = C()
    context.config = Box()
    context.status = Box()
    context.data = Box()
    return context


def get_config_file_cmdarg(arg='--env'):
    """Crud get command line variables, for when py.test is not being used.

    Default is looking for `env` argument.
    """
    argValue = None
    try:
        argValue = sys.argv[sys.argv.index(arg) + 1]
    except ValueError:
        argValue = None
    except IndexError:
        logger.error(
            "\n\n*** Error parsing command line.\nCould not identify existing file name after {} option.\n".
            format(arg))
        raise Exception(
            "Could not identify existing file name after {} option.\n".format(
                arg))
    except Exception:
        raise
    if argValue is not None:
        checkFile = os.path.isfile(argValue)
        if not checkFile:
            logger.error(
                "\n\n*** Error parsing command line.\nCould not identify existing file name after {} option.\n".
                format(arg))
            raise Exception(
                "Could not identify existing file name after {} option.\n".
                format(arg))
    return argValue


def load_config_file(filename='data/qed_env.yml', path=None):
    """Loads Yaml configuration file and return its content in a box."""
    if filename is None:
        filename = 'data/qed_env.yml'
    if not path:
        try:
            path = os.path.dirname(__file__)
        except NameError:
            path = ''
    try:
        filePath = os.path.join(path, filename)
        config = Box.from_yaml(filename=filePath)
    except IOError:  # Try searching the data folder as well
        path = os.path.join(path, 'data')
        filePath = os.path.join(path, filename)
        config = Box.from_yaml(filename=filePath)
    except Exception:
        raise
    return config


def load_auth_file(filename='data/pf_auth.yml', path=None):
    """Loads Yaml configuration file and return its content in a box."""
    if filename is None:
        filename = 'data/pf_auth.yml'
    if not path:
        try:
            path = os.path.dirname(__file__)
        except NameError:
            path = ''
    try:
        filePath = os.path.join(path, filename)
        config = Box.from_yaml(filename=filePath)
    except IOError:  # Try searching the data folder as well
        path = os.path.join(path, 'data')
        filePath = os.path.join(path, filename)
        config = Box.from_yaml(filename=filePath)
    except Exception:
        raise
    return config


def baseName(name):
    """Return base name of entity for test name ID."""
    return '-'.join(name.split('-')[:-2])


class C(object):
    """Stub replacement for missing classes."""

    def __init__(self):
        """Stub."""
        return


def stub(*args, **kwargs):
    """Stub replacement for missing decorators."""

    @wraps(stub)
    def decorator(func):
        @wraps(decorator)
        def decorated(*argsw, **kwargsw):
            return func(*argsw, **kwargsw)

        return decorated

    return decorator


def check(cmd, returnResponse=False, quiet=False, token=None):
    """Log and report exceptions in single swagger call test functions.

    Args:
        ``cmd`` (str) - the swagger client command to be executed, without the .result()

    Kwargs:
        ``returnResponse`` (bool) - when True, return tuple of swagger response
                                    and :mod:`requests` object.
                                    Default is False, which returns only swagger response object.
        ``quiet`` (bool)          - Default False, so errors are logged on 'error' level.
                                    When True, errors will be reported on debug level, so to suppress
                                    unnecessary logs for expected error cases.
        ``token`` (string)        - Default: None = generate valid token.
                                    Otherwise, use provided token.

    Returns:
        Returns the cmd result - cmd.result()

    Raises:
        Re-raises any underlying swagger client exception.

    """
    result = None
    try:
        if not token:
            token = __builtins__['context'].pf.get_token()
        cmd.also_return_response = returnResponse
        if 'headers' in token:
            cmd.future.request.headers = token['headers']
        result = cmd.result()
        logger.debug(result)
    except Exception as e:
        if 'response' in dir(e):  # Try logging response details
            if quiet:
                logger.debug("\nGot an error in response: {}".format(
                    repr(e.response)))
                if 'text' in dir(e.response):
                    logger.debug("\nError response details: {}".format(
                        e.response.text))
            else:
                logger.error("\nGot an error in response: {}".format(
                    repr(e.response)))
                if 'text' in dir(e.response):
                    logger.error("\nError response details: {}".format(
                        e.response.text))
        raise
    else:
        return result


@retry(
    stop=(stop_after_delay(60) | stop_after_attempt(30)),
    wait=wait_fixed(2),
    reraise=True,
    retry=retry_if_result(lambda result: result is None))
def retry_check(cmd,
                resultAttribute,
                expectedResult,
                returnResponse=False,
                quiet=False):
    """Log and report exceptions in single swagger call test functions.

    Will retry the swagger call up to a minute (every 2 sec.), unless got the expected result.

    Args:
        ``cmd`` (str)  - the swagger client command to be executed, without the .result()

        ``resultAttribute`` (str) - attribute in the result to compare to the expected result

        ``expectedResult`` (object) - expected return object from cmd.result()

    Kwargs:
        ``returnResponse`` (bool) - when True, return tuple of swagger response
                                    and :mod:`requests` object.
                                    Default is False, which returns only swagger response object.
        ``quiet`` (bool)          - Default False, so errors are logged on 'error' level.
                                    When True, errors will be reported on debug level, so to suppress
                                    unnecessary logs for expected error cases.

    Returns:
        Returns the cmd result object - cmd.result()

    Raises:
        Re-raises any underlying swagger client exception.

    """
    result = None
    try:
        token = __builtins__['context'].pf.get_token()
        cmd.also_return_response = returnResponse
        if 'headers' in token:
            cmd.future.request.headers = token['headers']
        result = cmd.result()
        if returnResponse:
            response = result[0]
        else:
            response = result
        attr = response.__dict__[list(
            response.__dict__.keys())[0]][resultAttribute]
        logger.info(result)
    except Exception as e:
        if 'response' in dir(e):  # Try logging response details
            if quiet:
                logger.debug("\nGot an error in response: {}".format(
                    e.response))
                logger.debug("\nError response details: {}".format(
                    e.response.text))
            else:
                logger.error("\nGot an error in response: {}".format(
                    e.response))
                logger.error("\nError response details: {}".format(
                    e.response.text))
        raise
    if attr == expectedResult:
        return result
    else:
        return None


def get_error_message(exception):
    """Extrat retuned messages from PathFinder swagger error response.

    Args:
        exception - the exception object caught.

    Returns:
        Embedded exception message.

    """
    message = ''
    if len(exception.response.json()['requestErrors']) > 0:
        message += exception.response.json()['requestErrors'][0]['message']
        message += ' \n'
    if len(exception.response.json()['parameterErrors']) > 0:
        message += exception.response.json()['parameterErrors'][0]['message']
    return str(message)


def delay_rerun(*args):
    """Delay re-run of a failed test."""
    time.sleep(2)
    return True
