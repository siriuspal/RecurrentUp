""" Class for talking to ClickUp API """

import requests


class ClickUp:
    """ Clickup API wrapper required for the project """

    def __init__(self, token):

        self.token = token

    def get_team(self):
        """ Get team and team member details for which token is provided """

        headers = {
            "Authorization": self.token
            }

        response = requests.get('https://api.clickup.com/api/v1/team', headers=headers)

        response_json = response.json()

        return response_json


    def get_space(self, team):
        """ Get information on Space for given team """

        headers = {
            "Authorization": self.token
            }

        response = requests.get('https://api.clickup.com/api/v1/team/%s/space' %team,
                                headers=headers)

        response_json = response.json()

        return response_json


    def get_proj(self, space):
        """ Get information on project including lists for a given space """
        headers = {
            "Authorization": self.token
            }

        response = requests.get('https://api.clickup.com/api/v1/space/%s/project' %space,
                                headers=headers)

        response_json = response.json()

        return response_json


    def create_list(self, name, proj):
        """ Create a Task with given name in a given project """
        values = {
            "name": name
        }

        headers = {
            "Authorization": self.token
        }

        response = requests.post('https://api.clickup.com/api/v1/project/%s/list' %proj,
                                 data=values, headers=headers)

        response_json = response.json()

        return response_json


    def create_task(self, lis):
        """ Create a task in a given list """
        values = {
            "name": "NewTaskName",
            "content": "New Task Content",
            "assignees": [65080],
            "status": "Open",
            "priority": 3,
            "due_date": "1508369194377"
        }

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

        response = requests.post('https://api.clickup.com/api/v1/list/%s/task' %lis,
                                 data=values, headers=headers)

        response_json = response.text

        return response_json


cu = ClickUp('token')

#print(cu.get_team())
#print(cu.get_space(602544))
#print(cu.get_proj(603365))
#print(cu.create_list('Trial Task 1', 606540))
print(cu.create_task(614774))
