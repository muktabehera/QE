"""Stand-Alone PFE Distribution Tests.

* Create a stand-alone distribution.
* ...

"""
import pytest

from qe_common import *

logger = init_logger()

# Common framwork variables initialization
global env
env = load_config_file(get_config_file_cmdarg())

# Make this code load, even when allure fixture is not present
# This will not work across multiple tests nor for tests requiring prior context
if 'allure' not in dir(pytest):
    from qe_common import init_allure, init_context
    import qe_modules.PathFinder as PF
    import qe_modules.PathFinderEdge as PFE
    init_allure()
    global context
    context = init_context()
    context.env = env
    context.status.PF_Clean_Upgrade = False
    context.status.PFE_Clean_Upgrade = False
    context.PF = PF
    context.PFE = PFE
    context.pf = PF.PathFinder(env.QED_Name)
    # context.interactive = True

# Used for generating random test data
faker = Factory.create(env.Locale)


@pytest.mark.distribution
@pytest.allure.feature('Distribution tests')
@pytest.allure.story('Stand-Alone PFE Sanity Distribution Test')
class Test_StandAlonePFE_Distribution(object):
    """PFE stand-alone sanity distribution test cases."""

    @pytest.mark.distribution
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_create_distribution(self, context, distributionTests,
                                 PFE_IP, PFE_Name,
                                 AudienceId=None, DistributionId=None, SourceURL=None):
        """Create Stand-Alone distribution.

        This test is generating DistributionId and AudienceId, if not available in context.data
        and are not assigned in the function call.
        This is done to make this function re-usable for other tests,
        and should not be the normal use case.
        """

        logger.info("\nCreating distribution for " + PFE_IP)

        # Create AudienceId, if we don't have one already
        if AudienceId is None:
            if 'distributions' not in context.data:
                context.data.distributions = Box()
            if PFE_IP not in context.data.distributions:
                context.data.distributions[PFE_IP] = Box()
            if 'AudienceIds' not in context.data.distributions[PFE_IP]:
                context.data.distributions[PFE_IP]['AudienceIds'] = list()
            if len(context.data.distributions[PFE_IP]['AudienceIds']) == 0:
                AudienceId = "audiencevne-{}".format(PFE_Name)
                context.data.distributions[PFE_IP]['AudienceIds'].append(AudienceId)
            else:
                AudienceId = context.data.distributions[PFE_IP]['AudienceIds'][-1]  # Latest on the list
        else:
            context.data.distributions[PFE_IP]['AudienceIds'].append(AudienceId)

        # Create BroadcastId, if we don't have one already
        if DistributionId is None:
            if 'DistributionIds' not in context.data.distributions[PFE_IP]:
                context.data.distributions[PFE_IP]['DistributionIds'] = list()
            if len(context.data.distributions[PFE_IP]['DistributionIds']) == 0:
                n = faker.pyint()
                distributionIdExt = time.strftime('-%Y%m%d%H%M%S') + '-' + str(n)
                DistributionId = 'distribution-' + PFE_Name + distributionIdExt
                context.data.distributions[PFE_IP]['DistributionIds'].append(DistributionId)
            else:
                DistributionId = context.data.distributions[PFE_IP]['DistributionIds'][-1]  # Latest on the list
        else:
            context.data.distributions[PFE_IP]['DistributionIds'].append(DistributionId)

        if not SourceURL:
            SourceURL = env.testFile

        AudienceIdNamePair = context.sc.IdNamePair(
            id=AudienceId,
            name="VideoEdge Audience {}".format(PFE_Name)
        )
        contentMetadata = context.sc.ContentMetadataDetails(
            mimeType="text/plain")
        distributionFile = context.sc.DistributionFileDetails(
            id=DistributionId + '_file_1',
            sourceUrl=SourceURL.format(context.status.origin.id).replace('file:', 'qedorigin:'),
            streamMetadata=contentMetadata)
        tz = pytz.timezone(env.Timezone)
        context.status['PFEs'][PFE_IP]['distributions'][DistributionId] = context.sc.DistributionDetails(
            id=DistributionId,
            name='Test Distribution ' + time.strftime('- %Y%m%d%H%M%S'),
            # activationDate=time.strftime('%Y-%m-%dT%H:%M:%S',
            #                              time.localtime(time.mktime(time.localtime()) - 60)),
            activationDate=datetime.datetime.now(tz) + datetime.timedelta(seconds=-60),
            # activationDate=datetime.datetime.now(),
            distributionPolicy="REQUIRED",
            files=[distributionFile],
            targetAudiences=[AudienceIdNamePair])
        check(context.cl.Distributions.createEntity(
            body=context.status['PFEs'][PFE_IP]['distributions'][DistributionId]))

    @pytest.mark.distribution
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_delete_distribution(self, context, distributionTests,
                                 PFE_IP, PFE_Name,
                                 AudienceId=None, DistributionId=None):
        """Delete stand-alone distribution."""
        logger.info("\nDeleting distribution for " + PFE_IP)
        if not DistributionId:
            DistributionId = context.data.distributions[PFE_IP]['DistributionIds'][-1]
        check(context.cl.Distributions.deleteEntity(
            id=DistributionId))
        context.status['PFEs'][PFE_IP]['distributions'].pop(DistributionId)
