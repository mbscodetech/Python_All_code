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