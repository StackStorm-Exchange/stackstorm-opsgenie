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


class PingHeartbeatAction(OpsGenieBaseAction):
    def run(self, name, method=None):
        """
        Ping a Heartbeat

        Args:
        - name: Name of the heartbeat
        - method: Method for ping request. It can be PUT, POST, GET, PATCH.


        Returns:
        - dict: Data from OpsGenie
        """

        body = {}
        method = method

        data = self._req(method, "v2/heartbeats/" + pathname2url(name) + "/ping", body=body)

        return data
