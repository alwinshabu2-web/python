def passwordstrength_checker():
    password=input("enter a password:")
    is_length_ok=(len(password) >= 8)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special =False
    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        elif i in "!@#$%^&*":
            has_special = True
    total=sum([is_length_ok, has_upper ,has_lower, has_digit, has_special])
    if total >=4:
        print("password strength : strong")
    elif total ==3:
        print("password strength : Medium")
    else:
        pass

passwordstrength_checker()
 

