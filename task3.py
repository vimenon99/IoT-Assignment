from flask import Flask, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Replace these with your ThingSpeak channel details
CHANNEL_ID = "2894178"
API_KEY = "Z2P9QNAZYR5YZRKR"

# Calculate the start and end time for the last 5 hours
def get_time_range():
    end_time = datetime.utcnow()  # Current time (UTC)
    start_time = end_time - timedelta(hours=5)  # 5 hours ago
    
    # Convert times to ISO 8601 format
    end_time_str = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    return start_time_str, end_time_str

# URL for ThingSpeak API to fetch data from the last 5 hours
def get_thingspeak_data():
    start_time, end_time = get_time_range()
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
    params = {
        "api_key": API_KEY,
        "start": start_time,
        "end": end_time
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/historical_data')
def get_historical_data():
    data = get_thingspeak_data()
    
    if data:
        feeds = data.get('feeds', [])
        if not feeds:
            return jsonify({'error': 'No data available for the last 5 hours'}), 404
        
        # Extract and format the data for display
        result = []
        for feed in feeds:
            result.append({
                'timestamp': feed['created_at'],
                'temperature': feed['field1'],
                'humidity': feed['field2'],
                'co2': feed['field3']
            })
        
        return jsonify(result)
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sensor Data</title>
    <script>
        function fetchData() {
            fetch('/historical_data')  // Fetch historical data
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('error').textContent = data.error;
                    } else {
                        let dataHtml = '<h2>Sensor Data from the Last 5 Hours</h2><ul>';
                        data.forEach(item => {
                            dataHtml += `<li>Time: ${item.timestamp}, Temperature: ${item.temperature}°C, Humidity: ${item.humidity}%, CO2: ${item.co2}ppm</li>`;
                        });
                        dataHtml += '</ul>';
                        document.getElementById('sensorData').innerHTML = dataHtml;
                    }
                })
                .catch(error => {
                    document.getElementById('error').textContent = 'Error fetching data: ' + error;
                });
        }
        window.onload = fetchData;  // Call fetchData when page loads
    </script>
</head>
<body>
    <h1>Latest Sensor Data</h1>
    <div id="sensorData">Loading...</div>
    <div id="error"></div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)
