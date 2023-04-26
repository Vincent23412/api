import requests
import json

url = 'http://localhost:5000/get_weather_and_suggestion'
params = {'city': 'Taipei', 'keyword': 'python'}
response = requests.get(url, params=params)
result = json.loads(response.text)
print(result)