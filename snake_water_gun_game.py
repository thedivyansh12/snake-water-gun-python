import random

computer = random.choice([-1, 0, 1])
yourstr = input("enter your choice (s, w, g) : ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reversedict = {1: "SNAKE", -1 : "WATER", 0 : "GUN"}
you = youdict[yourstr]
print(f"You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")


if(computer == you):
    print("It's a draw")
elif((computer - you) == -2 or (computer - you) == 1):
    print("YOU WIN !!")
else: 
    print("YOU LOSE !")
