from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL to ThingSpeak API endpoint
url = "https://api.thingspeak.com/channels/2894178/feeds.json"

@app.route('/data')
def get_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latest_data = data['feeds'][-1]  # Get the latest feed
        return jsonify({
            'temperature': latest_data['field1'],
            'humidity': latest_data['field2'],
            'co2': latest_data['field3']
        })
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500


@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Sensor Data</title>
    <script>
        // Function to fetch and update data every 10 seconds
        function fetchData() {
            fetch('/data')  // Fetch latest data from Flask API
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('error').textContent = data.error;
                    } else {
                        document.getElementById('temperature').textContent = 'Temperature: ' + data.temperature + '°C';
                        document.getElementById('humidity').textContent = 'Humidity: ' + data.humidity + '%';
                        document.getElementById('co2').textContent = 'CO2 Level: ' + data.co2 + ' ppm';
                    }
                })
                .catch(error => {
                    document.getElementById('error').textContent = 'Error fetching data: ' + error;
                });
        }

        // Call fetchData every 10 seconds
        setInterval(fetchData, 10000);

        // Call fetchData once to load data immediately when the page loads
        window.onload = fetchData;
    </script>
</head>
<body>
    <h1>Latest Sensor Data</h1>
    <p id="temperature">Loading...</p>
    <p id="humidity">Loading...</p>
    <p id="co2">Loading...</p>
    <p id="error"></p>
</body>
</html>'''
  
if __name__ == '__main__':
    app.run(debug=True)
