# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44214 - Routes POST:

  Verify that user is able to add single hop in the route having router1->router(10)->5 each in schema using request POST "/routes/{id}/hops/{memberId}".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1/hops/Test1_auto1_1?memberType=EDGE_DEVICE"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes/BSRoute1/hops/Test1_auto1_1?memberType=EDGE_DEVICE"

JSON data sent to PathFinder in this test:

  {'configAdminCanEdit': True,
   'configurations': [],
   'creationDate': '2016-03-09T12:07:24Z',
   'hops': [{'hops': [{'hops': [],
                       'member': {'id': 'validName4',
                                  'name': 'a123!@#$%&*()_-+=,.?;:{}[]`~'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'auto1', 'name': 'auto1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'auto2', 'name': 'auto2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'auto3', 'name': 'auto3'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoO2dist2', 'name': 'autoO2dist2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'}],
             'member': {'id': 'Testcase1', 'name': 'Testcase1'},
             'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'auto1', 'name': 'auto1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'auto3', 'name': 'auto3'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoO2dist2', 'name': 'autoO2dist2'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'Device1', 'name': 'Device1'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'GP1', 'name': 'GP1'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'GP3', 'name': 'GP3'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase10', 'name': 'Testcase10'},
             'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'auto1', 'name': 'auto1'},
                       'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'Device1', 'name': 'Device1'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'deleteGroup', 'name': 'Group Delete'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'P2OST1234', 'name': 'Group Id valid 2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': '123456', 'name': 'Group Id valid 3'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [{'hops': [],
                                 'member': {'id': 'Testcase1',
                                            'name': 'Testcase1'},
                                 'memberRoles': ['DISTRIBUTION',
                                                 'EDGE',
                                                 'ORIGIN'],
                                 'memberType': 'EDGE_DEVICE'},
                                {'hops': [],
                                 'member': {'id': 'Testcase11',
                                            'name': 'Testcase11'},
                                 'memberRoles': ['DISTRIBUTION',
                                                 'EDGE',
                                                 'ORIGIN'],
                                 'memberType': 'EDGE_DEVICE'},
                                {'hops': [],
                                 'member': {'id': 'Testcase13',
                                            'name': 'Testcase13'},
                                 'memberRoles': ['DISTRIBUTION',
                                                 'EDGE',
                                                 'ORIGIN'],
                                 'memberType': 'EDGE_DEVICE'},
                                {'hops': [],
                                 'member': {'id': 'Testcase14',
                                            'name': 'Testcase14'},
                                 'memberRoles': ['DISTRIBUTION',
                                                 'EDGE',
                                                 'ORIGIN'],
                                 'memberType': 'EDGE_DEVICE'},
                                {'hops': [],
                                 'member': {'id': 'Testcase15',
                                            'name': 'Testcase15'},
                                 'memberRoles': ['DISTRIBUTION',
                                                 'EDGE',
                                                 'ORIGIN'],
                                 'memberType': 'EDGE_DEVICE'}],
                       'member': {'id': 'POST_123:-.',
                                  'name': 'Group Id valid 4'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase11', 'name': 'Testcase11'},
             'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'GP2', 'name': 'GP2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'P2OST1234', 'name': 'Group Id valid 2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'POST_123:-.',
                                  'name': 'Group Id valid 4'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigTrue',
                                  'name': 'Group with Admin Configuration'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigFalse',
                                  'name': 'Group with Admin Configuration '
                                          'Disabled'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigNull',
                                  'name': 'Group with Admin Configuration Null'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'config_AllConfig',
                                  'name': 'Group with All Config and '
                                          'configuration'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase12', 'name': 'Testcase12'},
             'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'},
            {'hops': [{'hops': [],
                       'member': {'id': 'autoEdge2', 'name': 'autoEdge2'},
                       'memberRoles': ['EDGE'],
                       'memberType': 'EDGE_DEVICE'},
                      {'hops': [],
                       'member': {'id': 'P2OST1234', 'name': 'Group Id valid 2'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigTrue',
                                  'name': 'Group with Admin Configuration'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'adminConfigNull',
                                  'name': 'Group with Admin Configuration Null'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfigFalse',
                                  'name': 'Group with All Config False'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfig',
                                  'name': 'Group with All Configuration'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfigDisabled',
                                  'name': 'Group with All Configuration '
                                          'Disabled'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'},
                      {'hops': [],
                       'member': {'id': 'AllConfigNull',
                                  'name': 'Group with All Configuration Null'},
                       'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                       'memberType': 'GROUP'}],
             'member': {'id': 'Testcase13', 'name': 'Testcase13'},
             'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
             'memberType': 'EDGE_DEVICE'}],
   'id': '55devices1',
   'modificationDate': '2016-03-09T12:28:42Z',
   'name': 'devices551',
   'visibleInAllConfigurations': True}

"""

import pytest

from qe_common import *

logger = init_logger()


@pytest.mark.draft      # remove this after script passed unit tests successfuly
@pytest.mark.components
@pytest.allure.story('Routes')
@pytest.allure.feature('POST')
class Test_PFE_Components(object):
    """PFE Routes test cases."""

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44214')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44214_POST_Routes_Add_10Router5Hopseach(self, context):
        """TC-44214 - Routes-POST
           Verify that user is able to add single hop in the route having router1->router(10)->5 each in schema using request POST "/routes/{id}/hops/{memberId}"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to add single hop in the route having router1->router(10)->5 each in schema using request POST "/routes/{id}/hops/{memberId}"."""):

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
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                    'hops': [{
                        'member': {
                            'id': 'validName4',
                            'name': 'a123!@#$%&*()_-+=,.?;:{}[]`~'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto2',
                            'name': 'auto2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO2dist2',
                            'name': 'autoO2dist2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase10',
                        'name': 'Testcase10'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'Device1',
                            'name': 'Device1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP1',
                            'name': 'GP1'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP3',
                            'name': 'GP3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase11',
                        'name': 'Testcase11'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'deleteGroup',
                            'name': 'Group Delete'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': '123456',
                            'name': 'Group Id valid 3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType':
                        'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': [{
                            'member': {
                                'id': 'Testcase1',
                                'name': 'Testcase1'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase11',
                                'name': 'Testcase11'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase13',
                                'name': 'Testcase13'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase14',
                                'name': 'Testcase14'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase15',
                                'name': 'Testcase15'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }]
                    }]
                }, {
                    'member': {
                        'id': 'Testcase12',
                        'name': 'Testcase12'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigFalse',
                            'name': 'Group with Admin Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'config_AllConfig',
                            'name': 'Group with All Config and configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase13',
                        'name': 'Testcase13'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigFalse',
                            'name': 'Group with All Config False'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfig',
                            'name': 'Group with All Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigDisabled',
                            'name': 'Group with All Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigNull',
                            'name': 'Group with All Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }]
                }],
                member=None,
                memberRoles=None,
                memberType=None)


            # addHop the Routes.
            # The `check` call validates return code
            # and some of the swagger schema.
            # Most schema checks are disabled.
            response = check(
                context.cl.Routes.addHop(
                    id='test1', 
                    body=hopDetails, 
                    memberType='EDGE_DEVICE'
                
                )
            )

            ### Can add tests here to validate the response content

        with pytest.allure.step("""Verify that user is able to add single hop in the route having router1->router(10)->5 each in schema using request POST "/routes/{id}/hops/{memberId}"."""):

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
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                    'hops': [{
                        'member': {
                            'id': 'validName4',
                            'name': 'a123!@#$%&*()_-+=,.?;:{}[]`~'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto2',
                            'name': 'auto2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'autoO2dist2',
                            'name': 'autoO2dist2'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase10',
                        'name': 'Testcase10'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'auto3',
                            'name': 'auto3'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'Device1',
                            'name': 'Device1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP1',
                            'name': 'GP1'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP3',
                            'name': 'GP3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase11',
                        'name': 'Testcase11'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                    'hops': [{
                        'member': {
                            'id': 'auto1',
                            'name': 'auto1'
                        },
                        'memberType': 'EDGE_DEVICE',
                        'memberRoles': ['DISTRIBUTION', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'EDGE'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'GP2',
                            'name': 'GP2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'deleteGroup',
                            'name': 'Group Delete'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': '123456',
                            'name': 'Group Id valid 3'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType':
                        'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': [{
                            'member': {
                                'id': 'Testcase1',
                                'name': 'Testcase1'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase11',
                                'name': 'Testcase11'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase13',
                                'name': 'Testcase13'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase14',
                                'name': 'Testcase14'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }, {
                            'member': {
                                'id': 'Testcase15',
                                'name': 'Testcase15'
                            },
                            'memberType': 'EDGE_DEVICE',
                            'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                            'hops': []
                        }]
                    }]
                }, {
                    'member': {
                        'id': 'Testcase12',
                        'name': 'Testcase12'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'P2OST1234',
                            'name': 'Group Id valid 2'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'POST_123:-.',
                            'name': 'Group Id valid 4'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigFalse',
                            'name': 'Group with Admin Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'config_AllConfig',
                            'name': 'Group with All Config and configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }]
                }, {
                    'member': {
                        'id': 'Testcase13',
                        'name': 'Testcase13'
                    },
                    'memberType':
                    'EDGE_DEVICE',
                    'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
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
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigTrue',
                            'name': 'Group with Admin Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'adminConfigNull',
                            'name': 'Group with Admin Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigFalse',
                            'name': 'Group with All Config False'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfig',
                            'name': 'Group with All Configuration'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigDisabled',
                            'name': 'Group with All Configuration Disabled'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }, {
                        'member': {
                            'id': 'AllConfigNull',
                            'name': 'Group with All Configuration Null'
                        },
                        'memberType': 'GROUP',
                        'memberRoles': ['DISTRIBUTION', 'EDGE', 'ORIGIN'],
                        'hops': []
                    }]
                }],
                member=None,
                memberRoles=None,
                memberType=None)


            # prepare the request, so we can modify it
            request = context.cl.Routes.addHop(
                    id='test1', 
                    body=hopDetails, 
                    memberType='EDGE_DEVICE'
                
            )

            ### Invalid JSON Error injection example
            ### Errors that result in valid JSON can be configured above.
            ### Otherwise, uncomment the code below (request.future....)

            # Get the generated payload and corrupt the metric
            # request.future.request.data = request.future.request.data.replace(
            #     '"metric": 1,', '"metric":,'
            # )

            # addHop the Routes, and check we got the error we expect
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
