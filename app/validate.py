from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm, Form
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User



class RegistrationForm(Form):
    username = StringField('USERNAME', validators = [
        Length(min=4, max=25), 
    	DataRequired() 
	])
    email = StringField('EMAIL', validators = [
        Length(min=6, max=35), 
        Email()
    ])
    password = PasswordField('PASSWORD', validators = [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('CONFIRM PASSWORD')
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Register')



    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):	
	username = StringField('USERNAME', validators=[DataRequired()])
	password = PasswordField('PASSWORD', validators=[DataRequired()])






