# Weather API
# Application Programming Interface
import requests
import json

info = '''
1. Seoul
2. Paris
3. New York
4. Los Angeles
5. San Francisco
'''
print(info)
input_val = int(input('Choose a number you want to check: '))
city_name = 'Los_Angeles'

if input_val == 1:
    city_name = 'Seoul'
elif input_val == 2:
    city_name = 'Paris'
elif input_val == 3:
    city_name = 'new_york'
elif input_val == 4:
    city_name = 'los_angeles'
elif input_val == 5:
    city_name = 'san_francisco'
else:
    print('Choose a number!')

response = requests.get(
    'http://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q=' + city_name + '&aqi=yes')

json_obj = json.loads(response.text)

# print(response.text)
# print(json.dumps(jsonObj, indent=4))
print(json_obj['location']['name'], 'Temperature:', json_obj['current']
      ['temp_f'], 'Condition:', json_obj['current']['condition']['text'])
