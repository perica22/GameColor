from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired




class User():
    user = {'name': 'asdasd', 'email': 'perica@rechargeapps.com', 'password': 'perica22'}


class RegistrationForm(Form):
    username = StringField('USERNAME', [validators.Length(min=4, max=25), 
    	validators.DataRequired()
	])
    email = StringField('EMAIL', [validators.Length(min=6, max=35)])
    password = PasswordField('PASSWORD', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('CONFIRM PASSWORD')
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class LoginForm(FlaskForm):	
	username = StringField('USERNAME', validators=[DataRequired()])
	password = PasswordField('PASSWORD', validators=[DataRequired()])




	

