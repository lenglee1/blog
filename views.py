from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from forms import Entry

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "string"

@app.route('/')
def index():
	entry = Entry()
	return render_template('index.html', form = entry)




if __name__ == '__main__':
	app.run(debug = True)

