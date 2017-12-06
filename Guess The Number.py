import random


print "Hello, welcome to Guess The Number!\n\n"

# You must use a for loop in order for the user to guess the number in 3 tries.
print "As the title suggest, a number between 1-10 is generated and you must guess what it is in 3 tries.\n\n"

while True:
	choice = raw_input("Do you want to play?(y/n): ", )

	if choice not in ('y', 'n'):
		
		
		print "Please enter in a valid choice: \n",
		continue
	elif choice == 'y':
		print "Enter your name:"
		name = raw_input()
		break
	
	elif choice == 'n':
		print "I understand, well have a great day!"
		break
	

while choice == "y":
	min = 1 
	max = 10
	
	guess = random.randint(min, max)
	
	
	
	# This is where for loops comes in
	for i in range(1,4):
		print "\nTry # %d \n" % i
		guess_1 = int(raw_input("Enter in your guess: "))
		
		if guess_1 == guess:
			print "That is the right number %s!" % name
			break
		elif guess_1 > guess:
			print "You are high.\n"
		elif guess_1 < guess:
			print "You are low.\n"
		else:
			continue
	print guess
	
	
	choice = raw_input("Do you want to play again?(y/n): ",)
	if choice not in ('y', 'n'):
		print "That is not a valid input. \nPlease enter 'y' or 'n': ",
		continue
	elif choice == 'y' or 'n':
		print "Thank you for playing!"
		continue