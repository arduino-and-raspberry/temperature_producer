
import requests
import json
import time

# your temperature
usertemp = 14
TIME_OUT = 60
ADD_TEMP_URL = "http://84.47.161.121:8080/rest/users/add"
ADD_LOG_URL = "http://84.47.161.121:8080/rest/users/addlog"

payload = {'temp': usertemp}
logPayload = {'who': None, 'lastTemperature': -5, 'lastHumidity': 48, 'serverTime': None, 'lastContactTime': None, 'current': 151, 'amperage': 155, 'power': 180, 'consuming': 1024, 'lastContactDate': None, 'acOn': True, 'lanOn': True}
json_data = json.dumps(payload)
json_data2 = json.dumps(logPayload)


while 1:
    r = requests.post(ADD_TEMP_URL, data=json_data)
    print(r.text)
    time.sleep(10)

    r = requests.post(ADD_LOG_URL, data=json_data2)
    print(r.text)
    time.sleep(TIME_OUT)
