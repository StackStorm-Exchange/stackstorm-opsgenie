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

from .lib.actions import OpsGenieBaseAction


class DeleteAlertAction(OpsGenieBaseAction):
    def run(self, alert_id=None, alias=None, user=None, source="StackStorm"):
        """
        Delete an OpsGenie alert.

        Args
        - alert_id: Id of the alert that will be deleted.
        - alias: Alias of the alert will be deleted.
        - user: Default owner of the execution.
        - source: User defined field to specify source of delete action.

        Returns:
        - dict: Data from OpsGenie.

        Raises:
        - ValueError: If alert_id and alias are None.
        """

        payload = {}
        if source:
            if len(source) > 100:
                raise ValueError("source is too long, can't be over 100 chars.")
            else:
                payload['source'] = source

        if alert_id:
            identifier = pathname2url(alert_id)
            payload['identifierType'] = 'id'
        elif alias:
            identifier = pathname2url(alias)
            payload['identifierType'] = 'alias'
        else:
            raise ValueError("Need one of alert_id or alias.")

        if user:
            if len(user) > 100:
                raise ValueError("User is too long, can't be over 100 chars.")
            else:
                payload["user"] = "user"

        data = self._req("DELETE",
                         "v2/alerts/" + identifier,
                         payload=payload)
        return data
