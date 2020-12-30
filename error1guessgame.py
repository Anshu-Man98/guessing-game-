import random

def rand():
	r=random.randint(1, 10)
	return r



def data():
	while True:
		player=int(input("enter a number between 1 - 10 :") )
		if player in range(0,10):
			break
		else:
			print("PLEASE enter a number between 1 - 10")
			continue

	return player




		
computer=rand()


while True:

	while True:

		player=data()
		print(player)
		if player == computer:
			print( "you guessed right!!!!!!")
			break
		if computer-player == abs(1) or player - computer == abs(1):
			print ("you guessed wrong you are one steps away Try again")
			continue
		if computer-player == abs(2) or player - computer == abs(2):
			print ("you guessed wrong you are two steps away Try again")
			continue
		if computer-player == abs(3) or player - computer == abs(3):
			print ("you guessed wrong you are three steps away Try again")
			continue
		if computer-player == abs(4) or player - computer == abs(4):
			print ("you guessed wrong you are four steps away Try again")
			continue
		if computer-player == abs(5) or player - computer == abs(5):
			print ("you guessed wrong you are five steps away Try again")
			continue
		if computer-player == abs(6) or player - computer == abs(6):
			print ("you guessed wrong you are six steps away Try again")
			continue
		if computer-player == abs(7) or player - computer == abs(7):
			print ("you guessed wrong you are seven steps away Try again")
			continue
		if computer-player == abs(8) or player - computer == abs(8):
			print ("you guessed wrong you are eight steps away Try again")
			continue
		if computer-player == abs(9) or player - computer == abs(9):
			print ("you guessed wrong you are nine steps away Try again")
			continue
	u=str(input("if you want to play again? yes or no?"))
	if u == 'yes':
		continue
	else:
		break



