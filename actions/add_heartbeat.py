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


class AddHeartbeatAction(OpsGenieBaseAction):
    def run(self, name, interval=None, interval_unit=None, description=None, enabled=False, ownerTeamName=None, alertMessage=None, alertTags=None,alertPriority=None):
        """
        Add a Heartbeat to OpsGenie

        Args:
        - name: Name of the heartbeat
        - interval: Specifies how often a heartbeat message should be expected.
        - intervalUnit: interval specified as minutes, hours or days.
        - description: An optional description of the heartbeat.
        - enabled: Enable/disable heartbeat monitoring.
        - ownerTeam: Owner team of the heartbeat, consisting id and/or name of the owner team
        - alertMessage: Specifies the alert message for heartbeat expiration alert.
        - alertTags: Specifies the alert tags for heartbeat expiration alert.
        - alertPriority: Specifies the alert priority for heartbeat expiration alert.

        Returns:
        - dict: Data from OpsGenie
        """

        body = {"enabled": enabled}
        ownerTeam = {}

        if name:
            if len(name) > 200:
                raise ValueError("name is too long, can't be over 200 chars.")
            else:
                body["name"] = name

        if interval:
            body["interval"] = interval

        if interval_unit:
            body["intervalUnit"] = interval_unit

        if description:
            if len(description) > 10000:
                raise ValueError("name is too long, can't be over 200 chars.")
            else:
                body["description"] = description

        if ownerTeamName:
            ownerTeam["name"] = ownerTeamName
            body["ownerTeam"] = ownerTeam

        if alertMessage:
            if len(alertMessage) > 130:
                raise ValueError("alertMessage is too long, can't be over 130 chars.")
            else:
                body["alertMessage"] = alertMessage

        if alertTags:
            body["alertTags"] = alertTags

        if alertPriority:
            body["alertPriority"] = alertPriority

        data = self._req("POST",
                         "v2/heartbeats",
                         body=body)

        return data
