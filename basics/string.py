name="alwin"

length=len(name)
print(length)

namesort=name[0:3]
print(namesort)

print(name[-3:-1])

number="0123456789"
print(number[1:7:3])
print(number[1:7:2])


print("______________")
#important functions od strings

print(name.isdigit())
print(name.isalnum())
print(name.isalpha())
print(name.capitalize())
print(name.upper())
print(name.find("w"))
print(name.count("a"))

fruit="bannana"
print(fruit.count("a"))

a="alwin is a good boy"
print(a.replace("good","god"))

print(f"my name is {name}")

letter='''hello <name>
you are selected
<date>'''

print(letter.replace("<name>","alwin").replace("<date>","9-6-2006:"))