from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, RadioField, TextAreaField, FileField, DateField, DecimalField

fruit_choices = [(1, "Pear"), (2, "Nashi"), (3, "Orange"), (4, "Nectarine"), (5, "Berries")]
education_choices = [(1, "High School"), (2, "College"), (3, "Masters"), (4, "Doctorate"), (5, "Other")]
country_choices = [(1, "USA"), (2, "UK"), (3, "Australia"), (4, "Malaysia"), (5, "China")]

class Entry(Form):
	name = StringField("Name")
	education = RadioField("Education: ", choices = education_choices, default = [1])
	country = SelectField("Country of birth: ", choices = country_choices, default = [1])
	
	
	blog_post = TextAreaField("Blog entry: ")	
	temperature = DecimalField("What is the temp?")
	fruits = SelectMultipleField("Which fruits fo you like: ", choices = fruit_choices, default = [1])
	blog_date = DateField("Date")

	submit = SubmitField("Submit")



# loadedFile = FileField("Load file here")