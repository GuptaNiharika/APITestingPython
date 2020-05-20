import requests
import json
import jsonpath
url='https://reqres.in/api/users'
def test_create_new_user():
    file=open('C:\\niharika\\broadcom project\\API Test learn\\createUser.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    response=requests.post(url,request_json)
    assert response.status_code==201  #correct response code
    response_json=json.loads(response.text)
    id=jsonpath.jsonpath(response_json,"id")
    print("New User ID: ",id[0])

def test_create_other_user():
    file=open('C:\\niharika\\broadcom project\\API Test learn\\createUser.json','r')
    json_input=file.read()
    request_json=json.loads(json_input)
    response=requests.post(url,request_json)
    assert response.status_code==202  #wrong response code
    response_json=json.loads(response.text)
    id=jsonpath.jsonpath(response_json,"id")
    print(id[0])
