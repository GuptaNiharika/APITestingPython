import requests
import json
import jsonpath
url='https://reqres.in/api/users/2'
file=open('C:\\niharika\\broadcom project\\API Test learn\\createUser.json','r')
json_input=file.read()
request_json=json.loads(json_input)
print("Request - Update User\n",request_json)
print("---")
response=requests.put(url,request_json)
print("Response Content\n",response.content)
print("---")
assert response.status_code ==200

response_json=json.loads(response.text)
updated=jsonpath.jsonpath(response_json,"updatedAt")
print("Response: Updated At : ",updated[0])
