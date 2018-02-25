import random

comGuess = random.randint(0,100)

while True:
	userGuess = int(input("Enter a guess between 0 and 100: "))
	if userGuess > comGuess:
		print ("Guess lower")
	elif userGuess < comGuess:
		print ("Guess higher")
	else:
		print ("Congratulations you've guessed right")
		break