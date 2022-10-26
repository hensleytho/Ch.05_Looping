'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

-------
driving a car instead of camel, drinking gatorade instead of using canteen,
using cruise control instead of moderate speed, going up to 90 mph instead of full speed ahead,
stopping for gas instead of stopping for the night.
-------
'''

bg_red = '\u001b[41;1m\u001b[30m'
END = '\033[0m'
bg_green = '\u001b[42;1m\u001b[30m'
bg_yellow = '\u001b[43;1m\u001b[30m'
bg_orange = '\u001b[48;2;255;165;1m\u001b[30m'
text_yel = '\u001b[33;1m'
print()
print()
print("\033[95mWelcome to the Camel Game... well sort of.")
print("This is the Camel Game, but with a twist.")
print("\nThe instructions are simple, you're given a car that you must deliver to the waypoint.")
print("Along the way you will need to hydrate yourself, stop for gas, and watch out for carjackers.\n")
print("You will start with 3 drinks, and the carjackers 20 miles behind, dont get caught!" + END)
print(bg_green + "\33[3;4mGood luck!" + END)
print()
mt = 0 #miles traveled
gd = 3 #gatorade drinks
cg = 100 #cars gas
th = 0 #thirst
cj = -20 #carjackers -20 miles away
car = 0 #car variable
'''
Figure out how to stop the while loop from going forever
'''
done = False
import random
while not done:
    print("\033[97ma.) Drink your gatorade.")
    print("b.) Set cruise control.")
    print("c.) Speed up.")
    print("d.) Stop for gas.")
    print("e.) Status check.")
    print("q.) Quit")
    choice = input("What would you like to do?: " + END)

    if mt >= 200:
        done = True
        print()
        print(bg_green + "Congrats!" + END)
        print(bg_green + "You won!" + END)
        break

    if choice.lower() == "q":
        done = True
        print()
        print(bg_red + "Come again soon!" + END)
        exit()
    elif choice.lower() == "d":
        print("\u001b[33;1m\n Good idea!")
        print("Gas levels full.\n" + END)
        car = 0
    elif choice.lower() == "a" and gd > 0:
        gd -= 1
        th = 0
        print()
        print("\33[94mGood thinking, you are no longer thirsty!\n")
    elif choice.lower() == "e":
        print()
        print(text_yel +"Miles Traveled: ", mt)
        print("Gatorade drinks left: ", gd)
        print("Car-Jackers ", mt-cj, "miles behind!")
        print("Keep it up!\n" + END)
    elif choice.lower() == "c":
        miles = random.randint(12, 22)
        carj = random.randint(10, 20)
        tiredness = random.randint(2, 6)
        th += 1
        mt += miles
        cj += carj
        car = tiredness
        print("\33[92m\n Full speed ahead!")
        print("\33[92mYou just traveled ", miles, "miles!\n")
        oasis = random.randrange(1, 21)
        if oasis == 1:
            print("You found an Oasis!\n")
            car = 0
            th = 0
            gd = 3
    elif choice.lower() == "b":
        miles = random.randint(8, 16)
        carj = random.randint(8, 16)
        tiredness = random.randint(1,4)
        car = tiredness
        mt += miles
        cj += carj
        th += 1
        print()
        print("\33[92mYou have just traveled", miles, "miles!\n")
        oasis = random.randrange(1, 21)
        if oasis == 1:
            print("\33[133mYou found an Oasis!\n")
            car = 0
            th = 0
            gd = 3
        if car >= 5 and car < 8:
            print(bg_yellow + "Your car is running low on gas." + END)
        else:
            pass
        if car >= 7:
            done = True
            print(bg_orange + "Your car has run out of gas." + END)
            print(bg_red + "Game Over." + END)
            break
        else:
            pass
        if th >= 4 and th < 6 and choice.lower() != "a":
            print(bg_yellow + "You are very thirsty!" + END)

        else:
            pass
        if th >= 6:
            done = True
            print(bg_orange + "You died of thirst!" + END)
            print(bg_red + "Game Over." + END)
            break
        else:
            pass
        if cj >= mt:
            done = True
            print(bg_orange + "The Car-Jackers got you!" + END)
            print(bg_red + "Game Over." + END)
            break
        else:
            pass
        if mt - cj <= 15:
            print(bg_yellow + "The Car-Jackers are close!" + END)
        else:
            pass

    else:
        print()
        print(bg_red + "That was not an option." + END)
        print()
