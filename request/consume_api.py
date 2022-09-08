# Stackoverflow API
import requests


import requests
import json

response = requests.get(
    'https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

# print(response.json()['items'])
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print('--need to be answered--')
        print(data['title'])
        print(data['link'])
        print()
    else:
        print('--answered--')
        print(data['title'])
        print(data['link'])
    print()
