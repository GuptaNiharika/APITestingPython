import requests
import json
import jsonpath
url='https://reqres.in/api/users'
file=open('C:\\niharika\\broadcom project\\API Test learn\\createUser.json','r')
json_input=file.read()
request_json=json.loads(json_input)
print("Request - New User - JSON format \n",request_json)
print("---")
response=requests.post(url,request_json)
print("Response Content\n",response.content)
print("---")
assert response.status_code==201
print("Response Header\n",response.headers)
print("---")
print("Response header - Content-Length\n",response.headers.get('Content-Length'))
print("---")
response_json=json.loads(response.text)
id=jsonpath.jsonpath(response_json,"id") #returns a list
print("New User id : ",id[0],"\n")
print("New User details fetched from response\n",response.text)