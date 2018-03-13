"""PFE Component Tests - setup prerequisites.

* Create proximity zone.
* Create network location.
* Create client.
* Create PathFinderEdge Profile.
* Create PathFinderEdge Device.

"""
import pytest

from qe_common import *

logger = init_logger()





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





# We put the tests in a class, so we done have to repeat the different markings
#
# Forcing order=3 for initial common environment setup only.
# Other tests should not be use this method for ordering the tests.
# I.e., other tests must be able to run independently and in varying order.
# Please see the docs for more details on test ordering.
#
@pytest.mark.run(order=3)
@pytest.mark.init
@pytest.mark.components
@pytest.allure.story('Setup prerequisites')
@pytest.allure.feature('Test PathFinder SUT Components')
class Test_PFE_Components(object):
    """PFE Components test cases common setup."""

    @pytest.mark.config
    @pytest.allure.link('https://jira.qumu.com/browse/TC-43795')
    @pytest.mark.proximityZone
    @pytest.mark.post
    def test_TC_43795_POST_ProximityZone_AbleToCreateProximityZoneWithMandatoryParameters(self, context):
        """Create a common proximity zone for component tests.

        TC_43795_POST_ProximityZone_AbleToCreateProximityZoneWithMandatoryParameters

        id = "ProximityPost"
        name = "ProximityPost"
        """
        # These could come from a data file
        id = "ProximityPost"
        name = "ProximityPost"
        # Define a test step
        with pytest.allure.step("Create proximityZone `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing proximityZones
            if 'proximityZones' not in context.status:
                context.status.proximityZones = Box()
            # Per Swagger schema, proximityDetails is an object
            proximityDetails = context.sc.ProximityDetails(
                cidr='0.0.0.0/0',
                metric=1,
                notes='Test proximity details')
            # We store ProximityZoneDetails is contect.status, in case it is needed later
            context.status.proximityZones[id] = context.sc.ProximityZoneDetails(
                visibleInAllConfigurations=True,
                configAdminCanEdit=False,
                configurations=[context.status['globals']['configId']],
                id=id,
                name=name,
                proximityDetails=[proximityDetails])
            # Post the proximityZone.
            # The `check` call validates return code and some of the swagger schema
            # (most schema checks are disabled)
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Proximity_Zones.createEntity(
                        body=context.status.proximityZones[id]     # The object we created above
                    )
                )

    @pytest.mark.config
    def test_create_networkLocation(self, context):
        """Create a common network location for component tests.

        id = "NetworkLocationWithRulesGroups"
        name = "Network Rules and Groups"
        """
        # These could come from a data file
        id = "NetworkLocationWithRulesGroups"
        name = "Network Rules and Groups"
        # Define a test step
        with pytest.allure.step("Create networkLocation `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing network locations
            if 'networkLocations' not in context.status:
                context.status.networkLocations = Box()
            # This is an example of increamental object creation
            # Per Swagger schema, context.sc.ExpressionDetails is an object
            # We'll create a list of context.sc.ExpressionDetails, per the schema
            rules = []
            rules.append(context.sc.ExpressionDetails(
                contextField='remoteAddress',
                contextFieldKey=None,
                contextFieldType='String',
                expressionType='Single',
                matchValue='10.0.0.0/32',
                operator='IPMATCH'))
            rules.append(context.sc.ExpressionDetails(
                contextField='remoteHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='autoQEd',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='serverHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='101.101.101.101',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='serverPort',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue=80.0,
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='operatingSystem',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='BLACKBERRY',
                operator='OSMATCH'))
            rules.append(context.sc.ExpressionDetails(
                contextField='browser',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='CHROME',
                operator='BROWSERMATCH'))
            rules.append(context.sc.ExpressionDetails(
                contextField='headerMap',
                contextFieldKey='header',
                contextFieldType='String',
                expressionType='Map',
                matchValue='header',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='queryParamMap',
                contextFieldKey='query',
                contextFieldType='String',
                expressionType='Map',
                matchValue='query',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='tags',
                contextFieldKey='tags',
                contextFieldType='String',
                expressionType='Map',
                matchValue='tags',
                operator='EQ'))
            # ... and create a list of nested rules, for matching groups
            nestedRules = []
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='remoteAddress',
                contextFieldKey=None,
                contextFieldType='String',
                expressionType='Single',
                matchValue='10.19.20.0/32',
                operator='IPMATCH'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='remoteHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='autovcc.qumu.com',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='serverHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='10.10.10.25',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='serverPort',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue=8080.0,
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='operatingSystem',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='ANDROID',
                operator='OSMATCH'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='browser',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='IE6',
                operator='BROWSERMATCH'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='headerMap',
                contextFieldKey='45',
                contextFieldType='String',
                expressionType='Map',
                matchValue='45',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='queryParamMap',
                contextFieldKey='qumu',
                contextFieldType='String',
                expressionType='Map',
                matchValue='qmu',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='tags',
                contextFieldKey='tag',
                contextFieldType='String',
                expressionType='Map',
                matchValue='tag',
                operator='EQ'))

            # Rules are grouped in an context.sc.ExpressionTreeDetails object
            nestedExpressionTreeDetails = context.sc.ExpressionTreeDetails(
                operator="ALL",
                rules=nestedRules,
                groups=[]

            )
            # Another context.sc.ExpressionTreeDetails object, for top-level rules
            expressionTreeDetails = context.sc.ExpressionTreeDetails(
                operator="ALL",
                rules=rules,
                groups=[nestedExpressionTreeDetails]
            )
            # Create NetworkLocationDetails object, and keep it is context.status
            context.status.networkLocations[id] = context.sc.NetworkLocationDetails(
                id=id,
                name=name,
                description="Test network location description.",
                bitrateCapVOD=0,
                bitrateCapLive=0,
                matchingRule=expressionTreeDetails
            )
            # Post the networkLocation.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Network_Locations.createEntity(
                        body=context.status.networkLocations[id]     # The object we created above
                    )
                )

    @pytest.mark.config
    def test_create_client(self, context):
        """Create a common client for component tests.

        id = "clientsWithAllDetails"
        name = "Client with All Details"
        """
        # These could come from a data file
        id = "clientsWithAllDetails"
        name = "Client with All Details"
        # Define a test step
        with pytest.allure.step("Create client `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing clients
            if 'clients' not in context.status:
                context.status.clients = Box()

            # This is an example of monolitic object creation
            context.status.clients[id] = context.sc.ClientDetails(
                id=id,
                name=name,
                matchingRule=context.sc.ExpressionTreeDetails(
                    groups=[
                        context.sc.ExpressionTreeDetails(
                            groups=[],
                            operator='ALL',
                            rules=[
                                context.sc.ExpressionDetails(
                                    contextField='remoteAddress',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='172.0.0.0/8',
                                    operator='IPMATCH'),
                                context.sc.ExpressionDetails(
                                    contextField='remoteHost',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='qed.com',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='serverHost',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='172.30.3.174',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='serverPort',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue=8080.0,
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='operatingSystem',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='WINDOWS_8',
                                    operator='OSMATCH'),
                                context.sc.ExpressionDetails(
                                    contextField='browser',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='IE',
                                    operator='BROWSERMATCH'),
                                context.sc.ExpressionDetails(
                                    contextField='headerMap',
                                    contextFieldKey='headergroup',
                                    contextFieldType='String',
                                    expressionType='Map',
                                    matchValue='headergroup',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='queryParamMap',
                                    contextFieldKey='query1',
                                    contextFieldType='String',
                                    expressionType='Map',
                                    matchValue='query1',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='tags',
                                    contextFieldKey='1234',
                                    contextFieldType='String',
                                    expressionType='Map',
                                    matchValue='1234',
                                    operator='EQ')
                            ]
                        )
                    ],
                    operator='ALL',
                    rules=[
                        context.sc.ExpressionDetails(
                            contextField='remoteAddress',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='172.0.0.0/8',
                            operator='IPMATCH'),
                        context.sc.ExpressionDetails(
                            contextField='remoteHost',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='qed.com',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='serverHost',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='172.30.3.174',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='operatingSystem',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='BLACKBERRY',
                            operator='OSMATCH'),
                        context.sc.ExpressionDetails(
                            contextField='browser',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='IE10',
                            operator='BROWSERMATCH'),
                        context.sc.ExpressionDetails(
                            contextField='headerMap',
                            contextFieldKey='header',
                            contextFieldType='String',
                            expressionType='Map',
                            matchValue='header',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='queryParamMap',
                            contextFieldKey='query',
                            contextFieldType='String',
                            expressionType='Map',
                            matchValue='query',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='tags',
                            contextFieldKey='tag',
                            contextFieldType='String',
                            expressionType='Map',
                            matchValue='tag',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='serverPort',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue=8080.0,
                            operator='EQ')
                    ]
                ),
                sourceSelectionRule=[
                    context.sc.ExpressionTreeDetails(
                        groups=[
                            context.sc.ExpressionTreeDetails(
                                groups=[],
                                operator='ALL',
                                rules=[
                                    context.sc.ExpressionDetails(
                                        contextField='bitrateKbps',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue=523.0,
                                        operator='EQ'),
                                    context.sc.ExpressionDetails(
                                        contextField='heightPx',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue=456.0,
                                        operator='EQ'),
                                    context.sc.ExpressionDetails(
                                        contextField='mimetype',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue='video/mp4',
                                        operator='MIMEMATCH'),
                                    context.sc.ExpressionDetails(
                                        contextField='tags',
                                        contextFieldKey='456',
                                        contextFieldType='String',
                                        expressionType='Map',
                                        matchValue='456',
                                        operator='EQ'),
                                    context.sc.ExpressionDetails(
                                        contextField='widthPx',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue=200.0,
                                        operator='EQ')
                                ]
                            )
                        ],
                        operator='ALL',
                        rules=[
                            context.sc.ExpressionDetails(
                                contextField='bitrateKbps',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue=256.0,
                                operator='EQ'),
                            context.sc.ExpressionDetails(
                                contextField='heightPx',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue=563.0,
                                operator='EQ'),
                            context.sc.ExpressionDetails(
                                contextField='mimetype',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue='application/x-mpegURL',
                                operator='MIMEMATCH'),
                            context.sc.ExpressionDetails(
                                contextField='tags',
                                contextFieldKey='124',
                                contextFieldType='String',
                                expressionType='Map',
                                matchValue='124',
                                operator='EQ'),
                            context.sc.ExpressionDetails(
                                contextField='widthPx',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue=250.0,
                                operator='EQ')
                        ]
                    )
                ]
            )
            # Post the networkLocation.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Clients.createEntity(
                        body=context.status.clients[id]     # The object we created above
                    )
                )

    @pytest.mark.config
    def test_create_PFE_Profile(self, context):
        """Create a common PFE Profile for component tests.

        id = "No_proxy_profile_POST"
        name = "No proxy profile"
        """
        # These could come from a data file
        id = "No_proxy_profile_POST"
        name = "No proxy profile"
        # Define a test step
        with pytest.allure.step("Create client `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing PFE Profiles
            if 'PFEprofiles' not in context.status:
                context.status.PFEprofiles = Box()
            # Create VideoEdgeDevicePropertyDetails
            context.status.PFEprofiles[id] = context.sc.VideoEdgeDevicePropertyDetails(
                configAdminCanEdit=False,
                configurations=[],
                enablePrepositioning=True,
                enableTokenAuthentication=True,
                httpService=context.sc.VideoEdgeHTTPServiceDetails(
                    httpPort=80,
                    httpsPort=443,
                    protocol='http',
                    serviceActive=True,
                    vodPublishingPoints=None
                ),
                id='No_proxy_profile_POST',
                manifestRequestFrequency=600,
                maximumDownloadTime=54000,
                name='No_proxy_profile_POST',
                nonRestrictedPeriodDownloadBandwidth=500,
                proxyMode='NO_PROXY',
                restrictedBandwidthEnd=2,
                restrictedBandwidthStart=21,
                restrictedPeriodDownloadBandwidth=100,
                rtspService=context.sc.VideoEdgeRTSPServiceDetails(
                    multicastAddress='',
                    multicastEnabled=False,
                    multicastTtl=5,
                    rtspStreamingPort=554,
                    serviceActive=True,
                    unicastFailoverEnabled=True
                ),
                tokenExpirationTime=180,
                visibleInAllConfigurations=True
            )
            # Post the profile.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Pathfinder_Edge_Device_Profiles.createEntity(
                        body=context.status.PFEprofiles[id]
                    )
                )

    @pytest.mark.config
    def test_create_PFE_Device(self, context):
        """Create a common PFE Device for component tests.

        id = "POST_veDevices_AllConfigAdminMulticastTrue"
        name = "POST_veDevices_AllConfigAdminMulticastTrue"
        """
        # These could come from a data file
        id = "POST_veDevices_AllConfigAdminMulticastTrue"
        name = "POST_veDevices_AllConfigAdminMulticastTrue"
        deviceHost = "POST_veDevices"
        # Define a test step
        with pytest.allure.step("Create client `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing PFE Devices
            if deviceHost not in context.status:
                context.status['PFEs'][deviceHost] = Box()
            # Create VideoEdgeDevicePropertyDetails
            context.status['PFEs'][deviceHost].videoEdgeDevice = context.sc.VideoEdgeDeviceDetails(
                id=id,
                name=name,
                multicastHost=deviceHost,
                streamingHost=deviceHost,
                deviceHost=deviceHost,
                tag='testtag',
                description='Test PFE descriptions - {}'.format(name),
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=False,
                deviceGUID=None,
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=[
                    'DISTRIBUTION',
                    'ORIGIN',
                    'EDGE'],
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[
                    context.sc.ProximityRangeEdgeDeviceMappingDetails(
                        edgeDevice=context.sc.IdNamePair(
                            id='POST_veDevices_AllConfigAdminMulticastTrue',
                            name='POST_veDevices_AllConfigAdminMulticastTrue'
                        ),
                        endAddress='0.0.0.0',
                        startAddress='0.0.0.0'
                    )
                ],
                proximityZones=[
                    context.sc.IdNamePair(
                        id='ProximityPost',
                        name='ProximityPost'
                    )
                ],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                visibleInAllConfigurations=True
            )
            # Post the device.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Pathfinder_Edge_Device.createEntity(
                        body=context.status['PFEs'][deviceHost].videoEdgeDevice
                    )
                )

    @pytest.mark.config
    def test_create_PFE_Stand_Alone_DeliverySystem(self, context):
        """Create a common PFE stand-alone delivery for component tests.

        id = "POST_veDevices_AllConfigAdminMulticastTrue"
        name = "POST_veDevices_AllConfigAdminMulticastTrue"
        """
        # These could come from a data file
        id = "POST_veDevices_AllConfigAdminMulticastTrue"
        PFE_Name = "POST_veDevices_AllConfigAdminMulticastTrue"
        deviceHost = "POST_veDevices"
        # Define a test step
        with pytest.allure.step("Create client delivery system `{}`.".format(id)):
            if deviceHost not in context.status:
                context.status['PFEs'][deviceHost] = Box()
            context.status['PFEs'][deviceHost].deliverySystem = context.sc.DeliverySystemDetails(
                id=PFE_Name,
                name="VideoEdge Delivery System {}".format(PFE_Name),
                deliverySystemType="videoedge",
                deliverySystemRoles=['ORIGIN', 'DISTRIBUTION', 'EDGE'],
                configurations=[],
                settings={"deviceId": PFE_Name},
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
            )
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Delivery_Systems.createDeliveryOption(
                    body=context.status['PFEs'][deviceHost].deliverySystem))

    @pytest.mark.config
    def test_create_client_2(self, context):
        """Create a common client for component tests.

        id = "clientsWithAllDetails"
        name = "Client with All Details"
        """
        # These could come from a data file
        id = "clientsWithAllDetailsTwo"
        name = "Client with All DetailsTwo"
        # Define a test step
        with pytest.allure.step("Create client `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing clients
            if 'clients' not in context.status:
                context.status.clients = Box()

            # This is an example of monolitic object creation
            context.status.clients[id] = context.sc.ClientDetails(
                id=id,
                name=name,
                matchingRule=context.sc.ExpressionTreeDetails(
                    groups=[
                        context.sc.ExpressionTreeDetails(
                            groups=[],
                            operator='ALL',
                            rules=[
                                context.sc.ExpressionDetails(
                                    contextField='remoteAddress',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='172.0.0.0/8',
                                    operator='IPMATCH'),
                                context.sc.ExpressionDetails(
                                    contextField='remoteHost',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='qed.com',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='serverHost',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='172.30.3.174',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='serverPort',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue=8080.0,
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='operatingSystem',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='WINDOWS_8',
                                    operator='OSMATCH'),
                                context.sc.ExpressionDetails(
                                    contextField='browser',
                                    contextFieldKey=None,
                                    contextFieldType='String',
                                    expressionType='Single',
                                    matchValue='IE',
                                    operator='BROWSERMATCH'),
                                context.sc.ExpressionDetails(
                                    contextField='headerMap',
                                    contextFieldKey='headergroup',
                                    contextFieldType='String',
                                    expressionType='Map',
                                    matchValue='headergroup',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='queryParamMap',
                                    contextFieldKey='query1',
                                    contextFieldType='String',
                                    expressionType='Map',
                                    matchValue='query1',
                                    operator='EQ'),
                                context.sc.ExpressionDetails(
                                    contextField='tags',
                                    contextFieldKey='1234',
                                    contextFieldType='String',
                                    expressionType='Map',
                                    matchValue='1234',
                                    operator='EQ')
                            ]
                        )
                    ],
                    operator='ALL',
                    rules=[
                        context.sc.ExpressionDetails(
                            contextField='remoteAddress',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='172.0.0.0/8',
                            operator='IPMATCH'),
                        context.sc.ExpressionDetails(
                            contextField='remoteHost',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='qed.com',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='serverHost',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='172.30.3.174',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='operatingSystem',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='BLACKBERRY',
                            operator='OSMATCH'),
                        context.sc.ExpressionDetails(
                            contextField='browser',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue='IE10',
                            operator='BROWSERMATCH'),
                        context.sc.ExpressionDetails(
                            contextField='headerMap',
                            contextFieldKey='header',
                            contextFieldType='String',
                            expressionType='Map',
                            matchValue='header',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='queryParamMap',
                            contextFieldKey='query',
                            contextFieldType='String',
                            expressionType='Map',
                            matchValue='query',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='tags',
                            contextFieldKey='tag',
                            contextFieldType='String',
                            expressionType='Map',
                            matchValue='tag',
                            operator='EQ'),
                        context.sc.ExpressionDetails(
                            contextField='serverPort',
                            contextFieldKey=None,
                            contextFieldType='String',
                            expressionType='Single',
                            matchValue=8080.0,
                            operator='EQ')
                    ]
                ),
                sourceSelectionRule=[
                    context.sc.ExpressionTreeDetails(
                        groups=[
                            context.sc.ExpressionTreeDetails(
                                groups=[],
                                operator='ALL',
                                rules=[
                                    context.sc.ExpressionDetails(
                                        contextField='bitrateKbps',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue=523.0,
                                        operator='EQ'),
                                    context.sc.ExpressionDetails(
                                        contextField='heightPx',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue=456.0,
                                        operator='EQ'),
                                    context.sc.ExpressionDetails(
                                        contextField='mimetype',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue='video/mp4',
                                        operator='MIMEMATCH'),
                                    context.sc.ExpressionDetails(
                                        contextField='tags',
                                        contextFieldKey='456',
                                        contextFieldType='String',
                                        expressionType='Map',
                                        matchValue='456',
                                        operator='EQ'),
                                    context.sc.ExpressionDetails(
                                        contextField='widthPx',
                                        contextFieldKey=None,
                                        contextFieldType='String',
                                        expressionType='Single',
                                        matchValue=200.0,
                                        operator='EQ')
                                ]
                            )
                        ],
                        operator='ALL',
                        rules=[
                            context.sc.ExpressionDetails(
                                contextField='bitrateKbps',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue=256.0,
                                operator='EQ'),
                            context.sc.ExpressionDetails(
                                contextField='heightPx',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue=563.0,
                                operator='EQ'),
                            context.sc.ExpressionDetails(
                                contextField='mimetype',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue='application/x-mpegURL',
                                operator='MIMEMATCH'),
                            context.sc.ExpressionDetails(
                                contextField='tags',
                                contextFieldKey='124',
                                contextFieldType='String',
                                expressionType='Map',
                                matchValue='124',
                                operator='EQ'),
                            context.sc.ExpressionDetails(
                                contextField='widthPx',
                                contextFieldKey=None,
                                contextFieldType='String',
                                expressionType='Single',
                                matchValue=250.0,
                                operator='EQ')
                        ]
                    )
                ]
            )
            # Post the networkLocation.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Clients.createEntity(
                        body=context.status.clients[id]  # The object we created above
                    )
                )

    @pytest.mark.config
    def test_create_networkLocation_2(self, context):
        """Create a common network location for component tests.

        id = "NetworkLocationWithRulesGroups"
        name = "Network Rules and Groups"
        """
        # These could come from a data file
        id = "NetworkLocationWithRulesGroupsTwo"
        name = "Network Rules and GroupsTwo"
        # Define a test step
        with pytest.allure.step("Create networkLocation `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing network locations
            if 'networkLocations' not in context.status:
                context.status.networkLocations = Box()
            # This is an example of increamental object creation
            # Per Swagger schema, context.sc.ExpressionDetails is an object
            # We'll create a list of context.sc.ExpressionDetails, per the schema
            rules = []
            rules.append(context.sc.ExpressionDetails(
                contextField='remoteAddress',
                contextFieldKey=None,
                contextFieldType='String',
                expressionType='Single',
                matchValue='10.0.0.0/32',
                operator='IPMATCH'))
            rules.append(context.sc.ExpressionDetails(
                contextField='remoteHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='autoQEd',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='serverHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='101.101.101.101',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='serverPort',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue=80.0,
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='operatingSystem',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='BLACKBERRY',
                operator='OSMATCH'))
            rules.append(context.sc.ExpressionDetails(
                contextField='browser',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='CHROME',
                operator='BROWSERMATCH'))
            rules.append(context.sc.ExpressionDetails(
                contextField='headerMap',
                contextFieldKey='header',
                contextFieldType='String',
                expressionType='Map',
                matchValue='header',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='queryParamMap',
                contextFieldKey='query',
                contextFieldType='String',
                expressionType='Map',
                matchValue='query',
                operator='EQ'))
            rules.append(context.sc.ExpressionDetails(
                contextField='tags',
                contextFieldKey='tags',
                contextFieldType='String',
                expressionType='Map',
                matchValue='tags',
                operator='EQ'))
            # ... and create a list of nested rules, for matching groups
            nestedRules = []
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='remoteAddress',
                contextFieldKey=None,
                contextFieldType='String',
                expressionType='Single',
                matchValue='10.19.20.0/32',
                operator='IPMATCH'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='remoteHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='autovcc.qumu.com',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='serverHost',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='10.10.10.25',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='serverPort',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue=8080.0,
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='operatingSystem',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='ANDROID',
                operator='OSMATCH'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='browser',
                contextFieldKey='',
                contextFieldType='String',
                expressionType='Single',
                matchValue='IE6',
                operator='BROWSERMATCH'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='headerMap',
                contextFieldKey='45',
                contextFieldType='String',
                expressionType='Map',
                matchValue='45',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='queryParamMap',
                contextFieldKey='qumu',
                contextFieldType='String',
                expressionType='Map',
                matchValue='qmu',
                operator='EQ'))
            nestedRules.append(context.sc.ExpressionDetails(
                contextField='tags',
                contextFieldKey='tag',
                contextFieldType='String',
                expressionType='Map',
                matchValue='tag',
                operator='EQ'))

            # Rules are grouped in an context.sc.ExpressionTreeDetails object
            nestedExpressionTreeDetails = context.sc.ExpressionTreeDetails(
                operator="ALL",
                rules=nestedRules,
                groups=[]

            )
            # Another context.sc.ExpressionTreeDetails object, for top-level rules
            expressionTreeDetails = context.sc.ExpressionTreeDetails(
                operator="ALL",
                rules=rules,
                groups=[nestedExpressionTreeDetails]
            )
            # Create NetworkLocationDetails object, and keep it is context.status
            context.status.networkLocations[id] = context.sc.NetworkLocationDetails(
                id=id,
                name=name,
                description="Test network location description.",
                bitrateCapVOD=0,
                bitrateCapLive=0,
                matchingRule=expressionTreeDetails
            )
            # Post the networkLocation.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Network_Locations.createEntity(
                        body=context.status.networkLocations[id]  # The object we created above
                    )
                )

    @pytest.mark.config
    def test_create_PFE_Device_2(self, context):
        """Create a common PFE Device for component tests.

        id = "POST_veDevices_AllConfigAdminMulticastTrue"
        name = "POST_veDevices_AllConfigAdminMulticastTrue"
        """
        # These could come from a data file
        id = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        name = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        deviceHost = "POST_veDevices"
        # Define a test step
        with pytest.allure.step("Create client `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing PFE Devices
            if deviceHost not in context.status:
                context.status['PFEs'][deviceHost] = Box()
            # Create VideoEdgeDevicePropertyDetails
            context.status['PFEs'][deviceHost].videoEdgeDevice = context.sc.VideoEdgeDeviceDetails(
                id=id,
                name=name,
                multicastHost=deviceHost,
                streamingHost=deviceHost,
                deviceHost=deviceHost,
                tag='testtag',
                description='Test PFE descriptions - {}'.format(name),
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=False,
                deviceGUID=None,
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=[
                    'DISTRIBUTION',
                    'ORIGIN',
                    'EDGE'],
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[
                    context.sc.ProximityRangeEdgeDeviceMappingDetails(
                        edgeDevice=context.sc.IdNamePair(
                            id='POST_veDevices_AllConfigAdminMulticastTrue',
                            name='POST_veDevices_AllConfigAdminMulticastTrue'
                        ),
                        endAddress='0.0.0.0',
                        startAddress='0.0.0.0'
                    )
                ],
                proximityZones=[
                    context.sc.IdNamePair(
                        id='ProximityPost',
                        name='ProximityPost'
                    )
                ],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                visibleInAllConfigurations=True
            )
            # Post the device.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Pathfinder_Edge_Device.createEntity(
                        body=context.status['PFEs'][deviceHost].videoEdgeDevice
                    )
                )

    @pytest.mark.config
    def test_create_PFE_Stand_Alone_DeliverySystem_2(self, context):
        """Create a common PFE stand-alone delivery for component tests.

        id = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        name = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        """
        # These could come from a data file
        id = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        PFE_Name = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        deviceHost = "POST_veDevices"
        # Define a test step
        with pytest.allure.step("Create client delivery system `{}`.".format(id)):
            if deviceHost not in context.status:
                context.status['PFEs'][deviceHost] = Box()
            context.status['PFEs'][deviceHost].deliverySystem = context.sc.DeliverySystemDetails(
                id=PFE_Name,
                name="VideoEdge Delivery System {}".format(PFE_Name),
                deliverySystemType="videoedge",
                deliverySystemRoles=['ORIGIN', 'DISTRIBUTION', 'EDGE'],
                configurations=[],
                settings={"deviceId": PFE_Name},
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
            )
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Delivery_Systems.createDeliveryOption(
                    body=context.status['PFEs'][deviceHost].deliverySystem))

    @pytest.mark.config
    def test_create_PFE_Device_3(self, context):
        """Create a common PFE Device for component tests.

        id = "POST_veDevices_AllConfigAdminMulticastTrue"
        name = "POST_veDevices_AllConfigAdminMulticastTrue"
        """
        # These could come from a data file
        id = "POST_veDevices_AllConfigAdminMulticastTrueThree"
        name = "POST_veDevices_AllConfigAdminMulticastTrueThree"
        deviceHost = "POST_veDevices"
        # Define a test step
        with pytest.allure.step("Create client `{}` ({}).".format(name, id)):
            # Create a place in context.status for storing PFE Devices
            if deviceHost not in context.status:
                context.status['PFEs'][deviceHost] = Box()
            # Create VideoEdgeDevicePropertyDetails
            context.status['PFEs'][deviceHost].videoEdgeDevice = context.sc.VideoEdgeDeviceDetails(
                id=id,
                name=name,
                multicastHost=deviceHost,
                streamingHost=deviceHost,
                deviceHost=deviceHost,
                tag='testtag',
                description='Test PFE descriptions - {}'.format(name),
                alertCount=0,
                configAdminCanEdit=True,
                configurations=[],
                currentEdgeVersion=None,
                deactivateReflectorService=False,
                deviceGUID=None,
                deviceProfileId='No_proxy_profile_POST',
                edgeDeviceRoles=[
                    # 'DISTRIBUTION',
                    # 'ORIGIN',
                    'EDGE'],
                online=False,
                osVersion=None,
                overrideProfileProperties=False,
                proximityDetails=[
                    context.sc.ProximityRangeEdgeDeviceMappingDetails(
                        edgeDevice=context.sc.IdNamePair(
                            id='POST_veDevices_AllConfigAdminMulticastTrue',
                            name='POST_veDevices_AllConfigAdminMulticastTrue'
                        ),
                        endAddress='0.0.0.0',
                        startAddress='0.0.0.0'
                    )
                ],
                proximityZones=[
                    context.sc.IdNamePair(
                        id='ProximityPost',
                        name='ProximityPost'
                    )
                ],
                rtspMulticastAddressOverride='10.10.10.10',
                rtspMulticastEnabledOverride=True,
                rtspMulticastTTLOverride=5,
                visibleInAllConfigurations=True
            )
            # Post the device.
            if context.status.PF_Clean_Upgrade:
                check(
                    context.cl.Pathfinder_Edge_Device.createEntity(
                        body=context.status['PFEs'][deviceHost].videoEdgeDevice
                    )
                )

    @pytest.mark.config
    def test_create_PFE_Stand_Alone_DeliverySystem_3(self, context):
        """Create a common PFE stand-alone delivery for component tests.

        id = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        name = "POST_veDevices_AllConfigAdminMulticastTrueTWO"
        """
        # These could come from a data file
        id = "POST_veDevices_AllConfigAdminMulticastTrueThree"
        PFE_Name = "POST_veDevices_AllConfigAdminMulticastTrueThree"
        deviceHost = "POST_veDevices"
        # Define a test step
        with pytest.allure.step("Create client delivery system `{}`.".format(id)):
            if deviceHost not in context.status:
                context.status['PFEs'][deviceHost] = Box()
            context.status['PFEs'][deviceHost].deliverySystem = context.sc.DeliverySystemDetails(
                id=PFE_Name,
                name="VideoEdge Delivery System {}".format(PFE_Name),
                deliverySystemType="videoedge",
                deliverySystemRoles=['EDGE'],
                configurations=[],
                settings={"deviceId": PFE_Name},
                visibleInAllConfigurations=True,
                configAdminCanEdit=True,
            )
            if context.status.PF_Clean_Upgrade:
                check(context.cl.Delivery_Systems.createDeliveryOption(
                    body=context.status['PFEs'][deviceHost].deliverySystem))