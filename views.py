from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from forms import Entry
from models import db, User, Answer

app = Flask(__name__)
bootstrap = Bootstrap(app)
db.init_app(app)

app.config['SECRET_KEY'] = "string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dog@localhost/blog'


@app.route('/')
def index():
	entry = Entry()
	return render_template('index.html', form = entry)

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return "it works. i dont believe it!"
	else:
		return "shit not working. fuck fuck fuck."




if __name__ == '__main__':
	app.run(debug = True)

