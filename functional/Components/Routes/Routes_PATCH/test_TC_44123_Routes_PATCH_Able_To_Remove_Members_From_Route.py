# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44123 - Routes PATCH:

  Verify that user is able to Update(remove members) route having root-5 hops->10 hops each from root device using request PATCH "/routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X PATCH -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'creationDate': '2016-03-09T12:07:24Z',
   'hops': [{'hops': [{'hops': [],
                       'member': {'id': 'validName4',
                                  'name': 'a123!@#$%&*()_-+=,.?;:{}[]`~'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'auto1', 'name': 'auto1'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'auto2', 'name': 'auto2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'auto3', 'name': 'auto3'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoEdge1', 'name': 'autoEdge1'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoO1dist1', 'name': 'autoO1dist1'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoO2dist2', 'name': 'autoO2dist2'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'Testcase1', 'name': 'Testcase1'},
             'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'auto1', 'name': 'auto1'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'auto3', 'name': 'auto3'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoO2dist2', 'name': 'autoO2dist2'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'Device1', 'name': 'Device1'},
                       'memberRoles': ['EDGE', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'GP1', 'name': 'GP1'},
                       'memberRoles': ['EDGE', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'GP3', 'name': 'GP3'},
                       'memberRoles': ['EDGE', 'DISTRIBUTION'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase10', 'name': 'Testcase10'},
             'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'auto1', 'name': 'auto1'},
                       'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'Device1', 'name': 'Device1'},
                       'memberRoles': ['EDGE', 'DISTRIBUTION'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'deleteGroup', 'name': 'Group Delete'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'P2OST1234', 'name': 'Group Id valid 2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': '123456', 'name': 'Group Id valid 3'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'POST_123:-.',
                                  'name': 'Group Id valid 4'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase11', 'name': 'Testcase11'},
             'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'P2OST1234', 'name': 'Group Id valid 2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'POST_123:-.',
                                  'name': 'Group Id valid 4'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigTrue',
                                  'name': 'Group with Admin Configuration'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigFalse',
                                  'name': 'Group with Admin Configuration '
                                          'Disabled'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigNull',
                                  'name': 'Group with Admin Configuration Null'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'config_AllConfig',
                                  'name': 'Group with All Config and '
                                          'configuration'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase12', 'name': 'Testcase12'},
             'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'P2OST1234', 'name': 'Group Id valid 2'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigTrue',
                                  'name': 'Group with Admin Configuration'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigNull',
                                  'name': 'Group with Admin Configuration Null'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfigFalse',
                                  'name': 'Group with All Config False'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfig',
                                  'name': 'Group with All Configuration'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfigDisabled',
                                  'name': 'Group with All Configuration '
                                          'Disabled'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfigNull',
                                  'name': 'Group with All Configuration Null'},
                       'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase13', 'name': 'Testcase13'},
             'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
             'memberType': 'EDGE_DEVICE'}],
   'id': '55devices',
   'modificationDate': '2016-03-09T12:07:59Z',
   'name': 'devices55',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('PATCH')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44123')
    @pytest.mark.Routes
    @pytest.mark.PATCH
    def test_TC_44123_PATCH_Routes_Able_To_Remove_Members_From_Route(self, context):
        """TC-44123 - Routes-PATCH
           Verify that user is able to Update(remove members) route having root-5 hops->10 hops each from root device using request PATCH "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to Update(remove members) route having root-5 hops->10 hops each from root device using request PATCH "/routes"."""):

            ### Positive test example

            # Test case configuration
            hopDetails = context.sc.HopDetails(
                constraintViolations=None,
                hops=[{
                    'member': {
                        'id': 'Testcase1',
                        'name': 'Testcase1'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'validName4',
                            'name': 'a123!@#$%&*()_-+=,.?;:{}[]`~'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto2',
                            'name': 'auto2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge1',
                            'name': 'autoEdge1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO1dist1',
                            'name': 'autoO1dist1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO2dist2',
                            'name': 'autoO2dist2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase10',
                        'name': 'Testcase10'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO2dist2',
                            'name': 'autoO2dist2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'Device1',
                            'name': 'Device1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP1',
                            'name': 'GP1'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP3',
                            'name': 'GP3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase11',
                        'name': 'Testcase11'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'Device1',
                            'name': 'Device1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'deleteGroup',
                            'name': 'Group Delete'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': '123456',
                            'name': 'Group Id valid 3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase12',
                        'name': 'Testcase12'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigFalse',
                            'name': 'Group with Admin Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'config_AllConfig',
                            'name': 'Group with All Config and configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase13',
                        'name': 'Testcase13'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigFalse',
                            'name': 'Group with All Config False'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfig',
                            'name': 'Group with All Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigDisabled',
                            'name': 'Group with All Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigNull',
                            'name': 'Group with All Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }],
                member=None,
                memberRoles=None,
                memberType=None)


            # createHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.createHop(
                    body=hopDetails
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to Update(remove members) route having root-5 hops->10 hops each from root device using request PATCH "/routes"."""):

            ### Negative test example

            # Test case configuration
            hopDetails = context.sc.HopDetails(
                constraintViolations=None,
                hops=[{
                    'member': {
                        'id': 'Testcase1',
                        'name': 'Testcase1'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'validName4',
                            'name': 'a123!@#$%&*()_-+=,.?;:{}[]`~'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto2',
                            'name': 'auto2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge1',
                            'name': 'autoEdge1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO1dist1',
                            'name': 'autoO1dist1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO2dist2',
                            'name': 'autoO2dist2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase10',
                        'name': 'Testcase10'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO2dist2',
                            'name': 'autoO2dist2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'Device1',
                            'name': 'Device1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP1',
                            'name': 'GP1'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP3',
                            'name': 'GP3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase11',
                        'name': 'Testcase11'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'Device1',
                            'name': 'Device1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'deleteGroup',
                            'name': 'Group Delete'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': '123456',
                            'name': 'Group Id valid 3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase12',
                        'name': 'Testcase12'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigFalse',
                            'name': 'Group with Admin Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'config_AllConfig',
                            'name': 'Group with All Config and configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase13',
                        'name': 'Testcase13'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                    'hops': [{
                        'member': {
                            'id': 'autoEdge2',
                            'name': 'autoEdge2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigFalse',
                            'name': 'Group with All Config False'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfig',
                            'name': 'Group with All Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigDisabled',
                            'name': 'Group with All Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigNull',
                            'name': 'Group with All Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['EDGE', 'ORIGIN', 'DISTRIBUTION'],
                        'hops': []
                    }]
                }],
                member=None,
                memberRoles=None,
                memberType=None)


            # prepare the request, so we can modify it
            request = context.cl.Routes.createHop(
                    body=hopDetails
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # createHop the Routes, and check we got the error we expect
            try:
                client, response = check(
                    request,
                    quiet=True, returnResponse=True
                )
            except (HTTPBadRequest, HTTPForbidden) as e:        # 400, 403 error
                get_error_message(e) | expect.any(
                    should.start_with('may not be empty'),
                    should.start_with('Invalid page parameter specified'),
                    should.contain('Invalid Authorization Token')
                )
            else:
                raise Exception(
                    "Expected error message, got {} status code instead.".format(
                        response.status_code))
