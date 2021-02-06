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

from add_heartbeat import AddHeartbeatAction
from opsgenie_base_test_case import OpsGenieBaseActionTestCase


class AddHeartbeatTestCase(OpsGenieBaseActionTestCase):
    __test__ = True
    action_cls = AddHeartbeatAction

    def test_run_api_404(self):
        action, adapter = self._get_action_status_code(
            'POST',
            "mock://api.opsgenie.com/v2/heartbeats",
            status_code=404)

        self.assertRaises(ValueError,
                          action.run,
                          "Test")

    def test_run_invalid_json(self):
        action, adapter = self._get_action_invalid_json(
            'POST',
            "mock://api.opsgenie.com/v2/heartbeats")

        self.assertRaises(ValueError,
                          action.run,
                          "Test")

    def test_run_api_success(self):
        expected = self.load_json("add_heartbeat.json")

        action, adapter = self._get_mocked_action()
        adapter.register_uri('POST',
                             "mock://api.opsgenie.com/v2/heartbeats",
                             text=self.get_fixture_content("add_heartbeat.json"))

        result = action.run("Test")
        self.assertEqual(result, expected)
