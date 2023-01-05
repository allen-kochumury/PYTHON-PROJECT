import random
a = int(input("Enter Number of Rounds: "))
b = ["Rock","Paper","Scissors"]
d = random.choice(b)
p = input("Enter \"R\" for rules of the game or Press any other Key to skip: ")
x = 0
y = 0
if p.upper() == "R":
    print("")
    print("User can Select between \"Rock\", \"Paper\", \"Scissors\"")
    print("The CPU will randomly generate \"Rock\", \"Paper\", \"Scissors\" to counter the user")
    print("If User Wins against CPU according to hierarchy below ,User Wins, Else CPU wins")
    print("Rock wins against Scissors; Paper wins against Rock; and Scissors wins against Paper")
    print("")
else:
    pass
for i in range(0,a):
    d = random.choice(b)
    c = input("Rock, Paper or Scissors: ")
    print("CPU : {0}".format(d))
    if c.title() == d:
        print("Tie")
        print("")
    elif c.title() == "Rock" and d == "Scissors":
        # USER VICTORY
        print("You win! Rock smashes Scissors")
        x = x + 1
        print("")
    elif c.title() == "Scissors" and d == "Paper":
        print("You win! Scissors cut Paper")
        x = x + 1
        print("")
    elif c.title() == "Paper" and d == "Rock":
        print("You win! Paper covers Rock")
        x = x + 1
        print("")
        # CPU VICTORY
    elif d == "Rock" and c.title() == "Scissors":
        print("You lose... Rock smashes Scissors")
        y = y + 1
        print("")
    elif d == "Scissors" and c.title() == "Paper":
        print("You lose... Scissors cuts Paper")
        y = y + 1
        print("")
    elif d == "Paper" and c.title() == "Rock":
        print("You lose... Paper covers Rock")
        y = y + 1
        print("")
    else:
        print("Invalid Input, Game Ends")
        break

print("")
print("The final Score: ")
print("CPU: ",y)
print("User: ",x)
if y > x:
    print("CPU wins, Better luck next time")
elif x == y:
    print("It was a Tie")
else:
    print("Congratulations!, You won")
