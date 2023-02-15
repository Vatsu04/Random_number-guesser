import random 

def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	for i in range(5):
		guess = int(input(f"Guess a number between 1 and {x}, you have 5 chances"))

		if guess < random_number:
			print('Sorry, too low \n')
		elif guess > random_number:
			print('Sorry, too high\n ')
		elif guess == random_number:
			print(f'Yay, congrants. You have guessed the number {random_number} correctly!!')
	print(f"You have failed to guess {random_number}")
guess(10)