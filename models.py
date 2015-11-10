from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
	__tablename__ = 'users'

	users_id = db.Column(db.Integer, primary_key = True, index = True)
	name = db.Column(db.String(64), unique = True)
	education = db.Column(db.String(64))
	country = db.Column(db.String(64))
	answers = db.relationship('Answer', backref = 'user')

	def __repr__(self):
		return '<User {0}>'.format(self.users_id)

class Answer(db.Model):
	__tablename__ = 'answers'

	answers_id = db.Column(db.Integer, primary_key = True)
	blog_post = db.Column(db.Text)
	temperature = db.Column(db.Float)
	fruits = db.Column(db.String(64))
	blog_date = db.Column(db.Date)
	user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'))



