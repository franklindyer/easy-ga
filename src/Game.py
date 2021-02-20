class Game:

	def __init__(self):
		self.settings = {}

	def configure(self, settings):
		for key in settings:
			self.settings[key] = settings[key]

class TrivialGame(Game):

        def __init__(self):

            super().__init__()

        def play(self, genome):

            score = 0
            for i in range(genome.length):
                if genome.get(i) == 0:
                    score += 1

            return score

class DotProdGame(Game):

        def __init__(self, length=30, target=0):

            super().__init__()

            self.vector = None
            self.length = length
            self.target = target

        def random_vector(self, length):

            self.vector = [random.randint(1, length)*random.choice([-1, 1]) for i in range(length)]

        def setup(self):

            self.random_vector(self.length)

        def play(self, genome):

            self.setup()

            gvec = np.asarray(genome.sequence)
            vvec = np.asarray(self.vector)
            
            dot = np.dot(gvec, vvec)
            score = 1 / (1 + abs(self.target - dot))

            return score

class SodaCanGame(Game):

	def __init__(self):
		
		super().__init__()
		
		self.configure({
			"rows": 10,
			"cols": 10,
			"can_prob": 0.5,
			"start_pos": [0, 0],
			"duration": 100
		})
		self.board = [[0]]
		self.rows = 0
		self.cols = 0
		self.max_score = 0
		self.position = [0, 0]
		self.score = 0
		self.moves_remaining = 0

	def random_board(self, rows, cols, can_prob):

		board = [[0 for j in range(cols)] for i in range(rows)]
		max_score = 0
		for i in range(rows):
			for j in range(cols):
				if random.random() < can_prob:
					board[i][j] = 1
					max_score += 1

		self.rows = rows
		self.cols = cols
		self.max_score = max_score
		self.board = board

	def setup(self):

		self.score = 0
		self.moves_remaining = self.settings["duration"]

		rows = self.settings["rows"]
		cols = self.settings["cols"]
		can_prob = self.settings["can_prob"]
		self.position = self.settings["start_pos"]
		self.random_board(rows, cols, can_prob)
	
	## There are 2^8 = 256 possible values, since
	## the player can only see 8 adjacent spaces
	## and each space has 2 possible states.
	def encode_state(self):

		x = self.position[0]
		y = self.position[1]
		r = self.rows
		c = self.cols

		## order: nw, n, ne, w, e, sw, s, se
		adj_spaces = [
			self.board[(y-1)%r][(x-1)%c],
			self.board[(y-1)%r][x],
			self.board[(y-1)%r][(x+1)%c],
			self.board[y][(x-1)%c],
			self.board[y][(x+1)%c],
			self.board[(y+1)%r][(x-1)%c],
			self.board[(y+1)%r][x%c],
			self.board[(y+1)%r][(x+1)%c]
		]
		coded_state = sum([adj_spaces[i] * 2**i for i in range(8)])

		return coded_state

	## There are 4 possible moves, since
	## the player can move north, south, east, or west.
	def decode_move(self, code):

		r = self.rows
		c = self.cols

		if code == 0:
			self.position[1] += -1
		elif code == 1:
			self.position[1] += 1
		elif code == 2:
			self.position[0] += 1
		elif code == 3:
			self.position[0] += -1
		self.position[0] = self.position[0] % c
		self.position[1] = self.position[1] % r

		self.score += self.board[self.position[1]][self.position[0]]
		self.board[self.position[1]][self.position[0]] = 0

	def play(self, genome):

		self.setup()

		while self.moves_remaining > 0:
			state_code = self.encode_state()
			move_code = genome.get(state_code)
			self.decode_move(move_code)
			self.moves_remaining += -1

		return self.score / self.max_score
