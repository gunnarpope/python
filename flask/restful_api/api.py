

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = {'username': 'alice', 'password': 'password1234'}
data2 = {'username': 'bob', 'password': 'password1234'}
users = {'id': {
			1: data,
			2: data2}}

class TodoSimple(Resource):
	def get(self, user_id):
		return {user_id: users['id'][user_id]}

	def post(self, user_id):
		print('hello')
		print(request.form)
		users['id'][user_id] = request.form
		return {user_id: users['id'][user_id]}

api.add_resource(TodoSimple, '/v1/user/<int:user_id>')

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')


