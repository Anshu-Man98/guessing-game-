#Amnshuman's guessing game
import random

def rand():
	r=random.randint(1, 10)
	return r


def data():
	while True:
		player=int(input("enter a number between 1 - 10 :") )
		if player in range(0,11):
			break
		else:
			print("PLEASE enter a number between 1 - 10")
			continue

	return player



while True:
	computer=rand()

	while True:

		player=data()
		print(player)
		if player == computer:
			print( "WOW!!! you guessed right!!!!!!")
			break
		if computer-player == abs(1) or player - computer == abs(1):
			print ("SORRY your guess was wrong! you are 1 steps away Try again")
			continue
		if computer-player == abs(2) or player - computer == abs(2):
			print ("SORRY your guess was wrong! you are 2 steps away Try again")
			continue
		if computer-player == abs(3) or player - computer == abs(3):
			print ("SORRY your guess was wrong! you are 3 steps away Try again")
			continue
		if computer-player == abs(4) or player - computer == abs(4):
			print ("SORRY your guess was wrong! you are 4 steps away Try again")
			continue
		if computer-player == abs(5) or player - computer == abs(5):
			print ("SORRY your guess was wrong! you are 5 steps away Try again")
			continue
		if computer-player == abs(6) or player - computer == abs(6):
			print ("SORRY your guess was wrong! you are 6 steps away Try again")
			continue
		if computer-player == abs(7) or player - computer == abs(7):
			print ("SORRY your guess was wrong! you are 7 steps away Try again")
			continue
		if computer-player == abs(8) or player - computer == abs(8):
			print ("SORRY your guess was wrong! you are 8 steps away Try again")
			continue
		if computer-player == abs(9) or player - computer == abs(9):
			print (" SORRY your guess was wrong! you are 9 steps away Try again")
			continue
	playagain=str(input("DO you want to play again? yes or no?"))
	if playagain == 'yes':
		continue
	else:
		break

print( "Guessing game has ended")

