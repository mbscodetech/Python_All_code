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