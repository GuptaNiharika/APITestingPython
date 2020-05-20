import requests
import json
import jsonpath

url='https://reqres.in/api/users?page=2'
response=requests.get(url)
print("Response \n",response)
print("---")
print("Response Content \n",response.content)
print("---")
print("Response Headers \n",response.headers)
print("---")
json_response= json.loads(response.text)  #converting string to json format
print("Response : JSON format \n",json_response)
print("---")
pages= jsonpath.jsonpath(json_response,'total_pages')
print("Total pages : ",pages[0])
email= jsonpath.jsonpath(json_response,'data[0].email')
print("Email : ",email[0])
fname=jsonpath.jsonpath(json_response,'data[0].first_name')
print("fisrtname : ",fname[0])
assert email[0]=='michael.lawson@reqres.in'