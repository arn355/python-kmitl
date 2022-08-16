class TorKham:
	def __init__(self):
		self.words = []
		self.playing = True

	def restart(self):
		 ### Enter Your Code Here ###
		self.words = []
		print("game restarted")
		# return "game restarted"

	def play(self, word):
		### Enter Your Code Here ###
		word_play = word.split()
		if word_play[0] is 'P':
			if len(self.words) == 0:
				self.words.append(word_play[1])
				print(f'\'{word_play[1]}\' -> {self.words}')
				# print(self.words)
			else:
				# print("words =", self.words)
				if self.words[-1][-2:].lower() == word_play[1][:2].lower():
					self.words.append(word_play[1])
					print(f'\'{word_play[1]}\' -> {self.words}')
				else:
					print(f'\'{word_play[1]}\' -> game over')
					self.playing = False
		elif word_play[0] is 'R':
			self.restart()
		elif word_play[0] is 'X':
			self.playing = False
		else:
			print(f'\'{word_play[0]} {word_play[1]}\' is Invalid Input !!!')
			self.playing = False
		# return "game over"

torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')
 ### Enter Your Code Here ###
# print(S)
while torkham.playing:
	if len(S) > 0:
		word = S.pop(0)
		torkham.play(word)
		# print(torkham.words)
	# torkham.play(S)
