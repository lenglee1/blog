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
	
	# newUser = User(name = entry.name.data, education = entry.education.data)

	if request.method == 'POST':
		existing_user = User.query.filter_by(name=entry.name.data).first()
		if existing_user:
			newAnswer = Answer(blog_post = entry.blog_post.data, temperature = entry.temperature.data, user_id = existing_user.user_id)
			db.session.add(newAnswer)
			db.session.commit()

			return redirect(url_for('show'))

		else:
			newUser = User(name = entry.name.data, education = entry.education.data)
			db.session.add(newUser)	
			db.session.commit()
			newAnswer = Answer(blog_post = entry.blog_post.data, temperature = entry.temperature.data, user_id = newUser.user_id)
			db.session.add(newAnswer)
			db.session.commit()

			return redirect(url_for('show'))

	elif request.method == 'GET':
		return render_template('index.html', form = entry)


@app.route('/show')
def show():
	all_users_answers = User.query.join(Answer, User.user_id == Answer.user_id).add_columns(User.name, User.education, Answer.blog_post, Answer.temperature).order_by(Answer.answers_id).all()


	
	return render_template('show.html', object = all_users_answers)


@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return "it works. i dont believe it!"
	else:
		return "shit not working. fuck fuck fuck."




if __name__ == '__main__':
	app.run(debug = True)

