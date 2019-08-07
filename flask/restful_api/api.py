
import json
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = {'username': 'alice', 'password': 'password1234'}
data2 = {'username': 'bob', 'password': 'password1234'}
db 	  = {'user': {
			'id':{
				1 : data,
				2 : data2}
				}
		}

# API get format
# GET /version/<resource>/<id>
class get_userid(Resource):
	def get(self, resource, user_id):
		print('resource is: ', resource)
		return {user_id: db[str(resource)]['id'][user_id]}

	def post(self, resource, user_id):
		print('resource is: ', resource)
		db[resource]['id'][user_id] = request.form
		return {user_id: db[resource]['id'][user_id]}


api.add_resource(get_userid, '/v1/<string:resource>/<int:user_id>')


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')


