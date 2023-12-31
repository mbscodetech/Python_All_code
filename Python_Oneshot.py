#print("hello")
"""
q.1.
write a program to print twinkle twinkle
littile star poem in python
"""
"""
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
''')
"""
"""
q.2-use repl and print the table of 
5 using it
"""
#use terminal
"""
q.3.
inistall an external module and use it to perform an
 operation of playing music in python
"""
"""
from playsound import playsound
playsound('D:\\My all code\\PYTHON PROGRAMMING\\play.mp3')
"""
"""
q.4.
write py program to print the content
 of a directories using os module,search online for the function which does that
"""
"""
import os
print(os.listdir())
"""
"""
#variables
a_122='''mahi bhai'''
#p='hello ji'
#q="munna bhai'
b=345
c=45.32
d=True
#d=none
#printing the variables
a="gullu"
print(a)
print(b)
print(c)
print(d)
#printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
"""
"""
#operators
a=3
b=4
#Airthmetic Operators
print("The Value of 3+4 is",3+4)
print("The Value of 3-4 is",3-4)
print("The value of 3*4 is ",3*4)
print("The value of 3/4 is",3/4)
#Assignment operators
a=34
a-=12
a*=12
a/=12
print(a)
#Comparision Operators
# b=(14<=7)
# b=(14>=7)
# b=(14<7)
# b=(14>7)
# b=(14==7)
b=(14!=7)
print(b)
#Logical operators
bool1=True
bool2=False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or bool2))
print("The value of not bool2 is",(not bool2))
"""
"""
#Typecasting
a="352346"
a=int(a)
print(type(a))
print(a+5)
"""
"""
#Input function
a=input("Enter a number: ")
a=int(a)#Convert a to an Integer(if possible)
print(type(a))
"""
#practice set 2
"""
q.1.wa python program to add two numbers
"""
"""
a=30
b=15
print("the sum of a and b is",a+b)
"""
"""
q.2.
wa python program to find remainder when a number is 
devided by 2
"""
"""
a=12
b=2
print("th number when a is devided by b is",a%b)
"""
"""
q.3.check the type 
of variable assigned using input() function
"""
"""
a=34
print(a)
a=input("enter your number:")
print(type(a))
a=int(a)
print(a)
"""
"""
q.4.use comparision operators to find out whether a given
variable a is greter than 'b' or not.
take a=34 and b=80
"""
"""
a=34
b=80
print(a>b)
print(b>a)
"""
"""
q.5.wa python program to
find average of two numbers entended by the user
"""
"""
a=input("enter first number:")
b=input("enter second number:")
a=int(a)
b=int(b)
avg=(a+b)/2
print("the average of a and b is",avg)
"""
"""
q.6.wa puthon program to calculate square of a number
extend by the user
"""
"""
a=input("enter first number:")
a=int(a)
b=int(a*a)
print("the square is",b)
"""
#Strings
"""
b="Mahi's"  #--->use this if you have single quotes in
your strings
"""
"""
b='''Harry's and harry's'''
print(b)
#print(type(b))
"""
"""
#string slicing
greeting="Good Morning"
name="mahi"
print(type(name))
#Concatenating two strings
c=greeting+name
print(c)
"""
"""
name="Munna Bhai"
print(name[4])
#name[3]="d"---->does not work
print(name[1:4])
print(name[:4]) # same as name[0:4]
print(name[1:]) # same as name[1:5]
c=name[-4:-1]  # same as name[1:4]
print(c)
"""
"""
name="GulluRangilaBadaHiPyaraHain"
d = name[0::2]
print(d)
"""
#String Function
"""
story='''once upon a time there was a man
 whose name is mahi and he lift the 1 t20,
 1 50-50 and 1 ct'''
 """
