# curl -i http://127.0.0.1:5000/v1/user/2 -X GET


import requests 
import json

API_BASE ="http://127.0.0.1:5000" 
API_VERSION="/v1"

def set_userdata(userid, data):
	
	# data = {'username': 'sue', 'password': 'password1234'}
	apiurl = API_BASE + API_VERSION + '/user' + '/' +  str(userid)
	r = requests.post(url=apiurl, data=data)
	if (r.status_code == requests.codes.ok):
		return r.text
	else:
		return { 'Error Code: ', r.status_code}

def get_userdata(userid):	
	apiurl = API_BASE + API_VERSION + '/user' + '/' +  str(userid)
	headers = {'content-type': 'application/json', 'accept': 'application/json'}
	r = requests.get(url= apiurl)
	if (r.status_code == requests.codes.ok):
		return r.text
	else:
		print('Error Code: ', r.status_code)

if __name__ == '__main__':

	print( get_userdata(1))
	print( set_userdata(3, {'username':'mark','password':'password1234'}))
	print( get_userdata(3))
# 
# 	# api-endpoint 
# 	URL = "http://127.0.0.1:5000/v1/user/"
# 	 
# 	usernumber = 1
# 	
# 	apiurl = URL + str(usernumber)
# 	r = requests.get(url= apiurl)
# 	 
# 	print(r.text)
# 	# defining a params dict for the parameters to be sent to the API 
# 	data = {'username': 'sue', 'password': 'password1234'}
# 	apiurl = URL + str(3)
# 	r = requests.post(url=apiurl, data=data)
# 	print(r.text)
# 	print(r.status_code)
# 	
# 	
# 	headers = {'content-type': 'application/json', 'accept': 'application/json'}
# 	
# 	apiurl = URL + str(3)
# 	
# 	r = requests.get(url=apiurl, headers=headers)
# 	print(r.text)
# 	print(r.headers)
# 	
# 	
