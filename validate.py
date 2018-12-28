from wtforms import Form, BooleanField, StringField, PasswordField, validators


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