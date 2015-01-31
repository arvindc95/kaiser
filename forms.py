from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from models import User

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired(message="All fields are required.")])
	password = PasswordField('password', validators=[DataRequired("All fields are required.")])
	remember_me = BooleanField('remember_me', default=False)

	def validate(self):
		if not Form.validate(self):
			del self.username.errors[:]
			del self.password.errors[:]
			self.username.errors.append("All fields are required.")
			return False

		return True

class SignupForm(Form):
	username = StringField('username', validators=[DataRequired(message="All fields are required.")])
	password = PasswordField('password', validators=[DataRequired(message="All fields are required.")])
	cpassword = PasswordField('cpassword', validators=[DataRequired(message="All fields are required.")])
	remember_me = BooleanField('remember_me', default=False)

	def validate(self):
		if not Form.validate(self):
			del self.username.errors[:]
			del self.password.errors[:]
			del self.cpassword.errors[:]
			self.username.errors.append("All fields are required.")
			return False
		
		if len(self.username.data) > 20:
			self.username.errors.append('Usernames must be 20 characters or less.')
			return False

		user = User.query.filter_by(name=self.username.data).first()
		if user != None:
			self.username.errors.append('Username already taken.')
			return False
				
		if not self.password.data == self.cpassword.data:
			self.password.errors.append('Passwords don\'t match!')
			return False

		return True