# print(len(story))
# print(story.endswith("ct"))
# print(story.count("c"))
# print(story.capitalize())
# print(story.find("upon"))
# print(story.replace("man","Legend"))
# kahani="msd is the \ngretest finisher\t in the\\world"
# print(kahani)
#Practice set 3
"""
 1-write a python program to display a user entered name
 followed by Good Afternoon using input() function
"""
# name=input("Enter your name:\n")
# print("Good Afternoon,"+ name)
"""
2-write a program to fill in a letter template 
given below with name and date.
letter='''Dear</NAME/>
you are Selected!
<!DATE!>
"""
# letter='''Dear <|NAME|>,
# Greetings from ABC coding house.
#  I am happy to tell you about your
#  selection.
#  You are selected!
#  Have a great day ahead!
#  Thanks and regards,
#  Bill
#  Date: <|DATE|>
# '''
# name=input("Enter Your Name\n");
# date=input("Enter Date\n")
# letter=letter.replace("<|NAME|>",name)
# letter=letter.replace("<|DATE|>",date)
# print(letter)
"""
q.3-wap to deteect double spaces in a string
"""
# st="This is a string with double  spaces   "
# doubleSpaces=st.find("  ")
# print(doubleSpaces)
"""
q.4-replace the double spaces from pr.3 with single spaces
"""
# st="This is a string with double  spaces  ok"
# st=st.replace("  "," ")
# print(st)
"""
q.5.write a new letter
"""
# letter="Dear mahi,This crickete game is nice! Thanks"
# print(letter)
# formatted_letter="Dear msd,\nyou are great\tfinisher and\ngreat captain\nThanks!"
# print(formatted_letter)
"""
lists in python
"""
# Create a list using []
# a=[1,2,4,56,6]
# Print the list using print() function
# print(a)
# Access using index using a[0],a[1],a[2]
# print(a[2])
# Change the value of list using
# a[0]=98
# print(a)
# We can create a list with items of different types
# c=[45,"Harry",False,6.9]
# print(c)
# List slicing
# friends =["Mahi","yuvi","sunil","rohit","shami","nehra",45]
# print(friends[0:4])
# print(friends[-4:])
#list methods in python
# l1=[1,8,7,2,21,15]
# print(l1)
# sorts the list
# l1.sort()
# reverse the list
# l1.reverse()
# append in the list
# l1.append(45)   #add 45 at the end of the list
#insert in the list
# l1.insert(2,544)   #inserts 544 at index 2
#pop in the  list
# l1.pop(2)   #remove element at index 2
#remove in the list
# l1.remove(21)    # remove 21 from the list
# print(l1)
"""
Tuples in python
"""
# Creating a tuple using ()
# t=(1,2,4,5)
# t1 =()    # Empty tuple
# t1 =(1)   # Wrong way to declare a Tuple with single element
# t1=(1,)  # Tuple with single element
# print(t1)
# Printing the element of a tuple
# print(t[0])
# Printing update the values  of a tuple
# t[0] = 34    # throws an error
# Creating a tuple using ()
# t=(1,2,4,5,4,1,2,1,1)
# print(t.count(1))   #count 1 in a
# print(t.index(5))   #index 5 pe kya
"""
CHAPTER 4 PRACTICE SET
"""
"""
Q.1.wap to store seven fruits in a 
list entered by the user
"""
"""
f1 = input("Enter Fruit Number 1: ")
f2 =input("Enter Fruit Number 2: ")
f3 =input("Enter Fruit Number 3: ")
f4 =input("Enter Fruit Number 4: ")
f5 =input("Enter Fruit Number 5: ")
f6 =input("Enter Fruit Number 6: ")
f7 =input("Enter Fruit Number 7: ")
myFruitList =[f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)
"""
"""
Q.2.wap to accept marks of 6 students and
display them in a sorted manner
"""
"""
m1=int(input("Enter Marks for Student Number 1:"))
m2=int(input("Enter Marks for Student Number 2:"))
m3=int(input("Enter Marks for Student Number 3:"))
m4=int(input("Enter Marks for Student Number 4:"))
m5=int(input("Enter Marks for Student Number 5:"))
m6=int(input("Enter Marks for Students Number 6:"))
myList=[m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)
"""
"""
Q.3.Check that a tuple cannot be changed in python
"""
"""
a=(2,4,5,3,2)
a[0]=45
"""
# TypeError: 'tuple' object does not support item assignment
"""
Q.4.wap to sum a list with 4 numbers
"""
"""
a=[2,4,56,7]
print(a[0]+a[1]+a[2]+a[3])
print(sum(a))
"""

