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

from enable_integration import EnableIntegrationAction
from opsgenie_base_test_case import OpsGenieBaseActionTestCase


class EnableIntegrationTestCase(OpsGenieBaseActionTestCase):
    __test__ = True
    action_cls = EnableIntegrationAction

    def test_run_api_404(self):
        action, adapter = self._get_action_status_code(
            'POST',
            "mock://api.opsgenie.com/v2/integrations/32d16e6-020c-46f0-9383-4f0e32603b9d/enable",
            status_code=404)

        self.assertRaises(ValueError,
                          action.run,
                          "32d16e6-020c-46f0-9383-4f0e32603b9d", 'POST')

    def test_run_invalid_json(self):
        action, adapter = self._get_action_invalid_json(
            'POST',
            "mock://api.opsgenie.com/v2/integrations/32d16e6-020c-46f0-9383-4f0e32603b9d/enable")

        self.assertRaises(ValueError,
                          action.run,
                          "32d16e6-020c-46f0-9383-4f0e32603b9d", 'POST')

    def test_run_api_success(self):
        expected = self.load_json("enable_integration.json")

        action, adapter = self._get_mocked_action()
        adapter.register_uri('POST',
                             "mock://api.opsgenie.com/v2/integrations/32d16e6-020c-46f0-9383"
                             "-4f0e32603b9d/enable",
                             text=self.get_fixture_content("enable_integration.json"))

        result = action.run("32d16e6-020c-46f0-9383-4f0e32603b9d", 'POST')
        self.assertEqual(result, expected)
