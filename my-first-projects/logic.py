user_wins = 0
computer_wins = 0
dontetlen = 0

def whoWins(user, computer):
    global user_wins
    global computer_wins
    global dontetlen

    if (user == "p"):
        if (computer == "r"):
            print("User nyert")
            user_wins += 1
        elif (computer == "s"):
            print("Computer nyert")
            computer_wins += 1
        else:
            print("Döntetlen")
            dontetlen += 1

    elif (user == "r"):
        if (computer == "s"):
            print("user nyert")
            user_wins += 1
        elif (computer == "p"):
            print("computer nyert")
            computer_wins += 1
        else:
            print("Döntetlen")
            dontetlen += 1
    
    elif (user == "s"):
        if (computer == "r"):
            print("Computer nyert")
            computer_wins += 1
        if (computer == "p"):
            print("User nyert")
            user_wins += 1
        else:
            print("Döntetlen")
            dontetlen += 1
    else:
        print("Invalid user input")

    print("user: ", user)
    print("computer: ", computer)

def result():
    print("User wins: ", user_wins)
    print("Computer wins: ", computer_wins)
    print("Döntetlen: ", dontetlen)