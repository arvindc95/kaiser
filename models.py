from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), index=True, unique=True)
	password = db.Column(db.String(60), index=False, unique=False)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)
		except:
			return str(self.id)

	def __repr__(self):
		return '<User %r>' % (self.name)
