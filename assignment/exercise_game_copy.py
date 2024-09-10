import network # Only possible when installing the Pi Pico W version of MicroPython
import time
import urequests
import json

# CONNECT TO WIFI
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    if not wlan.isconnected():
        print('Attempting to connect')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
            
    print('Connected!')
    
connect_to_wifi('iPhone (3889)', 'password')

# POST TO DATABASE
def send_data_to_firebase(data):
    url = 'https://ec463-miniproject-38c6e-default-rtdb.firebaseio.com/.json'
    headers = {'Content-Type': 'application/json'}

    try:
        response = urequests.post(url, data=json.dumps(data), headers=headers)
        print('Response:', response.text)
        response.close()
    except Exception as e:
        print('Error:', e)

# GAME CODE
from machine import Pin
import time
import random
import json

N: int = 10
sample_ms = 10.0
on_ms = 500

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:

    with open(json_filename, "w") as f:
        json.dump(data, f)

def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # DICTIONARY WITH MIN, MAX, AVG, AND COUNT
    data = {}
    min_value = min(value for value in t if value is not None)
    max_value = max(value for value in t if value is not None)
    avg_value = sum(value for value in t if value is not None)/N
    score = (N-misses)/N
    
    data['min'] = min_value
    data['max'] = max_value
    data['avg'] = avg_value
    data['score'] = score
    

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)

    # WHEN GAME IS COMPLETE, POST TO DATABASE
    send_data_to_firebase(data)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files

    # CHANGED TO PIN 15 FOR EASE OF USE -- 'LED' PIN DID NOTHING
    led = Pin(15, Pin.OUT)
    button = Pin(14, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    scorer(t)



