"""Global stand-alone PFE broadcast test data generation."""
import pytest

from box import Box

from qe_common import *

global env
env = load_config_file('data/qed_env.yml')

global logger
logger = init_logger()

faker = Factory.create(env.Locale)


@pytest.fixture(scope="session")
def broadcastTests(request, context):
    """Generate test data context for all broadcast tests.

    Test data is in under context.data.broadcasts.

    For stand-alone PFE tests, pairs of Audience Id and Broadcast Id are created
    for each PFE, and stored and a PFE_IP key (the PFE IP address), under broadcasts.

    For example:

    >>> context.data.broadcasts["10.0.0.1"]['AudienceId']
    >>> context.data.broadcasts["10.0.0.2"]['BroadcastId']

    """
    if 'broadcasts' not in context.data:
        context.data.broadcasts = Box()
    for ip, name in env.PFE_IPs:
        if ip not in context.data.broadcasts:
            context.data.broadcasts[ip] = Box()
            if 'AudienceIds' not in context.data.broadcasts[ip]:
                context.data.broadcasts[ip]['AudienceIds'] = list()
            audienceId = "audiencevne-{}".format(name)
            if audienceId not in context.data.broadcasts[ip]['AudienceIds']:
                context.data.broadcasts[ip]['AudienceIds'].append(audienceId)
            #
            # Per the schema, the audience should be defined from IdNamePair object,
            # however this is not working (bug), hence just a string
            #
            # context.data.broadcasts[ip]['AudienceIds'].append(
            #     context.sc.IdNamePair(
            #         id="audiencevne-{}".format(PFE_Name),
            #         name="VideoEdge Audience {}".format(PFE_Name)
            #     )
            # )
            #
            if 'BroadcastIds' not in context.data.broadcasts[ip]:
                context.data.broadcasts[ip]['BroadcastIds'] = list()
            n = faker.pyint()
            broadcastIdExt = time.strftime('-%Y%m%d%H%M%S') + '-' + str(n)
            context.data.broadcasts[ip]['BroadcastIds'].append(
                'broadcast-' + name + broadcastIdExt)
    return context.data.broadcasts


@pytest.fixture(scope="session")
def distributionTests(request, context):
    """Generate test data context for all distribution tests.

    Test data is in under context.data.distribution.

    For stand-alone PFE tests, pairs of Audience Id and Distribution Id are created
    for each PFE, and stored and a PFE_IP key (the PFE IP address), under broadcasts.

    For example:

    >>> context.data.distribution["10.0.0.1"]['AudienceId']
    >>> context.data.distribution["10.0.0.2"]['DistributionId']

    """
    if 'distribution' not in context.data:
        context.data.distributions = Box()
    for ip, name in env.PFE_IPs:
        if ip not in context.data.distributions:
            context.data.distributions[ip] = Box()
            if 'AudienceIds' not in context.data.distributions[ip]:
                context.data.distributions[ip]['AudienceIds'] = list()
            audienceId = "audiencevne-{}".format(name)
            if audienceId not in context.data.distributions[ip]['AudienceIds']:
                context.data.distributions[ip]['AudienceIds'].append(audienceId)
            #
            # Per the schema, the audience should be defined from IdNamePair object,
            # however this is not working (bug), hence just a string
            #
            # context.data.distributions[ip]['AudienceIds'].append(
            #     context.sc.IdNamePair(
            #         id="audiencevne-{}".format(PFE_Name),
            #         name="VideoEdge Audience {}".format(PFE_Name)
            #     )
            # )
            #
            if 'DistributionId' not in context.data.broadcasts[ip]:
                context.data.distributions[ip]['DistributionIds'] = list()
            n = faker.pyint()
            distributionIdExt = time.strftime('-%Y%m%d%H%M%S') + '-' + str(n)
            context.data.distributions[ip]['DistributionIds'].append(
                'distribution-' + name + distributionIdExt)
    return context.data.distributions
