from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, RadioField, TextAreaField, FileField, DateField, DecimalField

education_choices = [(1, "High School"), (2, "College"), (3, "Masters"), (4, "Doctorate"), (5, "Other")]


class Entry(Form):
	name = StringField("Name")
	education = RadioField("Education: ",  choices = education_choices, default = 1)	
	blog_post = TextAreaField("Blog entry: ")	
	temperature = DecimalField("What is the temp?")
	
	submit = SubmitField("Submit")




