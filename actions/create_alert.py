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


class CreateAlertAction(OpsGenieBaseAction):
    def run(self, message, alias=None,
            description=None, responders=None, visibleTo=None, actions=None,
            tags=None, details=None, entity=None, source="StackStorm",
            priority=None, user=None, note=None
            ):
        """
        Create alert in OpsGenie.

        Args:
        - message: Alert text limited to 130 characters
        - alias: Used for alert deduplication.
        - description: Detailed description of the alert.
        - responders: Teams, users, escalations and schedules that the alert will be routed to
        send notifications.
        - visibleTo: Teams and users that the alert will become visible to without sending any
        notification.
        - actions: A comma separated list of actions that can be executed.
        - tags: A comma separated list of labels attached to the alert.
        - details: Set of user defined properties.
        - entity: The entity the alert is related to.
        - source: Field to specify source of alert.
        - priority: Priority level of the alert.
        - user: Default owner of the execution.
        - note: Additional alert note.

        Returns:
        - dict: Data returned by OpsGenie.

        Raises:
        - ValueError: If description or message is too long.
        """

        responders_list = []
        visibleTo_list = []

        if len(message) > 130:
            raise ValueError("Message length ({}) is over 130 chars".format(
                len(message)))
        else:
            body = {"message": message}

        if alias:
            if len(alias) > 512:
                raise ValueError("alias is too long, can't be over 512 chars.")
            else:
                body["alias"] = alias

        if description:
            if len(description) > 15000:
                raise ValueError("Description is too long, can't be over 15000 chars.")
            else:
                body["description"] = description

        if responders:
            for responder in responders:
                responder_dict = {}
                splitted = responder.rsplit("-", 1)
                responder_dict["name"] = str(splitted[0])
                responder_dict["type"] = str(splitted[1])
                responders_list.append(responder_dict)
            body["responders"] = responders_list

        if visibleTo:
            for visibleOne in visibleTo:
                visibleTo_dict = {}
                split = visibleOne.rsplit("-", 1)
                visibleTo_dict["name"] = str(split[0])
                visibleTo_dict["type"] = str(split[1])
                visibleTo_list.append(visibleTo_dict)

            body["visibleTo"] = visibleTo_list

        if actions:
            body["actions"] = actions

        if tags:
            body["tags"] = tags

        if details:
            if len(details) > 8000:
                raise ValueError("Details is too long, can't be over 8000 chars.")
            else:
                body["details"] = details

        if entity:
            if len(entity) > 512:
                raise ValueError("Entity is too long, can't be over 512 chars.")
            else:
                body["entity"] = entity

        if source:
            if len(source) > 100:
                raise ValueError("Source is too long, can't be over 100 chars.")
            else:
                body["source"] = source

        if priority:
            body["priority"] = priority

        if user:
            if len(user) > 100:
                raise ValueError("User is too long, can't be over 100 chars.")
            else:
                body['user'] = user

        if note:
            if len(note) > 25000:
                raise ValueError("Note is too long, can't be over 25000 chars.")
            else:
                body['note'] = note

        data = self._req("POST",
                         "v2/alerts",
                         body=body)

        return data