"""
Q.5.wap to count the number of zeros in the following tuple
a=(7,0,8,0,0,9)
"""
"""
t=(7,0,8,0,0,9)
print(t.count(0))   #count 0 in a
"""
"""
DICTIONARY IN PYTHON
"""
#syntax of dictionary
"""
mydict={
      "fast":"In A Quick Manner",
      "mahi":"Captain of team india",
      "scores":[183,148,139],
      "anotherdict":{'ms':'cricketer'}
}
print(mydict['fast'])
print(mydict['mahi'])
mydict['scores']=[91,128]
print(mydict['scores'])
print(mydict['anotherdict']['ms'])
"""
#methods of dictionary in python
"""
myDict={
      "fast":"In a Quick Manner",
      "mahi":"a cricketer",
      "marks":[1,2,5],
      "anotherdictt":{"mahi":"player"},
      1:2
}
#Dictionary Methods
print(list(myDict.keys()))   #print the key of the dictionary
print(myDict.values())       #prints the values of the dictionary
print(myDict.items())      #print the (key,value) for all contents of the dictionary
print(myDict)
updateDict={
      "ballu":"dost",
"shreya":"good friend",
"vaishnavi":"devi",
"munna":"bhai"
}
myDict.update(updateDict)    #updates the dictionaery by adding  key-value pairs from updateDict
print(myDict)
print(myDict.get("mahi"))   #print value associated with key "mahi"
print(myDict["mahi"])     #print value associates with key "mahi"
#the difference between .get and [] syntax in dictionaries?
print(myDict.get("mahi2"))   #returns none as mahi2 is not present in the dictionary
# print(myDict["mahi2"])   #throws an error as mahi2 is not present in the dictionary
"""
##SETS IN PYTHON
#Syntax of sets in python
# a={1.3,4,5,1}
# print(type(a))
# print(a)
#empty set in python
"""
Important:this synatx will create an empty dictionary and
not an empty set
"""
# a={}
# print(type(a))  #this is dictionary
#SET METHODS IN PYTHON
"""
Importance:An empty set can be created using the below syntax:
"""
#Creating an empty set
# b=set()
# print(type(b))
#Adding values to an empty set
# b.add(4)
# b.add(5)
# b.add(5) #Adding a value repeatedly does not changes a set
# b.add((4,5,6))
#Accessing elements
#b.add({4:5})   #cannot add list or dictionary to sets
# print(b)
#Length of the set
# print(len(b))  #prints the length of this set
#Removel of an item
# b.remove(5)  #remove 5 from set b
# b.remove(15)  #throws an error while trying to remove 15( which is not present in the set)
# print(b)
# print(b.pop()) #remove an arbitary element from the set and return the element removed
# print(b)
# b.clear()  #empties the set b
# print(b)
# c=b.union({8,11})  #union means all
# print(c)
# c=b.intersection({8,11,4,5,1})  #intersections means common
# print(c)
# c=b.union({8,11})  #union means all
# print(c)
# r1=c-b   # c={8,11,4,5} isme se 4,5 nikal diya 8,11 bacha
# print(r)
# r2=b-c  # b-={4,5} isme se c={8,11,4,5} nikal diya pura ka pura nikal gaya empty set bacha
# print(r)
"""
Practice Set 5:
"""
"""
Q.1:Write a program to create a dictionary of Hindi 
words with values as their English translation.
 Provide the user with an option to look it up!
"""
"""
myDict={
      "Banda":"Man",
      "Pankha":"Fan",
      "Dabba":"Box",
      "Vastu":"Item",
      "Bandi":"GF",
}
print("uptions are",myDict.keys())
a=input("enter the hindi word\n")
#print(the meaning of your word is:",myDict[a])
#Below line will not throw an error if the key is not present in the dictionary
#we always want error free code
print("The meaning of your word is:",myDict.get(a))
"""


"""

Q.2.Write a program to input eight numbers from the user
 and display all the unique numbers (once).

"""
#uniqe-means set
"""
num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))
s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)
"""

"""
Q.3.
Can we have
 a set with 18(int) and “18”(str) as a value in it?
"""
"""
s={18,"18","18.1"}
print(s)
"""
"""
Q.4.What will be the length of the following set S:
S = Set()

S.add(20)

S.add(20.0)

S.add(“20”)
What will be the length of S after the above operations?
"""
"""
s={20,20.0,"20"}
print(s)
print(len(s))
"""

"""
Q.5.
S = {}, what is the type of S?
"""
# the ans is dict
"""
s= {}
print(type(s))
"""

"""
Q.6.Create an empty dictionary. Allow 4 friends to 
enter their favorite language as values and use keys 
as their names. Assume that the names are unique.
"""
"""
favLang={}
a=input("enter your favorite language shubham\n")
b=input("enter your favorite language shubham\n")
c=input("enter your favorite language shubham\n")
d=input("enter your favorite language shubham\n")
favLang['shubham']=a
favLang['ankit']=b
favLang['sonali']=c
favLang['harshita']=d
print(favLang)
"""
"""
Q.7.
If the names of 2 friends are the same; 
what will happen to the program in Program 6?
"""
"""
#bad me jo aayega use le liya
favLang={}
a=input("enter your favorite language shubham\n")
b=input("enter your favorite language shubham\n")
c=input("enter your favorite language shubham\n")
d=input("enter your favorite language shubham\n")
favLang['shubham']=a
favLang['ankit']=b
favLang['shubham']=c  #latest lega wah
favLang['harshita']=d
print(favLang)
"""
"""
Q.8.If the languages of two friends are the same; 
what will happen to the program in Program 6?
"""
#lang 2 fr same-kuch bhi nahi huva,key unique values nahi

"""
Q.9.Can you change the values inside a list which 
is contained in set S
S = {8, 7, 12, “Harry”, [1, 2]}
"""
#saval hi galat,list bhi nahi aa sakati set me,tuple to change hota hi nahi
#set ke andar list aur tuples change nahi hota
