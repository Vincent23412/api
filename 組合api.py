from flask import Flask, request
import requests
import json

app = Flask(__name__)

# 第一个 API：获取天气信息
@app.route('/get_weather')
def get_weather():
    city = request.args.get('city', 'Taipei')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    return response.text

# 第二个 API：获取单词建议
@app.route('/get_suggestion')
def get_suggestion():
    keyword = request.args.get('keyword', '')
    url = f'http://api.datamuse.com/words?rel_syn={keyword}'
    response = requests.get(url)
    return response.text

# 新的 API：组合现有 API
@app.route('/get_weather_and_suggestion')
def get_weather_and_suggestion():
    city = request.args.get('city', 'Taipei')
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    weather_response = requests.get(weather_url)
    weather_data = json.loads(weather_response.text)
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

    keyword = request.args.get('keyword', '')
    suggestion_url = f'http://api.datamuse.com/words?rel_syn={keyword}'
    suggestion_response = requests.get(suggestion_url)
    suggestion_data = json.loads(suggestion_response.text)
    suggestion_words = [suggestion['word'] for suggestion in suggestion_data]

    result = {
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'suggestion_words': suggestion_words
    }

    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
