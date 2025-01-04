import random
choices=["rock","paper","scissors"]
aichoice=random.choice(choices)
playerchoice=input("Do you want to be rock, paper, or scissors?")
if playerchoice=="rock":
    if aichoice=="rock":
        print("Its a draw")
    elif aichoice == "paper":
        print("You lose")
    else:
        print("You win")
elif playerchoice=="paper":
    if aichoice=="rock":
        print("You win")
    elif aichoice == "paper":
        print("Its a draw")
    else:
        print("You lose")
elif playerchoice=="scissors":
    if aichoice=="rock":
        print("You lose")
    elif aichoice == "paper":
        print("You win")
    else:
        print("Its a draw")