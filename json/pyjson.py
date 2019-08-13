import json

def jsonFileToDict(filename):
	"""Import a .json file into a Python dictionary
	   INPUT: filename.json file
		Output: dict containing file contents
	   """

	with open(filename, 'r') as f:
		jsondata = json.load(f)
		dictdata = dict(jsondata)
		return dictdata	

	
def jsonLoad(filename):
	"""	Import a .json file into a Python dictionary
	   	INPUT: filename.json file
		OUTPUT: json object
	   """

	with open(filename, 'r') as f:
		return json.load(f) 

def jsonSave(data, filename):
	"""Save a dict datatype to a .json file
		INPUT: 	data : <dict>
				filename : <string>
		OUTPUT: file.json : a JSON formatted file
	"""
	with open(filename, 'w') as f:
		jsonstr = json.dumps(data)
		json.dump(data, f)
		print('Success: Data saved to JSON file: ', filename)

if __name__ == '__main__':

	# save a python dict as a .json file	
	newdata = {'username':'bob', 'password':'badpassword'}
	jsonSave(newdata,'data.json')

	# import the .json file into a dict type
	filename = 'data.json'
	dictdata = jsonFileToDict(filename)
	print('File import successful.')
	print('The keys to the python dict are: ', dictdata.keys())	

	# import the .json file into a json type
	jsondata = jsonLoad(filename)
	print('The imported JSON Object is:', jsondata)


