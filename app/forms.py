from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):    
	name = StringField('Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	subject = StringField('Subject', validators=[DataRequired()])
	message = TextAreaField('Message', validators=[DataRequired()])