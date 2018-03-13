"""Stand-Alone PFE Broadcast Tests.

* Create a stand-alone broadcast.
* Check that broadcast is ready to activate.
* Activate the broadcast.
* Get broadcast URI and check for correctness.
* Delete the broadcast.

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


@pytest.mark.broadcast
@pytest.allure.feature('Broadcast tests')
@pytest.allure.story('Stand-Alone PFE Sanity Broadcast Test')
class Test_StandAlonePFE_Broadcast(object):
    """PFE stand-alone sanity broadcast test cases."""

    @pytest.mark.broadcast
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_create_stand_alone_broadcast(self, context, broadcastTests,
                                          PFE_IP, PFE_Name,
                                          AudienceId=None, BroadcastId=None,
                                          Stream=None):
        """Create Stand-Alone broadcast.

        This test is generating BroadcastId and AudienceId, if not available in context.data
        and are not assigned in the function call.
        This is done to make this function re-usable for other tests,
        and should not be the normal use case.
        """
        logger.info("\nCreating broadcast for " + PFE_IP)

        # Create AudienceId, if we don't have one already
        if AudienceId is None:
            if 'broadcasts' not in context.data:
                context.data.broadcasts = Box()
            if PFE_IP not in context.data.broadcasts:
                context.data.broadcasts[PFE_IP] = Box()
            if 'AudienceIds' not in context.data.broadcasts[PFE_IP]:
                context.data.broadcasts[PFE_IP]['AudienceIds'] = list()
            if len(context.data.broadcasts[PFE_IP]['AudienceIds']) == 0:
                AudienceId = "audiencevne-{}".format(PFE_Name)
                context.data.broadcasts[PFE_IP]['AudienceIds'].append(AudienceId)
            else:
                AudienceId = context.data.broadcasts[PFE_IP]['AudienceIds'][-1]  # Latest on the list
        else:
            context.data.broadcasts[PFE_IP]['AudienceIds'].append(AudienceId)

        # Create BroadcastId, if we don't have one already
        if BroadcastId is None:
            if 'BroadcastIds' not in context.data.broadcasts[PFE_IP]:
                context.data.broadcasts[PFE_IP]['BroadcastIds'] = list()
            if len(context.data.broadcasts[PFE_IP]['BroadcastIds']) == 0:
                n = faker.pyint()
                broadcastIdExt = time.strftime('-%Y%m%d%H%M%S') + '-' + str(n)
                BroadcastId = 'broadcast-' + PFE_Name + broadcastIdExt
                context.data.broadcasts[PFE_IP]['BroadcastIds'].append(BroadcastId)
            else:
                BroadcastId = context.data.broadcasts[PFE_IP]['BroadcastIds'][-1]  # Latest on the list
        else:
            context.data.broadcasts[PFE_IP]['BroadcastIds'].append(BroadcastId)

        if not Stream:
            Stream = env.testStream

        # Create Required Broadcast Objects
        AudienceIdNamePair = context.sc.IdNamePair(
            id=AudienceId,
            name="VideoEdge Audience {}".format(PFE_Name)
        )
        contentMetadata = context.sc.ContentMetadataDetails(
            mimeType="application/vnd.apple.mpegurl")
        broadcastConnectionPoint = context.sc.BroadcastConnectionPointDetails(
            mode="PULL",
            maxConnections=10000,
            url=Stream)
        subContentMetadata = context.sc.ContentMetadataDetails(
            mimeType="application/vnd.apple.mpegurl",
            bitrateKbps=2097152,
            width=1280,
            height=720,
            tags={})
        broadcastSubstream = context.sc.BroadcastSubstreamDetails(
            relativeUrl=Stream.split('/')[-1],
            # ['VARIANTMANIFEST', 'STREAMMANIFEST', 'CAPTIONS', 'AUDIO', 'VIDEO'],
            usage='STREAMMANIFEST',
            streamMetadata=subContentMetadata)
        broadcastStream = context.sc.BroadcastStreamDetails(
            id=BroadcastId,
            streamMetadata=contentMetadata,
            connectionPoints=[broadcastConnectionPoint],
            substreams=[broadcastSubstream])
        # Optional object, not used in this test:
        # broadcastStreamGroup = BroadcastStreamGroupDetails(
        #     id='testBroadcastStreamGroup' + broadcastIdExt,
        #     streams=[broadcastStream])
        # broadcastSourceGroup = BroadcastSourceGroupDetails(
        #     id='testBroadcastSourceGroup' + broadcastIdExt,
        #     # streamGroups=[broadcastStreamGroup])
        #     streams=[broadcastStream],)

        # Keep `BroadcastCreate` object in test cotext status
        context.status['PFEs'][PFE_IP]['broadcasts'][BroadcastId] = context.sc.BroadcastCreate(
            id=BroadcastId,
            name='Test Broadcast with {}'.format(PFE_Name),
            streams=[broadcastStream],
            targetAudiences=[AudienceIdNamePair])

        # Create the broadcast
        check(context.cl.Broadcasts.createEntity(
            body=context.status['PFEs'][PFE_IP]['broadcasts'][BroadcastId]))

    @pytest.mark.broadcast
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_check_broadcast_ready_to_activate(self, context, broadcastTests,
                                               PFE_IP, PFE_Name,
                                               AudienceId=None, BroadcastId=None):
        """Check that broadcast is ready to activate."""
        if not BroadcastId:   # get last broadcast created
            BroadcastId = context.data.broadcasts[PFE_IP]['BroadcastIds'][-1]
            # BroadcastId = context.status['PFEs'][PFE_IP]['broadcasts'][
            #     list(context.status['PFEs'][PFE_IP]['broadcasts'])[-1]].id
        logger.info("\nCheck that broadcast is ready to activate " + BroadcastId)
        broadcastStatus = retry_check(
            context.cl.Broadcasts.getEntity(
                id=BroadcastId),
            'status',
            'READY_TO_START'
        ).status
        logger.info(broadcastStatus)

    @pytest.mark.broadcast
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_activate_broadcasts(self, context, broadcastTests,
                                 PFE_IP, PFE_Name, AudienceId=None,
                                 BroadcastId=None):
        """Activate test broadcasts."""
        if not BroadcastId:   # get last briadcast created
            BroadcastId = context.data.broadcasts[PFE_IP]['BroadcastIds'][-1]
            # BroadcastId = context.status['PFEs'][PFE_IP]['broadcasts'][
            #     list(context.status['PFEs'][PFE_IP]['broadcasts'])[-1]].id
        logger.info("\nActivating broadcast " + BroadcastId)
        broadcastUpdate = context.sc.BroadcastStatusUpdate(status='ACTIVE')
        check(context.cl.Broadcasts.updateEntity(
            id=BroadcastId,
            body=broadcastUpdate))

    @pytest.mark.broadcast
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_get_broadcast_URI(self, context, broadcastTests,
                               PFE_IP, PFE_Name,
                               AudienceId=None, BroadcastId=None,
                               Stream=None):
        """Get broadcast URI for stand-alone PFE.

        This also validates the returned URL content for sanity.
        """
        # for broadcastID in testBroadcasts:
        #     if PFE_Name in broadcastID:
        if not Stream:
            Stream = env.testStream
        if not BroadcastId:   # get last briadcast created
            BroadcastId = context.data.broadcasts[PFE_IP]['BroadcastIds'][-1]
            # BroadcastId = context.status['PFEs'][PFE_IP]['broadcasts'][
            #     list(context.status['PFEs'][PFE_IP]['broadcasts'])[-1]].id
        if not AudienceId:    # get last audience created
            AudienceId = context.data.broadcasts[PFE_IP]['AudienceIds'][-1]
            # AudienceId = context.status['PFEs'][PFE_IP]['audiences'][
            #     list(context.status['PFEs'][PFE_IP]['audiences'])[-1]].id
        logger.info("\nGetting {} URI for audience {} in broadcast {} (via {}) ".format(
            Stream, AudienceId, BroadcastId, PFE_IP))
        # localAudienceId = "audiencevne-{}".format(PFE_Name)
        deliveryUrls = check(context.cl.Delivery_Urls.deliveryUrlsGet(
            audience=AudienceId,
            sourceUrl='qedbroadcast://{}'.format(BroadcastId)))
        for deliveryUrl in deliveryUrls:
            logger.info("- Validating {}".format(deliveryUrl))
            # TODO(video validation): Add video playback validation.
            parsedDeliveryUrl = urlparse(deliveryUrl.url)
            parsedTestStreamUrl = urlparse(Stream)
            with pytest.allure.step('Check delivery URL network location contains either PFE IP or DNS.'):
                str(parsedDeliveryUrl.netloc) | expect.any(
                    should.contain(PFE_Name),
                    should.contain(PFE_IP))
            with pytest.allure.step('Check delivery URL path is the same as the content path.'):
                str(parsedDeliveryUrl.path) | should.be.equal.to(
                    parsedTestStreamUrl.path)
            with pytest.allure.step('Check delivery URL origin query parametr contains the "origin" and the content network location.'):
                str(parsedDeliveryUrl.query) | expect.all(
                    should.contain('origin'),
                    should.contain(parsedTestStreamUrl.netloc))

    @pytest.mark.broadcast
    @pytest.mark.parametrize("PFE_IP, PFE_Name", env.PFE_IPs, ids=baseName)
    def test_delete_broadcast(self, context, broadcastTests,
                              PFE_IP, PFE_Name,
                              AudienceId=None, BroadcastId=None):
        """Delete stand-alone broadcast."""
        logger.info("\nDeleting broadcast for " + PFE_IP)
        if not BroadcastId:
            BroadcastId = context.data.broadcasts[PFE_IP]['BroadcastIds'][-1]
            # broadcastIdExt = time.strftime('-%Y%m%d%H%M%S')
            # BroadcastId = 'broadcast-' + PFE_Name + broadcastIdExt
        check(context.cl.Broadcasts.deleteEntity(
            id=BroadcastId))
        context.status['PFEs'][PFE_IP]['broadcasts'].pop(BroadcastId)
