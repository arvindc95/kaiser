from time import sleep
import uuid

MAX_GAMES = 10

class KaiserServer:
	def __init__(self):
		self.games = []
	
	def create_game(self):
		self.games.append(

class KaiserGame:
	def __init__(self, game_name):
		self.gameid = uuid.uuid1()
		self.name = game_name

