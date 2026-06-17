import random

comp_choice=random.randint(1,20)
num=0

while True:
    users_choice=int(input("enter a number between 1 to 20:"))

    if comp_choice > users_choice:
        print("go a bit higher")
        num=num+1
    elif comp_choice < users_choice:
        print("go a bit lower")
        num=num+1
    else:
         print("Hurray!, you guessed it right")
         break
print(f"it took {num} attempt")
print("thank you")
  

    

    

    




