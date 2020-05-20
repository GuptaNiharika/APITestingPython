import requests
url= 'https://reqres.in/api/users/2'
response=requests.delete(url)
print("Response Status Code :",response.status_code)
assert response.status_code==204
