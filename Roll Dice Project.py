import random

min_num = 1
max_num = 6

while True:

    print "We are going to play a little rolling dice game.\n\n"
    choice = raw_input("Do you want to play?(y/n): ", )

    if choice not in ('y', 'n'):
        print "Please enter in a valid choice for the program. Try again\n"
        continue
    elif choice == "n":
        print "Have a good one!"
        break
    else:
        print "Ok, let's get going.\n\n\nLOADING..."
        name = raw_input("What is your name?: ", )
        break

roll_again = "y"
while choice == "y" and roll_again == "y":
    print "\n\n%s has thrown both of the dices..." % name
    print "Rolling ... Rolling ... Rolling ... stopped\n"
    print "Look! The first dice is %d and the second dice is %d\n\n" % (random.randint(min_num, max_num), random.randint(min_num, max_num))

    roll_again = raw_input("Roll the dices again?(y/n)")
    if roll_again not in ('y', 'n'):
        print "Please enter in a correct value(y/n)"
        continue
    elif roll_again == "n":
        print "Have a good one!"
        break

