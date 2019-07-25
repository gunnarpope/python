import json

def json2dict(filename):
	"""Import a .json file into a Python dictionary"""

	with open(filename, 'r') as f:
		jsondata = json.load(f)
		dictdata = dict(json.loads(jsondata))
		return dictdata	
	

if __name__ == '__main__':
	
	filename = 'voting_organization.json'
	dictdata = json2dict(filename)
	print(dictdata.keys())	
