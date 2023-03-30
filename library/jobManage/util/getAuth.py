import requests
import json


def getToken():
    url = 'http://146.56.203.127:8143/library/api/library-prod/auth/oauth/token?username=testuser&password=123456!@%23&grant_type=password&scope='
    headers = {'content-type': "application/json", 'Authorization': 'Basic bWVzc2FnaW5nLWNsaWVudDpzZWNyZXQ='}
    response = requests.post(url=url, headers=headers)
    if response.status_code == 200:
        json_object = json.loads(response.text)
        return  json_object['data']['access_token']
    else:
        return '接口异常'




