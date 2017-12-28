import requests
import json

API_TOKEN = 'MYTOKEN'


def get_team(token):
    headers = {
        "Authorization": token
        }

    response = requests.get('https://api.clickup.com/api/v1/team', headers=headers)

    response_json = response.json()

    return response_json


def get_space(token):
    headers = {
        "Authorization": token
        }

    response = requests.get('https://api.clickup.com/api/v1/team/602544/space', headers=headers)

    response_json = response.json()

    return response_json


def get_proj(token):
    headers = {
        "Authorization": token
        }

    response = requests.get('https://api.clickup.com/api/v1/space/603365/project', headers=headers)

    response_json = response.json()

    return response_json


def create_list(token):
    values = {
        "name": "New List 3"
    }

    headers = {
        "Authorization": token
    }

    response = requests.post('https://api.clickup.com/api/v1/project/606540/list',
                             data=values, headers=headers)

    response_json = response.json()

    return response_json


def create_task(token):
    values = {
        "name": "New Task Name",
        "content": "New Task Content",
        "assignees": [65080],
        "status": "Open",
        "priority": 3,
        "due_date": "1508369194377"
    }

    headers = {
        "Authorization": token,
        "Content-Type": 'application/json'
    }

    response = requests.post('https://api.clickup.com/api/v1/list/614774/task',
                             data=values, headers=headers)

    response_json = response.text

    return response_json

"""
print(get_team(API_TOKEN))
print(get_space(API_TOKEN))
print(get_proj(API_TOKEN))
print(create_list(API_TOKEN))
"""
print(create_task(API_TOKEN))
