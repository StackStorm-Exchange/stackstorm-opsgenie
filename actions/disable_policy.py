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

from lib.actions import OpsGenieBaseAction


class DisablePolicyAction(OpsGenieBaseAction):
    def run(self, policy_id, team_id):
        """
        Enable an alert policy in OpsGenie.

        Args:
        - policy_id: Id of policy.
        - team_id: Id of team that policy belongs
        Returns:
        - dict: Data from OpsGenie.
        """

        if team_id:
            payload = {"teamId": team_id}
        else:
            payload = {}

        data = self._req("POST",
                         "v2/policies/" + policy_id + "/disable",
                         payload=payload)
        return data
