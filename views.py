from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from kaiserapp import app, db, lm, bc
from forms import LoginForm, SignupForm
from models import User
from db_interact import try_login
import testing

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
						   title='Home',
						   user=g.user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()

	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		user = try_login(form.username.data, form.password.data)
		if user is None:
			flash('Invalid login. Please try again.')
			return redirect(url_for('login'))

		ulogin(user)
		return redirect(url_for('index'))

	return render_template('login.html',
							title='Sign In',
							form=form)

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		user = User(name=form.username.data, 
					password=bc.generate_password_hash(form.password.data))
		db.session.add(user)
		db.session.commit()
		flash('Registration successful!')
		ulogin(user)
		return redirect(url_for('index'))

	return render_template('signup.html',
							title="Sign Up",
							form=form)	

@app.route('/game')
@login_required
def game():
	return render_template('game.html',
							title="Kaiser",
							hand=testing.make_hand())

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	return render_template('500.html'), 500

def ulogin(user):
     if 'remember_me' in session:
         remember_me = session['remember_me']
         session.pop('remember_me', None)
     login_user(user, remember = remember_me)

