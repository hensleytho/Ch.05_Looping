'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''

import random
done = False
loss = 0
wins = 0
ties = 0
print("Welcome to Rock, Paper, Scissors! Today we will be testing your skills")
print("If you give up and quit, press \"4\"")

while not done:

    x = random.randint(1,3)

    print("1.) Rock")
    print("2.) Paper")
    print("3.) Scissors")

    play = int(input("Pick a number"))
    if play == 4:
        done = True

        print("")
        print("Goodbye")

    else:
        if play == x:
            print("You tied!")
            ties += 1
            if x == 1:
                print("We both picked Rock!\n")
            elif x == 2:
                print("We both picked Paper!\n")
            else:
                print("We both picked Scissors!\n")
        elif play == 1 and x == 2 or play == 2 and x == 3 or play == 3 and x == 1:
            print("You win!")
            wins += 1
            if x == 1:
                print("You Picked Paper! The computer chose Rock!\n")
            elif x == 2:
                print("You picked Scissors! The computer chose Paper!\n")
            else:
                print("You picked Rock! The computer chose Scissors!\n")
        elif play == 1 and x == 3 or play == 2 and x == 1 or play == 3 and x == 1:
            print("Tough luck, You lose.")
            loss += 1
            if x == 1:
                print("You selected Scissors, and the computer chose Rock.\n")
            elif x == 2:
                print("You selected Rock, and the computer chose paper.\n")
            else:
                print("You selected paper, and the computer chose Scissors.\n")
        else:
            print("That was not an option, you may try again or quit.")

print("You had",wins,"wins!")
print("You had",loss,"losses!")
print("You had",ties,"ties!\n")

