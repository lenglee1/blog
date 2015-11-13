from flask import Flask, render_template, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect
from forms import Entry
from models import db, User, Answer

app = Flask(__name__)
bootstrap = Bootstrap(app)
db.init_app(app)
csrf = CsrfProtect(app)


app.config['SECRET_KEY'] = "string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dog@localhost/blog'


@app.route('/', methods = ['GET', 'POST'])
def index():
	entry = Entry()
	dbObject = User.query.filter_by(name=entry.name.data).first()
	newUser = User(name = entry.name.data, education = entry.education.data)

	if request.method == 'POST':
		if dbObject.name == entry.name.data:
			newAnswer = Answer(blog_post = entry.blog_post.data, temperature = entry.temperature.data, user_id = dbObject.user_id)
			db.session.add(newAnswer)
			db.session.commit()

			return render_template('blog.html')

		else:
			
			db.session.add(newUser)	
			db.session.commit()
			newAnswer = Answer(blog_post = entry.blog_post.data, temperature = entry.temperature.data, user_id = newUser.user_id)
			db.session.add(newAnswer)
			db.session.commit()

			return render_template('blog.html')

	elif request.method == 'GET':
		return render_template('index.html', form = entry)

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return "it works. i dont believe it!"
	else:
		return "shit not working. fuck fuck fuck."




if __name__ == '__main__':
	app.run(debug = True)

