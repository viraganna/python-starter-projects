import random
import logic

all_tips = ["r", "s", "p"]
next_game = 'y'

while (next_game == 'y'):
    user_choice = input("Select (r)ock, (s)cissors, (p)aper: ")
    computer_choice = random.choice(all_tips)
    logic.whoWins(user_choice, computer_choice)
    next_game = input("Akarsz még játszani? y/n: ")
    while (next_game != 'y' and next_game != 'n'):
        print("Invalid, choose y or n")
        next_game = input("Akarsz még játszani? y/n: ")
print("Köszi a játékot!")
logic.result()


