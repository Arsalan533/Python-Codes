import random
'''
1 for snake
-1 for water
0 for gun

'''
computer = -1
youstr = input("Enter your choose: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]

print(f"You Choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")
else:
    # if(computer ==-1 and you ==1):
    #     print("You win")

    # elif(computer ==-1 and you ==0):
    #     (print("You Lose"))

    # elif(computer ==1 and you ==-1):
    #     (print("You Lose"))

    # elif(computer ==1 and you ==0):
    #     (print("You win"))

    # elif(computer ==0 and you ==-1):
    #     (print("You win"))

    # elif(computer ==0 and you ==1):
    #     (print("You win"))

