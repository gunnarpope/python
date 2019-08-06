

from flask import Flask, request
import requests 

app = Flask(__name__)


# importing the requests library 
  
# api-endpoint 
URL = "http://127.0.0.1/"
  
# location given here 
todo = "finish this tutorial"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'data':todo} 
  
 
# # extracting latitude, longitude and formatted address  
# # of the first matching location 
# latitude = data['results'][0]['geometry']['location']['lat'] 
# longitude = data['results'][0]['geometry']['location']['lng'] 
# formatted_address = data['results'][0]['formatted_address'] 
#   
# # printing the output 
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#       %(latitude, longitude,formatted_address)) 


@app.route('/')
def init():
	# sending get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS) 
  
	# extracting data in json format 
	data = r.json() 

	return 'hello!' # jsonify(data)  
 
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.0')


