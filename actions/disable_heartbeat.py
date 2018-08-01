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
import urllib

from lib.actions import OpsGenieBaseAction


class DisableHeartbeatAction(OpsGenieBaseAction):
    def run(self, name):
        """
        Disable monitored heartbeat in OpsGenie

        Args:
        - name: Name of the heartbeat.

        Returns:
        - dict: data from OpsGenie.
        """

        body = {}
        name_url = urllib.pathname2url(name)

        data = self._req("POST",
                         "v2/heartbeats/"+name_url+"/disable",
                         body=body)

        return data
