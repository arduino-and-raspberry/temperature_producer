import requests
payload = "{'who':null,'lastTemperature':-5,'lastHumidity':48,'serverTime':null,'lastContactTime':null,'current':151,'amperage':155,'power':180,'consuming':1024,'lastContactDate':null,'acOn':true,'lanOn':true}"
r = requests.post("http://localhost:8080/rest/users/addlog", data=payload)
print(r.text)