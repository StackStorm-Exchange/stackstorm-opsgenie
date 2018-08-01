# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

from opsgenie_base_test_case import OpsGenieBaseActionTestCase

from get_request_status import GetRequestStatusAction


class GetRequestStatusTestCase(OpsGenieBaseActionTestCase):
    __test__ = True
    action_cls = GetRequestStatusAction

    def test_run_api_404(self):
        action, adapter = self._get_action_status_code(
            'GET',
            "mock://api.opsgenie.com/v2/alerts/requests/513085b8-caf3-4f91-aa23-be5fdefc3570",
            status_code=404)

        self.assertRaises(ValueError,
                          action.run,
                          "513085b8-caf3-4f91-aa23-be5fdefc3570")

    def test_run_invalid_json(self):
        action, adapter = self._get_action_invalid_json(
            'GET',
            "mock://api.opsgenie.com/v2/alerts/requests/513085b8-caf3-4f91-aa23-be5fdefc3570")

        self.assertRaises(ValueError,
                          action.run,
                          "513085b8-caf3-4f91-aa23-be5fdefc3570")

    def test_run_api_success(self):
        expected = self.load_json("get_request_status.json")

        action, adapter = self._get_mocked_action()
        adapter.register_uri('GET',
                             "mock://api.opsgenie.com/v2/alerts/requests/513085b8-caf3-4f91-aa23-be5fdefc3570",
                             text=self.get_fixture_content("get_request_status.json"))

        result = action.run("513085b8-caf3-4f91-aa23-be5fdefc3570")
        self.assertEqual(result, expected)
