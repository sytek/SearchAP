from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address"), Email("Please enter your email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password"), Length(min=6, message="Password must be a minimum of 6 characters")])
    submit = SubmitField('')

class LoginForm(Form):
    email = StringField('Email Address', validators=[DataRequired("Please enter your email to login"), Email("Please enter your email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password")])
    submit = SubmitField('Sign in')

class AddressForm(Form):
    address = StringField('Address', validators=[DataRequired("Enter address to search...")])
    submit = SubmitField("Search")
