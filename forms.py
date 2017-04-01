from flask_wtf import Form  
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length 

'''

uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)
  pwdhash = db.Column(db.String(54))
  address = db.Column(db.String(500))
  zipcode = db.Column(db.String(500))
  volunteergroup = db.Column(db.String(100))

  '''
class SignupForm(Form):
	first_name = StringField('First name', validators = [DataRequired('Please enter your first name.')])
	last_name  = StringField('Last name', validators = [DataRequired('Please enter your last name')])
	email = StringField('Email', render_kw = {"placeholder": "xyz@example.com"}, validators = [DataRequired('Please enter your email address.'), Email('Please enter a valid email address.')])
	password = PasswordField('Password', validators = [DataRequired('Please enter your password.'), Length(min=6, message = 'Password must be 6 characters or more')])
	address = StringField('Address', validators = [DataRequired('Please enter your address')])
	zipcode = StringField('Zipcode', validators = [DataRequired('Please enter your zipcode')])
	volunteergroup = StringField('Volunteer Group  (Optional)', render_kw = {'placeholder': "First year medical students"})
	submit = SubmitField('Sign up')




class LoginForm(Form):
	email = StringField('Email', render_kw = {"placeholder": "xyz@example.com"}, validators = [DataRequired('Please enter your email address.'), Email('Please enter a valid email address.')])
	password = PasswordField('Password', validators = [DataRequired('Please enter your password.')])
	submit = SubmitField('Sign in')