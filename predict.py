import numpy as np
import pandas as pd
import requests
import json
import time
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load dataset for scaler fitting
file_path = 'water_quality_sensor_data.csv'
data = pd.read_csv(file_path)
scaler = StandardScaler()
scaler.fit(data[['pH', 'Turbidity', 'TDS']])

# Load models
voltage_model = load_model('voltage_model_weights.h5')
current_model = load_model('current_model_weights.h5')

fetch_url = "https://yourdomain.com/php/fetch_sensor_data.php"
post_url = "https://yourdomain.com/php/update_predictions.php"

while True:
    try:
        response = requests.get(fetch_url)
        if response.status_code == 200:
            sensor_data = response.json()

            if all(key in sensor_data for key in ['pH', 'Turbidity', 'TDS']):
                sample = scaler.transform([[sensor_data['pH'], sensor_data['Turbidity'], sensor_data['TDS']]])
                voltage = voltage_model.predict(sample)[0][0]
                current = current_model.predict(sample)[0][0]

                payload = {"voltage": voltage, "current": current}
                headers = {'Content-Type': 'application/json'}
                post_response = requests.post(post_url, json=payload, headers=headers)
                print(post_response.text)
            else:
                print("Error: Missing sensor values")
        else:
            print("Error fetching sensor data")

    except Exception as e:
        print(f"Request error: {e}")

    time.sleep(5)
