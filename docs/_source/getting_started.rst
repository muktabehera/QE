Getting Started
===============

Interactive Shell
-----------------

Assuming framework was installed successfuly, and `ptpython <https://github.com/jonathanslenders/ptpython>`_ has been installed as well.

* Open command prompt shell
* Navigate to QE project root folder
* Run ptpython
* Run the following:

>>> from functional.init_PF_test import *

View available PathFinder objects:

>>> dir()

or, preferably:

>>> dir(context.sc)

View available PathFidner access paths:

>>> dir(context.cl)

Now you can try different commands:

>>> print(context.cl.System.getSystemInfo(_request_options=context.pf.get_token()).result())

The 'check' function add token handling & error reporting, while 'retry_check' adds retry capabilities as well.

So the command above will look like:

>>> print(check(context.cl.System.getSystemInfo()))

More examples:

>>> buildInfo = check(context.cl.System.getBuildInfo())
>>> print(buildInfo.buildVersion)

We can also create and modify the configuration. For example, assuming some audience(s) have already been configured:


Get current list of audiences:

>>> audiences = check(context.cl.Audiences.listEntities())
>>> for audience in audiences:
        print audience.id

Make a copy of the first audience, and change its Id:

>>> from copy import copy
>>> newAudience = copy(audiences[0])
>>> newAudience.id = 'myNewAudienceTestId'

Post the new audience, and print the response. Please note that errors are raised as exceptions.

>>> response = check(context.cl.Audiences.createEntity(body=newAudience))
>>> print response


Running Existing Tests
----------------------

Tests are executed using py.test.
Please see ``run.sh`` for command-line example, and check `pytest help <https://docs.pytest.org/en/latest/usage.html>`_ for
additional details. Specifically, please review the *-m* and *-s* options. Example::

    py.test --alluredir allure --disable-pytest-warnings --disable-warnings -s --env data/qed_env.yml functional/ -m "init or sanity"


Writing New tests
-----------------

.. important:: All new tests, and any other code changes, **must** be done using:

    * Use **your own fork** of the code.
    * Create a **new / different branch** for the code changes.
    * **Test the code** on your environment and fork, including regression tests with earlier code and tests.
    * Submit change to the main repository via a **pull-request**.

Please see existing tests for reference and structure.


All tests must be able to run independently and in any order.
Exceptions to this are only the following:

* order=0  -  global environment initialization
* order=1  -  PathFinder specific initialization
* order=2  -  PathFinderEdge specific initialization
* order=3  -  common test data generation, if used in multiple tests and scripts

Please mark tests as draft, until they consistently pass unit-test::

    @pytest.mark.draft
