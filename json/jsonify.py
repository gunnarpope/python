"""jsonify.py
	Input: dictionary of data
	Output: data in JSON format
"""

import json

def jsonify( data ):
	return json.dumps(data, sort_keys=True, indent=4)

if __name__ == '__main__':
	data = {'Name': 'Fido', 'Age': 2, 'List': [1,2,3,4]}
	print (jsonify(data))
