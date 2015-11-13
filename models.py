from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True, index = True)
	education = db.Column(db.String(64))
	answers = db.relationship('Answer', backref = 'user')


	def __init__(self, name, education):
		self.name = name
		self.education = education

	def __repr__(self):
		return '<User {0}>'.format(self.user_id)



class Answer(db.Model):
	__tablename__ = 'answers'

	answers_id = db.Column(db.Integer, primary_key = True)
	blog_post = db.Column(db.Text)
	temperature = db.Column(db.Float)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	

	def __init__(self, blog_post, temperature, user_id):
		self.blog_post = blog_post
		self.temperature = temperature
		self.user_id = user_id	
		





