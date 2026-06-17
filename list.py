#list

#syntax
friends=["alwin","aaron",9,6.6]

# calling members of list
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#lists are mutable ie we can make changes in the list

friends[1]="shabu"
print(friends)
print(friends[1])

#append method
friends.append("aaron")
print(friends)

#remove method

friends.remove("aaron")
print(friends)

#sort method

num=[1,5,10,2,8,6]
num.sort()
print(num)

#reverse method

num=[1,5,10,2,8,6]
num.reverse()
print(num)

#insert method
num.insert(3,5)
print(num)

#pop method
num.pop(3)
print(num)
