from flask import Flask
from flask_sqlalchemy import SQLAlchemy


if __name__ == '__main__':
	
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
	db = SQLAlchemy(app)

	class User(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		username = db.Column(db.String(80), unique=True, nullable=False)
		email = db.Column(db.String(120), unique=True, nullable=False)

		def __repr__(self):
			return '<User %r>' % self.username


	db.create_all()
	admin = User(username='admin', email='guest@example.com')
	guest = User(username='guest', email='guest@example.com')

	db.session.add(admin)
	db.session.add(guest)
	db.session.commit()

	print( User.query.all() )

	print( User.query.filter_by(username='admin').first() )

	
