# curl -i http://127.0.0.1:5000/v1/user/2 -X GET


import requests 

# api-endpoint 
URL = "http://127.0.0.1:5000/v1/user/"
 
usernumber = 1

apiurl = URL + str(usernumber)
# sending get request and saving the response as response object 
r = requests.get(url= apiurl)
 
print(r.text)
# defining a params dict for the parameters to be sent to the API 
data = {'username': 'sue', 'password': 'password1234'}
apiurl = URL + str(3)
r = requests.post(url = apiurl, data = data)
print(r.text)
 


