import requests
import json
"""
>>> r = requests.get('http://httpbin.org/get')
>>> r = requests.post('http://httpbin.org/post')
>>> r = requests.put('http://httpbin.org/put')
>>> r = requests.delete('http://httpbin.org/delete')
"""
"""
#r = requests.post('http://api.walkovr.com/users/login/', data={"username":"sinan","password":"asd123"})
r = requests.post('http://api.walkovr.com/users/forget-password/', data={"email":"koksalkapucuoglu@hotmail.com"})
print(r.status_code)
print(r.json())
"""

"""
r1 = requests.get("http://httpbin.org/redirect/1",allow_redirects=True)
print(r1.status_code)

r2 = requests.post("http://httpbin.org/post", data={"username":"sinan","password":"asd123"})
print(r2.status_code)
print(r2.json())
"""


"""
endpoint = "http://httpbin.org/post"
myData =   {"id": 1, 
"name": "Leanne Graham", 
"username": "Bret", "email": 
"Sincere@april.biz","address": 
{  "street": "Kulas Light","suite": "Apt. 556",
   "city": "Gwenborough",
   "zipcode": "92998-3874",
   "geo": 
    {
    "lat": "-37.3159",
    "lng": "81.1496"
    }
},
"phone": "1-770-736-8031 x56442",
"website": "hildegard.org",
"company": 
{
  "name": "Romaguera-Crona",
   "catchPhrase": "Multi-layered client-server neural-net",
   "bs": "harness real-time e-markets"
} 
}
r3 = requests.post(endpoint, data=json.dumps(myData))
print(r3.status_code)
r4 = requests.post("http://httpbin.org/post",headers={"User-Agent":"Sinan-Chrome"})
print(r4.status_code)
"""


"""
response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())

#working jsondata
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

#with querry param
parameters = {
    "lat": 40.71,
    "lon": -74
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())
"""
