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
from six.moves.urllib.request import pathname2url

from lib.actions import OpsGenieBaseAction


class AcknowledgeAlertAction(OpsGenieBaseAction):
    def run(self, alert_id=None, alias=None, user=None, note=None, source="StackStorm"):
        """
        Acknowledge alert request is used to acknowledge open alerts in OpsGenie.

        Args:
        - alert_id: Id of the alert that will be acknowledged.
        - alias: Alias of the alert that will be acknowledged.
        - user: Default owner of the execution.
        - note: Additional alert note
        - source: User defined field to specify source of acknowledge action.

        Returns:
        - dict: Data from OpsGenie

        Raises:
        - ValueError: If alias and alert_id are None.
        """

        body = {"source": source}
        parameters = {}

        if alert_id:
            identifier = pathname2url(alert_id)  # default
            parameters["identifierType"] = "id"
        elif alias:
            identifier = pathname2url(alias)
            parameters["identifierType"] = "alias"
        else:
            raise ValueError("Need one of alias or alert_id to be set.")

        if user:
            body["user"] = user

        if note:
            body["note"] = note

        data = self._req(
            "POST", "v2/alerts/" + identifier + "/acknowledge", body=body, payload=parameters
        )

        return data
