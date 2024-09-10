Exercise 1:
max_bright value: 45000
min_bright value: 20000
//we tested this in a fairly bright photonics lab room, so to achieve a dim light we considered casting a shadow with our hand over the photocell to qualify,
and the value of 20000 for min_bright corresponded to a 0% duty cycle of the led when shadowing the photocell. 
//the max bright value we found was 45000 and when shining a phone flashlight we were able to achieve around 100% duty cycle with the led.

Exercise 2:

posting code:
import network
import time

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('Network connected:', wlan.ifconfig())
    
# Replace with your Wi-Fi credentials
connect_to_wifi('iPhone (3889)', 'password')

import urequests
import json

def send_data_to_firebase(data):
    url = 'https://ec463-miniproject-38c6e-default-rtdb.firebaseio.com/.json'  # Change 'data' to the path in your DB
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = urequests.post(url, data=json.dumps(data), headers=headers)
        print('Response:', response.text)
        response.close()
    except Exception as e:
        print('Error sending data:', e)

# Example data to send
data = {
    'temperature': 25,
    'humidity': 60
}

# Send data to Firebase
send_data_to_firebase(data)
