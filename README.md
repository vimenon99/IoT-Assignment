Here is the `README.md` file including details about your three scripts:  

---

```md
# IoT Environmental Sensor Data System  

## Project Overview  
This project is an IoT-based system that collects, processes, and displays environmental sensor data from **ThingSpeak**. It consists of three main components:  

1. **api.py** - Simulates and sends random sensor data to ThingSpeak.  
2. **iot.py** - Fetches the latest sensor data and integrates it into a Flask web application.  
3. **task3.py** - Retrieves the sensor data recorded in the last 5 hours from ThingSpeak and displays it on the web application.  

---

## Features  
✔️ Simulates real-time environmental sensor data  
✔️ Sends data to ThingSpeak API at regular intervals  
✔️ Fetches and displays the latest sensor data dynamically using Flask  
✔️ Retrieves data from the past 5 hours and presents it in a user-friendly format  
✔️ HTML, CSS, and JavaScript are integrated directly within the Python application  

---

## Installation and Setup  

### **1. Clone the Repository**  
```sh
git clone https://github.com/yourusername/IoT-Environmental-Sensor.git
cd IoT-Environmental-Sensor
```

### **2. Create a Virtual Environment**  
```sh
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### **3. Install Dependencies**  
```sh
pip install flask, requests,  paho-mqqt
```

### **4. Set Up ThingSpeak API Key**  
- Create a ThingSpeak channel and obtain the **API Key**.
- Update **api.py**, **iot.py**, and **task3.py** with your **ThingSpeak API Keys**.

### **5. Run the Sensor Data Simulation**  
```sh
python api.py
```

### **6. Start the Flask Web Application (Latest Data Retrieval)**  
```sh
python iot.py
```
- Open your browser and visit: `http://127.0.0.1:5000/`

### **7. Retrieve and Display the Last 5 Hours of Sensor Data**  
```sh
python task3.py
```
- This will fetch data from the past 5 hours and integrate it into the Flask web application.

---

## File Structure  
```
IoT-Environmental-Sensor/
│── api.py               # Sends random sensor data to ThingSpeak
│── iot.py               # Flask app displaying latest data
│── task3.py             # Retrieves last 5 hours of data
│── templates/           
│   ├── index.html       # Web interface to display data
│── static/              
│   ├── style.css        # Styling for the webpage
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
```

---

## Technologies Used  
🔹 Python (Flask)  
🔹 ThingSpeak API  
🔹 HTML, CSS, JavaScript (Integrated into Python)  
🔹 Virtual Environment (venv)  

