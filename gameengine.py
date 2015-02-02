class KaiserServer:
	def __init__(self):
		self.games = []


class KaiserGame:
	def __init__(self, gid):
		self.gameid = gid
		self.players = []
		self.t1score = 0
		self.t2score = 0
		self.dealer = 0
		self.turn = 0
