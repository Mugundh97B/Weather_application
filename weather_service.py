from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# pseudo api key is given here, need to update a new api key
API_KEY = "9111b144ff05aa1sedcb18ccdc5e99282c8"
BASE_URL = "http://api.weatherstack.com/current"

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    try:
        # Fetch weather data from Weatherstack API
        params = {
            "access_key": API_KEY,
            "query": city
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
   
        if "error" in data:
            return jsonify({"error": data["error"]["info"]}), 400  
        current_data = data["current"]
        weather_data = {
            "city": data["location"]["name"],
            "temperature": current_data["temperature"],
            "description": current_data["weather_descriptions"][0],
            "humidity": current_data["humidity"],
            "wind_speed": current_data["wind_speed"]
        }
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
