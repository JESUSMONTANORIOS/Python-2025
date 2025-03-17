'''
Print Hello World to the Screen
By Jesus M
'''
#Learn python Coding in 2025 with John Elder

import os
os.system('clear') # This is another comment

first_name = 'Jesus' 
print (first_name) 

first_name = "" 
print (first_name) 


'''
Data types
Strings
Numbers
Lists
Tuples
Dictionaries
Boolean
'''

first_name = "Bob" # String
age=45 # Number
names = ["Jhon","Bob","Mary"] # This is a list and index starts at 0
print (names[0])

#Tuple is a list you can't change
names = ("Jhon","Bob","Mary") # This is a tuple
print (names)
print (names[1])

#Dictionaries "key" : "value"
fav_pizza={
	"Jhon" : "Pepperoni",
	"Bob" : "Mushroon",
	"Mary":"Cheese"
	}

print (fav_pizza["Jhon"])

#Boolean True or False

 
'''
git push of new revision
git add .
git commit -am " "
git push
'''

#Strings

# \ ignore and \n new line

#for contcatenating strings use + symbol

greetings = "Hello my name is Jesus"

#print(greetings.upper()) upper case
#print(greetings.lower()) lower case
#print(greetings.capitalize()) caps first letter in string
#print(greetings.title())
#print(greetings.swapcase())
#print(len(greetings)) string lenght
##print(greetings[13]) return 14 element in the string (starts at 0)
#print(greetings[18:22]) returns elements in the range
#print(greetings.split(" ") returns a list of separated words
#print(greetings.split(" "[5]) returns element 6 of the list
#print(greetings.split(" ")[4:6]) returns a range

#Numbers

num=10
print(10)
print(float(10))
num=10.25
print(int(num))
print(7+2)
print(7-2)
print(10/3)
print(10%3) #remainder
print(5**2)

num_1=5
num_2=2
print(num_1*num_2)

#15 or 7
print(4 + 1 * 3)
print((4 + 1) * 3)

num="6" # this is a string

print((int(num)) * 3) #convert number to string

# LISTS

names = ["John","Bob", 'Tina']
names[0]="Wes"
print(names[0])
print(names)
names = ["John","Bob", 'Tina']
names.append("Wes")
print(names)
print(names[3])
names = ["John","Bob", 'Tina', 45]
print(names[3]+10)
nums=[1,2,3,4,5]
names = ["John","Bob", 'Tina', nums]
print(names)
print(names[3])
print(names[3][2])
print(names[3][2]+10) 
names = ["John","Bob", 'Tina']
print(len(names))
print(names[len(names)-1])

#TUPLES

names = ("John","Bob", 'Tina')
print(names)

tuple1 = ("John","Bob", 'Tina')

print(tuple1[0:2])

tuple2 = ("Mary",)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple3=tuple1[0:2]
print(tuple3)

tuple3=tuple1[1]
print(tuple3)

#DICTIONARIES

favorite_pizza = {
	"John" : "Pepperoni",
	"Bob" : "Mushroon",
	"Mary": "Cheese"
	}

del favorite_pizza["John"] #delete an element form the dictionary

print(favorite_pizza)

favorite_pizza = {
	"John" : "Pepperoni",
	"Bob" : "Mushroon",
	"Mary": "Cheese"
	}

favorite_pizza.update({"Tina":"green peppers"})

print(favorite_pizza)
print(favorite_pizza["Tina"])

favorite_pizza["John"]="fish" #change the value for a key
print(favorite_pizza["John"])

favorite_pizza = {
	"John" : [1,2,3,4,5],
	"Bob" : "Mushroon",
	"Mary": "Cheese"
	}

print(favorite_pizza["John"])
print(favorite_pizza["John"][2])
print(favorite_pizza["John"][2]+10)

'''
Assigment operators
=
+=
-=
*=
/=
**=
%=
'''

num=47

num=num+1
print(num)
num+=2
print(num)


'''
COMPARISON OPERATORS
==
!=
>
<
>=
<=
'''

print(10==10)
print(10==9)
print(10!=10)

print("Mary"=="Mary")
print("Mary"=="mary")

print([1,2,3]==[1,2,3])


'''
Conditional Statements
if / else / elif
'''

num=10

if (num>10):
	print("Your Number Is Greater Than 10!")

elif(num==10):
	print("your number is 10!")

else:
	print("Your number is less than 10")


#multiple conditional statements

# and / or

num=150

if (num>10) and (num>100):
	print("Your Number Is Greater Than 10 ans 100!")



# WHILE LOOPS

counter=0

while (counter<=10):
	print ("The count is: "+ str(counter))
	counter+=1


# For Loops

names = ["John","Bob", "Mary"]

for name in names:
	print(name)

fav_pizza = {
	"John" : "Pepperoni",
	"Bob" : "Mushroon",
	"Mary": "Cheese"
	}

for key,value in fav_pizza.items():
	print(key + " likes " + value + " pizza!")

