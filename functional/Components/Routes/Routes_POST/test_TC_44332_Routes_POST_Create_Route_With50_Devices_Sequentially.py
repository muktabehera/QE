# -*- coding: UTF-8 -*-

"""PFE Component Tests - Routes.

* TC-44332 - Routes POST:

  Verify that user is able to create route with root->50 devices sequentially using request POST "/routes".


Equivalent test CURL command:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

Same, with test data:

  curl -H "Host: <client_host>" -H "Authorization: Bearer <valid_token>"
       -X POST -d @<JSON_data_file> -H "Content-Type: application/json"
       "<PF_host>://<client_host>/routes"

JSON data sent to PathFinder in this test:

    {
      "visibleInAllConfigurations": false,
      "configAdminCanEdit": false,
      "configurations": [
        {
          "id": "default",
          "host": "172.30.2.149"
        }
      ],
      "id": "wabe",
      "name": "wabe",
      "creationDate": "2016-03-01T12:34:58Z",
      "modificationDate": "2016-03-01T12:34:58Z",
      "hops": [
        {
          "member": {
            "id": "Testcase1",
            "name": "Testcase1"
          },
          "memberType": "EDGE_DEVICE",
          "memberRoles": [
            "ORIGIN",
            "EDGE",
            "DISTRIBUTION"
          ],
          "hops": [
            {
              "member": {
                "id": "Testcase10",
                "name": "Testcase10"
              },
              "memberType": "EDGE_DEVICE",
              "memberRoles": [
                "ORIGIN",
                "EDGE",
                "DISTRIBUTION"
              ],
              "hops": [
                {
                  "member": {
                    "id": "Testcase11",
                    "name": "Testcase11"
                  },
                  "memberType": "EDGE_DEVICE",
                  "memberRoles": [
                    "ORIGIN",
                    "EDGE",
                    "DISTRIBUTION"
                  ],
                  "hops": [
                    {
                      "member": {
                        "id": "Testcase12",
                        "name": "Testcase12"
                      },
                      "memberType": "EDGE_DEVICE",
                      "memberRoles": [
                        "ORIGIN",
                        "EDGE",
                        "DISTRIBUTION"
                      ],
                      "hops": [
                        {
                          "member": {
                            "id": "Testcase13",
                            "name": "Testcase13"
                          },
                          "memberType": "EDGE_DEVICE",
                          "memberRoles": [
                            "ORIGIN",
                            "EDGE",
                            "DISTRIBUTION"
                          ],
                          "hops": [
                            {
                              "member": {
                                "id": "Testcase14",
                                "name": "Testcase14"
                              },
                              "memberType": "EDGE_DEVICE",
                              "memberRoles": [
                                "ORIGIN",
                                "EDGE",
                                "DISTRIBUTION"
                              ],
                              "hops": [
                                {
                                  "member": {
                                    "id": "Testcase15",
                                    "name": "Testcase15"
                                  },
                                  "memberType": "EDGE_DEVICE",
                                  "memberRoles": [
                                    "ORIGIN",
                                    "EDGE",
                                    "DISTRIBUTION"
                                  ],
                                  "hops": [
                                    {
                                      "member": {
                                        "id": "Testcase16",
                                        "name": "Testcase16"
                                      },
                                      "memberType": "EDGE_DEVICE",
                                      "memberRoles": [
                                        "ORIGIN",
                                        "EDGE",
                                        "DISTRIBUTION"
                                      ],
                                      "hops": [
                                        {
                                          "member": {
                                            "id": "Testcase17",
                                            "name": "Testcase17"
                                          },
                                          "memberType": "EDGE_DEVICE",
                                          "memberRoles": [
                                            "ORIGIN",
                                            "EDGE",
                                            "DISTRIBUTION"
                                          ],
                                          "hops": [
                                            {
                                              "member": {
                                                "id": "Testcase18",
                                                "name": "Testcase18"
                                              },
                                              "memberType": "EDGE_DEVICE",
                                              "memberRoles": [
                                                "ORIGIN",
                                                "EDGE",
                                                "DISTRIBUTION"
                                              ],
                                              "hops": [
                                                {
                                                  "member": {
                                                    "id": "Testcase19",
                                                    "name": "Testcase19"
                                                  },
                                                  "memberType": "EDGE_DEVICE",
                                                  "memberRoles": [
                                                    "ORIGIN",
                                                    "EDGE",
                                                    "DISTRIBUTION"
                                                  ],
                                                  "hops": [
                                                    {
                                                      "member": {
                                                        "id": "Testcase2",
                                                        "name": "Testcase2"
                                                      },
                                                      "memberType": "EDGE_DEVICE",
                                                      "memberRoles": [
                                                        "ORIGIN",
                                                        "EDGE",
                                                        "DISTRIBUTION"
                                                      ],
                                                      "hops": [
                                                        {
                                                          "member": {
                                                            "id": "Testcase20",
                                                            "name": "Testcase20"
                                                          },
                                                          "memberType": "EDGE_DEVICE",
                                                          "memberRoles": [
                                                            "ORIGIN",
                                                            "EDGE",
                                                            "DISTRIBUTION"
                                                          ],
                                                          "hops": [
                                                            {
                                                              "member": {
                                                                "id": "Testcase21",
                                                                "name": "Testcase21"
                                                              },
                                                              "memberType": "EDGE_DEVICE",
                                                              "memberRoles": [
                                                                "ORIGIN",
                                                                "EDGE",
                                                                "DISTRIBUTION"
                                                              ],
                                                              "hops": [
                                                                {
                                                                  "member": {
                                                                    "id": "Testcase22",
                                                                    "name": "Testcase22"
                                                                  },
                                                                  "memberType": "EDGE_DEVICE",
                                                                  "memberRoles": [
                                                                    "ORIGIN",
                                                                    "EDGE",
                                                                    "DISTRIBUTION"
                                                                  ],
                                                                  "hops": [
                                                                    {
                                                                      "member": {
                                                                        "id": "Testcase23",
                                                                        "name": "Testcase23"
                                                                      },
                                                                      "memberType": "EDGE_DEVICE",
                                                                      "memberRoles": [
                                                                        "ORIGIN",
                                                                        "EDGE",
                                                                        "DISTRIBUTION"
                                                                      ],
                                                                      "hops": [
                                                                        {
                                                                          "member": {
                                                                            "id": "Testcase24",
                                                                            "name": "Testcase24"
                                                                          },
                                                                          "memberType": "EDGE_DEVICE",
                                                                          "memberRoles": [
                                                                            "ORIGIN",
                                                                            "EDGE",
                                                                            "DISTRIBUTION"
                                                                          ],
                                                                          "hops": [
                                                                            {
                                                                              "member": {
                                                                                "id": "Testcase25",
                                                                                "name": "Testcase25"
                                                                              },
                                                                              "memberType": "EDGE_DEVICE",
                                                                              "memberRoles": [
                                                                                "ORIGIN",
                                                                                "EDGE",
                                                                                "DISTRIBUTION"
                                                                              ],
                                                                              "hops": [
                                                                                {
                                                                                  "member": {
                                                                                    "id": "Testcase26",
                                                                                    "name": "Testcase26"
                                                                                  },
                                                                                  "memberType": "EDGE_DEVICE",
                                                                                  "memberRoles": [
                                                                                    "ORIGIN",
                                                                                    "EDGE",
                                                                                    "DISTRIBUTION"
                                                                                  ],
                                                                                  "hops": [
                                                                                    {
                                                                                      "member": {
                                                                                        "id": "Testcase27",
                                                                                        "name": "Testcase27"
                                                                                      },
                                                                                      "memberType": "EDGE_DEVICE",
                                                                                      "memberRoles": [
                                                                                        "ORIGIN",
                                                                                        "EDGE",
                                                                                        "DISTRIBUTION"
                                                                                      ],
                                                                                      "hops": [
                                                                                        {
                                                                                          "member": {
                                                                                            "id": "Testcase28",
                                                                                            "name": "Testcase28"
                                                                                          },
                                                                                          "memberType": "EDGE_DEVICE",
                                                                                          "memberRoles": [
                                                                                            "ORIGIN",
                                                                                            "EDGE",
                                                                                            "DISTRIBUTION"
                                                                                          ],
                                                                                          "hops": [
                                                                                            {
                                                                                              "member": {
                                                                                                "id": "Testcase29",
                                                                                                "name": "Testcase29"
                                                                                              },
                                                                                              "memberType": "EDGE_DEVICE",
                                                                                              "memberRoles": [
                                                                                                "ORIGIN",
                                                                                                "EDGE",
                                                                                                "DISTRIBUTION"
                                                                                              ],
                                                                                              "hops": [
                                                                                                {
                                                                                                  "member": {
                                                                                                    "id": "Testcase3",
                                                                                                    "name": "Testcase3"
                                                                                                  },
                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                  "memberRoles": [
                                                                                                    "ORIGIN",
                                                                                                    "EDGE",
                                                                                                    "DISTRIBUTION"
                                                                                                  ],
                                                                                                  "hops": [
                                                                                                    {
                                                                                                      "member": {
                                                                                                        "id": "Testcase30",
                                                                                                        "name": "Testcase30"
                                                                                                      },
                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                      "memberRoles": [
                                                                                                        "ORIGIN",
                                                                                                        "EDGE",
                                                                                                        "DISTRIBUTION"
                                                                                                      ],
                                                                                                      "hops": [
                                                                                                        {
                                                                                                          "member": {
                                                                                                            "id": "Testcase31",
                                                                                                            "name": "Testcase31"
                                                                                                          },
                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                          "memberRoles": [
                                                                                                            "ORIGIN",
                                                                                                            "EDGE",
                                                                                                            "DISTRIBUTION"
                                                                                                          ],
                                                                                                          "hops": [
                                                                                                            {
                                                                                                              "member": {
                                                                                                                "id": "Testcase32",
                                                                                                                "name": "Testcase32"
                                                                                                              },
                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                              "memberRoles": [
                                                                                                                "ORIGIN",
                                                                                                                "EDGE",
                                                                                                                "DISTRIBUTION"
                                                                                                              ],
                                                                                                              "hops": [
                                                                                                                {
                                                                                                                  "member": {
                                                                                                                    "id": "Testcase33",
                                                                                                                    "name": "Testcase33"
                                                                                                                  },
                                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                                  "memberRoles": [
                                                                                                                    "ORIGIN",
                                                                                                                    "EDGE",
                                                                                                                    "DISTRIBUTION"
                                                                                                                  ],
                                                                                                                  "hops": [
                                                                                                                    {
                                                                                                                      "member": {
                                                                                                                        "id": "Testcase34",
                                                                                                                        "name": "Testcase34"
                                                                                                                      },
                                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                                      "memberRoles": [
                                                                                                                        "ORIGIN",
                                                                                                                        "EDGE",
                                                                                                                        "DISTRIBUTION"
                                                                                                                      ],
                                                                                                                      "hops": [
                                                                                                                        {
                                                                                                                          "member": {
                                                                                                                            "id": "Testcase35",
                                                                                                                            "name": "Testcase35"
                                                                                                                          },
                                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                                          "memberRoles": [
                                                                                                                            "ORIGIN",
                                                                                                                            "EDGE",
                                                                                                                            "DISTRIBUTION"
                                                                                                                          ],
                                                                                                                          "hops": [
                                                                                                                            {
                                                                                                                              "member": {
                                                                                                                                "id": "Testcase36",
                                                                                                                                "name": "Testcase36"
                                                                                                                              },
                                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                                              "memberRoles": [
                                                                                                                                "ORIGIN",
                                                                                                                                "EDGE",
                                                                                                                                "DISTRIBUTION"
                                                                                                                              ],
                                                                                                                              "hops": [
                                                                                                                                {
                                                                                                                                  "member": {
                                                                                                                                    "id": "Testcase37",
                                                                                                                                    "name": "Testcase37"
                                                                                                                                  },
                                                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                                                  "memberRoles": [
                                                                                                                                    "ORIGIN",
                                                                                                                                    "EDGE",
                                                                                                                                    "DISTRIBUTION"
                                                                                                                                  ],
                                                                                                                                  "hops": [
                                                                                                                                    {
                                                                                                                                      "member": {
                                                                                                                                        "id": "Testcase38",
                                                                                                                                        "name": "Testcase38"
                                                                                                                                      },
                                                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                                                      "memberRoles": [
                                                                                                                                        "ORIGIN",
                                                                                                                                        "EDGE",
                                                                                                                                        "DISTRIBUTION"
                                                                                                                                      ],
                                                                                                                                      "hops": [
                                                                                                                                        {
                                                                                                                                          "member": {
                                                                                                                                            "id": "Testcase39",
                                                                                                                                            "name": "Testcase39"
                                                                                                                                          },
                                                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                                                          "memberRoles": [
                                                                                                                                            "ORIGIN",
                                                                                                                                            "EDGE",
                                                                                                                                            "DISTRIBUTION"
                                                                                                                                          ],
                                                                                                                                          "hops": [
                                                                                                                                            {
                                                                                                                                              "member": {
                                                                                                                                                "id": "Testcase4",
                                                                                                                                                "name": "Testcase4"
                                                                                                                                              },
                                                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                                                              "memberRoles": [
                                                                                                                                                "ORIGIN",
                                                                                                                                                "EDGE",
                                                                                                                                                "DISTRIBUTION"
                                                                                                                                              ],
                                                                                                                                              "hops": [
                                                                                                                                                {
                                                                                                                                                  "member": {
                                                                                                                                                    "id": "Testcase40",
                                                                                                                                                    "name": "Testcase40"
                                                                                                                                                  },
                                                                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                                                                  "memberRoles": [
                                                                                                                                                    "ORIGIN",
                                                                                                                                                    "EDGE",
                                                                                                                                                    "DISTRIBUTION"
                                                                                                                                                  ],
                                                                                                                                                  "hops": [
                                                                                                                                                    {
                                                                                                                                                      "member": {
                                                                                                                                                        "id": "Testcase41",
                                                                                                                                                        "name": "Testcase41"
                                                                                                                                                      },
                                                                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                                                                      "memberRoles": [
                                                                                                                                                        "ORIGIN",
                                                                                                                                                        "EDGE",
                                                                                                                                                        "DISTRIBUTION"
                                                                                                                                                      ],
                                                                                                                                                      "hops": [
                                                                                                                                                        {
                                                                                                                                                          "member": {
                                                                                                                                                            "id": "Testcase42",
                                                                                                                                                            "name": "Testcase42"
                                                                                                                                                          },
                                                                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                                                                          "memberRoles": [
                                                                                                                                                            "ORIGIN",
                                                                                                                                                            "EDGE",
                                                                                                                                                            "DISTRIBUTION"
                                                                                                                                                          ],
                                                                                                                                                          "hops": [
                                                                                                                                                            {
                                                                                                                                                              "member": {
                                                                                                                                                                "id": "Testcase43",
                                                                                                                                                                "name": "Testcase43"
                                                                                                                                                              },
                                                                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                                                                              "memberRoles": [
                                                                                                                                                                "ORIGIN",
                                                                                                                                                                "EDGE",
                                                                                                                                                                "DISTRIBUTION"
                                                                                                                                                              ],
                                                                                                                                                              "hops": [
                                                                                                                                                                {
                                                                                                                                                                  "member": {
                                                                                                                                                                    "id": "Testcase44",
                                                                                                                                                                    "name": "Testcase44"
                                                                                                                                                                  },
                                                                                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                                                                                  "memberRoles": [
                                                                                                                                                                    "ORIGIN",
                                                                                                                                                                    "EDGE",
                                                                                                                                                                    "DISTRIBUTION"
                                                                                                                                                                  ],
                                                                                                                                                                  "hops": [
                                                                                                                                                                    {
                                                                                                                                                                      "member": {
                                                                                                                                                                        "id": "Testcase45",
                                                                                                                                                                        "name": "Testcase45"
                                                                                                                                                                      },
                                                                                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                                                                                      "memberRoles": [
                                                                                                                                                                        "ORIGIN",
                                                                                                                                                                        "EDGE",
                                                                                                                                                                        "DISTRIBUTION"
                                                                                                                                                                      ],
                                                                                                                                                                      "hops": [
                                                                                                                                                                        {
                                                                                                                                                                          "member": {
                                                                                                                                                                            "id": "Testcase46",
                                                                                                                                                                            "name": "Testcase46"
                                                                                                                                                                          },
                                                                                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                                                                                          "memberRoles": [
                                                                                                                                                                            "ORIGIN",
                                                                                                                                                                            "EDGE",
                                                                                                                                                                            "DISTRIBUTION"
                                                                                                                                                                          ],
                                                                                                                                                                          "hops": [
                                                                                                                                                                            {
                                                                                                                                                                              "member": {
                                                                                                                                                                                "id": "Testcase47",
                                                                                                                                                                                "name": "Testcase47"
                                                                                                                                                                              },
                                                                                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                                                                                              "memberRoles": [
                                                                                                                                                                                "ORIGIN",
                                                                                                                                                                                "EDGE",
                                                                                                                                                                                "DISTRIBUTION"
                                                                                                                                                                              ],
                                                                                                                                                                              "hops": [
                                                                                                                                                                                {
                                                                                                                                                                                  "member": {
                                                                                                                                                                                    "id": "Testcase48",
                                                                                                                                                                                    "name": "Testcase48"
                                                                                                                                                                                  },
                                                                                                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                                                                                                  "memberRoles": [
                                                                                                                                                                                    "ORIGIN",
                                                                                                                                                                                    "EDGE",
                                                                                                                                                                                    "DISTRIBUTION"
                                                                                                                                                                                  ],
                                                                                                                                                                                  "hops": [
                                                                                                                                                                                    {
                                                                                                                                                                                      "member": {
                                                                                                                                                                                        "id": "Testcase5",
                                                                                                                                                                                        "name": "Testcase5"
                                                                                                                                                                                      },
                                                                                                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                                                                                                      "memberRoles": [
                                                                                                                                                                                        "ORIGIN",
                                                                                                                                                                                        "EDGE",
                                                                                                                                                                                        "DISTRIBUTION"
                                                                                                                                                                                      ],
                                                                                                                                                                                      "hops": [
                                                                                                                                                                                        {
                                                                                                                                                                                          "member": {
                                                                                                                                                                                            "id": "Testcase49",
                                                                                                                                                                                            "name": "Testcase49"
                                                                                                                                                                                          },
                                                                                                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                                                                                                          "memberRoles": [
                                                                                                                                                                                            "ORIGIN",
                                                                                                                                                                                            "EDGE",
                                                                                                                                                                                            "DISTRIBUTION"
                                                                                                                                                                                          ],
                                                                                                                                                                                          "hops": [
                                                                                                                                                                                            {
                                                                                                                                                                                              "member": {
                                                                                                                                                                                                "id": "Testcase50",
                                                                                                                                                                                                "name": "Testcase50"
                                                                                                                                                                                              },
                                                                                                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                                                                                                              "memberRoles": [
                                                                                                                                                                                                "ORIGIN",
                                                                                                                                                                                                "EDGE",
                                                                                                                                                                                                "DISTRIBUTION"
                                                                                                                                                                                              ],
                                                                                                                                                                                              "hops": [
                                                                                                                                                                                                {
                                                                                                                                                                                                  "member": {
                                                                                                                                                                                                    "id": "Testcase6",
                                                                                                                                                                                                    "name": "Testcase6"
                                                                                                                                                                                                  },
                                                                                                                                                                                                  "memberType": "EDGE_DEVICE",
                                                                                                                                                                                                  "memberRoles": [
                                                                                                                                                                                                    "ORIGIN",
                                                                                                                                                                                                    "EDGE",
                                                                                                                                                                                                    "DISTRIBUTION"
                                                                                                                                                                                                  ],
                                                                                                                                                                                                  "hops": [
                                                                                                                                                                                                    {
                                                                                                                                                                                                      "member": {
                                                                                                                                                                                                        "id": "Testcase7",
                                                                                                                                                                                                        "name": "Testcase7"
                                                                                                                                                                                                      },
                                                                                                                                                                                                      "memberType": "EDGE_DEVICE",
                                                                                                                                                                                                      "memberRoles": [
                                                                                                                                                                                                        "ORIGIN",
                                                                                                                                                                                                        "EDGE",
                                                                                                                                                                                                        "DISTRIBUTION"
                                                                                                                                                                                                      ],
                                                                                                                                                                                                      "hops": [
                                                                                                                                                                                                        {
                                                                                                                                                                                                          "member": {
                                                                                                                                                                                                            "id": "Testcase8",
                                                                                                                                                                                                            "name": "Testcase8"
                                                                                                                                                                                                          },
                                                                                                                                                                                                          "memberType": "EDGE_DEVICE",
                                                                                                                                                                                                          "memberRoles": [
                                                                                                                                                                                                            "ORIGIN",
                                                                                                                                                                                                            "EDGE",
                                                                                                                                                                                                            "DISTRIBUTION"
                                                                                                                                                                                                          ],
                                                                                                                                                                                                          "hops": [
                                                                                                                                                                                                            {
                                                                                                                                                                                                              "member": {
                                                                                                                                                                                                                "id": "Testcase9",
                                                                                                                                                                                                                "name": "Testcase9"
                                                                                                                                                                                                              },
                                                                                                                                                                                                              "memberType": "EDGE_DEVICE",
                                                                                                                                                                                                              "memberRoles": [
                                                                                                                                                                                                                "ORIGIN",
                                                                                                                                                                                                                "EDGE",
                                                                                                                                                                                                                "DISTRIBUTION"
                                                                                                                                                                                                              ],
                                                                                                                                                                                                              "hops": []
                                                                                                                                                                                                            }
                                                                                                                                                                                                          ]
                                                                                                                                                                                                        }
                                                                                                                                                                                                      ]
                                                                                                                                                                                                    }
                                                                                                                                                                                                  ]
                                                                                                                                                                                                }
                                                                                                                                                                                              ]
                                                                                                                                                                                            }
                                                                                                                                                                                          ]
                                                                                                                                                                                        }
                                                                                                                                                                                      ]
                                                                                                                                                                                    }
                                                                                                                                                                                  ]
                                                                                                                                                                                }
                                                                                                                                                                              ]
                                                                                                                                                                            }
                                                                                                                                                                          ]
                                                                                                                                                                        }
                                                                                                                                                                      ]
                                                                                                                                                                    }
                                                                                                                                                                  ]
                                                                                                                                                                }
                                                                                                                                                              ]
                                                                                                                                                            }
                                                                                                                                                          ]
                                                                                                                                                        }
                                                                                                                                                      ]
                                                                                                                                                    }
                                                                                                                                                  ]
                                                                                                                                                }
                                                                                                                                              ]
                                                                                                                                            }
                                                                                                                                          ]
                                                                                                                                        }
                                                                                                                                      ]
                                                                                                                                    }
                                                                                                                                  ]
                                                                                                                                }
                                                                                                                              ]
                                                                                                                            }
                                                                                                                          ]
                                                                                                                        }
                                                                                                                      ]
                                                                                                                    }
                                                                                                                  ]
                                                                                                                }
                                                                                                              ]
                                                                                                            }
                                                                                                          ]
                                                                                                        }
                                                                                                      ]
                                                                                                    }
                                                                                                  ]
                                                                                                }
                                                                                              ]
                                                                                            }
                                                                                          ]
                                                                                        }
                                                                                      ]
                                                                                    }
                                                                                  ]
                                                                                }
                                                                              ]
                                                                            }
                                                                          ]
                                                                        }
                                                                      ]
                                                                    }
                                                                  ]
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        }
                                                      ]
                                                    }
                                                  ]
                                                }
                                              ]
                                            }
                                          ]
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }

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

    @pytest.allure.link('https://jira.qumu.com/browse/TC-44332')
    @pytest.mark.Routes
    @pytest.mark.POST
    def test_TC_44332_POST_Routes_Create_Route_With50_Devices_Sequentially(self, context):
        """TC-44332 - Routes-POST
           Verify that user is able to create route with root->50 devices sequentially using request POST "/routes"."""
        # Define a test step
        with pytest.allure.step("""Verify that user is able to create route with root->50 devices sequentially using request POST "/routes"."""):

            ### Positive test example

            # Test case configuration

            ### THIS CODE IS WAY TOO LONG,
            ### and have to be refactored.

            # hopDetails = context.sc.HopDetails(constraintViolations=None, hops=[{'member': {'id': 'Testcase1', 'name': 'Testcase1'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase10', 'name': 'Testcase10'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase11', 'name': 'Testcase11'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase12', 'name': 'Testcase12'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase13', 'name': 'Testcase13'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase14', 'name': 'Testcase14'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase15', 'name': 'Testcase15'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase16', 'name': 'Testcase16'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase17', 'name': 'Testcase17'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase18', 'name': 'Testcase18'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase19', 'name': 'Testcase19'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase2', 'name': 'Testcase2'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase20', 'name': 'Testcase20'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase21', 'name': 'Testcase21'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase22', 'name': 'Testcase22'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase23', 'name': 'Testcase23'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase24', 'name': 'Testcase24'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase25', 'name': 'Testcase25'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase26', 'name': 'Testcase26'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase27', 'name': 'Testcase27'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase28', 'name': 'Testcase28'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase29', 'name': 'Testcase29'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase3', 'name': 'Testcase3'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase30', 'name': 'Testcase30'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase31', 'name': 'Testcase31'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase32', 'name': 'Testcase32'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase33', 'name': 'Testcase33'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase34', 'name': 'Testcase34'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase35', 'name': 'Testcase35'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase36', 'name': 'Testcase36'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase37', 'name': 'Testcase37'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase38', 'name': 'Testcase38'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase39', 'name': 'Testcase39'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase4', 'name': 'Testcase4'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase40', 'name': 'Testcase40'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase41', 'name': 'Testcase41'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase42', 'name': 'Testcase42'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase43', 'name': 'Testcase43'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase44', 'name': 'Testcase44'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase45', 'name': 'Testcase45'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase46', 'name': 'Testcase46'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase47', 'name': 'Testcase47'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase48', 'name': 'Testcase48'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase5', 'name': 'Testcase5'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase49', 'name': 'Testcase49'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase50', 'name': 'Testcase50'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase6', 'name': 'Testcase6'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase7', 'name': 'Testcase7'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase8', 'name': 'Testcase8'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase9', 'name': 'Testcase9'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': []}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}], member=None, memberRoles=None, memberType=None)
            #

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

        with pytest.allure.step("""Verify that user is able to create route with root->50 devices sequentially using request POST "/routes"."""):

            ### Negative test example

            ### THIS CODE IS WAY TOO LONG,
            ### and have to be refactored.

            # Test case configuration
            # hopDetails = context.sc.HopDetails(constraintViolations=None, hops=[{'member': {'id': 'Testcase1', 'name': 'Testcase1'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase10', 'name': 'Testcase10'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase11', 'name': 'Testcase11'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase12', 'name': 'Testcase12'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase13', 'name': 'Testcase13'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase14', 'name': 'Testcase14'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase15', 'name': 'Testcase15'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase16', 'name': 'Testcase16'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase17', 'name': 'Testcase17'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase18', 'name': 'Testcase18'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase19', 'name': 'Testcase19'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase2', 'name': 'Testcase2'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase20', 'name': 'Testcase20'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase21', 'name': 'Testcase21'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase22', 'name': 'Testcase22'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase23', 'name': 'Testcase23'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase24', 'name': 'Testcase24'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase25', 'name': 'Testcase25'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase26', 'name': 'Testcase26'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase27', 'name': 'Testcase27'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase28', 'name': 'Testcase28'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase29', 'name': 'Testcase29'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase3', 'name': 'Testcase3'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase30', 'name': 'Testcase30'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase31', 'name': 'Testcase31'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase32', 'name': 'Testcase32'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase33', 'name': 'Testcase33'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase34', 'name': 'Testcase34'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase35', 'name': 'Testcase35'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase36', 'name': 'Testcase36'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase37', 'name': 'Testcase37'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase38', 'name': 'Testcase38'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase39', 'name': 'Testcase39'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase4', 'name': 'Testcase4'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase40', 'name': 'Testcase40'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase41', 'name': 'Testcase41'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase42', 'name': 'Testcase42'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase43', 'name': 'Testcase43'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase44', 'name': 'Testcase44'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase45', 'name': 'Testcase45'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase46', 'name': 'Testcase46'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase47', 'name': 'Testcase47'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase48', 'name': 'Testcase48'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase5', 'name': 'Testcase5'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase49', 'name': 'Testcase49'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase50', 'name': 'Testcase50'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase6', 'name': 'Testcase6'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase7', 'name': 'Testcase7'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase8', 'name': 'Testcase8'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': [{'member': {'id': 'Testcase9', 'name': 'Testcase9'}, 'memberType': 'EDGE_DEVICE', 'memberRoles': ['ORIGIN', 'EDGE', 'DISTRIBUTION'], 'hops': []}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}], member=None, memberRoles=None, memberType=None)


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
