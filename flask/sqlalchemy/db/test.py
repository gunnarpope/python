from db_example import db, User

me = User()
me.username = 'admin'
me.email = 'admin@example.com'
db.session.add(me)
db.session.commit()
