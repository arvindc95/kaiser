from app import db, bc
from models import User

def try_login(user, password):
	query = User.query.filter_by(name=user).first()
	
	try:
		if bc.check_password_hash(query.password, password):
			return query
		else:
			return None
	except AttributeError:
		return None

