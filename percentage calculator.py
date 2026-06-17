x="""WELCOME TO PERCENTAGE CALCULATING PROGRAM
============================================"""
print(x)
name=input("enter your full name")
std=int(input("enter std(1 to 12)"))
first=int(input("enter marks of first subject"))
second=int(input("enter marks of second subject"))
third=int(input("enter marks of third subject"))
forth=int(input("enter marks of forth subject"))
fifth=int(input("enter marks of fifth subject"))
sixth=int(input("enter marks of sixth subject"))
total_mark=first+second+third+forth+fifth+sixth
percentage=float((total_mark/600)*100)

if percentage > 75:
    print(f"congratulation,{name}! For recieving a total of {total_mark} marks out of 600,securing {percentage}% and achieving distinction in {std} class.")
elif percentage > 60 and percentage < 74:
     print(f"congratulation,{name}! For recieving a total of {total_mark} marks out of 600,securing {percentage}% and achieving first class in {std} class.")
elif percentage > 49 and percentage < 59:
    print(f"congratulation,{name}! For recieving a total of {total_mark} marks out of 600,securing {percentage}% and achieving second division in {std} class.")
elif percentage > 35 and percentage < 44:
     print(f"congratulation,{name}! For recieving a total of {total_mark} marks out of 600,securing {percentage}% and achieving pass in {std} class.")
else:
     print(f"sorry,{name}! For recieving a total of {total_mark} marks out of 600,securing {percentage}% and achieving fail in {std} class.")
     print("thank you")