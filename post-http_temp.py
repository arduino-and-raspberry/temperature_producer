
import requests
import json
import time
import serial

# your temperature

TIME_OUT = 60
ADD_TEMP_URL = "http://84.47.161.121:8080/rest/users/add"
ADD_LOG_URL = "http://84.47.161.121:8080/rest/users/addlog"

ser = serial.Serial("/dev/ttyUSB0", 9600)
serialLine = ser.readline()


logPayload = {'who': None, 'lastTemperature': -5, 'lastHumidity': 48, 'serverTime': None, 'lastContactTime': None, 'current': 151, 'amperage': 155, 'power': 180, 'consuming': 1024, 'lastContactDate': None, 'acOn': True, 'lanOn': True}
json_data2 = json.dumps(logPayload)

while 1:
    print(serialLine)
    decodedLine = serialLine.decode('utf-8', 'backslashreplace')
    if "DHT" not in decodedLine:

        usertemp = int(serialLine.strip('\0'))
        print(usertemp)
        payload = {'temp': usertemp}
        json_data = json.dumps(payload)
        r = requests.post(ADD_TEMP_URL, data=json_data)
        print(r.text)
        time.sleep(10)

        r = requests.post(ADD_LOG_URL, data=json_data2)
        print(r.text)
        time.sleep(TIME_OUT)
