import random

rules=""" Lets Play Rock Scissor Paper
setting up the rule
=================================================================
1.papper vs rock:papper wins
2.papper vs scissor: scissor wins
3.rock vs scissor:rock wins
"""

print(rules)


possible_choice=["rock","paper","scissor"]
users_choice=input((f"neter your choice {possible_choice}")).lower()
comp_choice=random.choice(possible_choice)

print(f"user chose {users_choice} , computer_chose {comp_choice}")

if users_choice == comp_choice:
    print("its a tie")
elif  comp_choice=="paper":
    if users_choice=="rock":
        print("computer won")
elif  comp_choice=="scissor":
    if users_choice=="paper":
        print("computer won")
elif  comp_choice=="rock":
    if users_choice=="scissor":
        print("computer won")
else:
    print("invalid choice")
print("thank you")
