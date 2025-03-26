import random
import time
import requests
import json

# ThingSpeak channel details
API_KEY = 'Z2P9QNAZYR5YZRKR'
URL = f'https://api.thingspeak.com/update?api_key=Z2P9QNAZYR5YZRKR'

# Function to simulate sensor data
def generate_sensor_data():
    temperature = random.uniform(-50, 50)
    humidity = random.uniform(0, 100)
    co2 = random.randint(300, 2000)
    return temperature, humidity, co2

# Publish data periodically
while True:
    temperature, humidity, co2 = generate_sensor_data()
    payload = {
        'field1': temperature,
        'field2': humidity,
        'field3': co2
    }
    response = requests.get(URL, params=payload)
    print(f"Published data: {payload}")
    time.sleep(10)  # Send data every 10 seconds
