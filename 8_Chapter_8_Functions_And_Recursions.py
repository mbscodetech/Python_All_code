"""
Chapter 8 – Functions and Recursions
"""
"""Q.1.USE 4 subject marks out of 400
 P= MARKS LOGIC AND USE DEF FUNCTIONS"""
"""
def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p  #VALUE KO LAUTO DO
marks1=[45,78,86,77]
percentage1=percent(marks1)

marks2=[75,98,88,78]
percentage2=percent(marks2)
print(percentage1,percentage2)
"""
"""QUICK QUIZ 2:WRITE A PROGRAM TO GREET A USER WITH "Good day" USING FUNCTIONS"""
"""
def greet(name):
    print("Good Day, " + name)
greet("Mahi")
"""
"""QUICK QUIZ:2: """
"""
def greed(name):
    print("good day, " + name)
def mysum(num1,num2):
    return num1+num2
greed("mahi")
s=mysum(6,32)   # 6+32=38
print(s)
"""
"""DEFAULT ARGUMENTS IN PY"""
"""
def greet(name="Stranger"):
    print("Good Day, " + name)
greet("Mahi")  #Good Day Mahi Print Karvaaya
greet()    # DEFAULT STRANGER PRINT KAR VAAYA
"""
"""RECURSION:FUNCTION CALLING ITSELF"""
"""Q.3:FACTORIAL """
"""M.1:"""
"""
#n!=1*2*3*4......*n
n=0
# n=1
# n=2
# n=3
product=1   #default argument
for i in range(n):
    product=product*(i+1)
print(product)
"""
"""M2:FUNCION METHOD:"""
"""
def factorial_iter(n):
   product=1
   for i in range(n):
    product=product*(i+1)
    return product
f=factorial_iter(5)
print(f)
"""
#Imp Notes:
# n!=1*2*3*4.....*n
#n!=[1*2*3*4.....n-1]*n
#n!=n*(n-1)!
"""
def factorial_iter(n):
    product=1  #default argument
    for i in range(n):
        product=product*(i+1)
        return product
def factorial_recursive(n):
        if n==1 or n==0:
            return 1
        return n*factorial_recursive(n-1)
#f=factorial_iter(5)
f=factorial_recursive(0)
print(f)
"""
"""Chapter 8 – Practice Set"""

"""1.Write a program using the function
 to find the greatest of three numbers. """
"""
def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m=maximum(13,55,2)
print("the value of the maximum is " + str(m))  
"""



"""2.Write a python program 
using the function to convert Celsius to Fahrenheit."""
"""
def farh(cel):
    return(cel*(9/5))+32
c=0
f=farh(c)
print("fahreheit temperature is " + str(f))
"""

"""3.How do you prevent a 
python print() function to print a new line at the end? """
"""
print("hello",end="  ")
print("how",end="  ")
print("are",end="  ")
print("you",end="  ")
"""

"""4.Write a recursive function
 to calculate the sum of first n natural numbers.
   """
"""
# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n +recur_sum(n-1)  #recursive sum
     # return n * recur_sum(n - 1)  # recursive product,factorial
# change this value for a different result
num = 5
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))

"""








"""
5.Write a python function to print the
first n lines of the following pattern.

***

**       #For n = 3

*
"""
"""
n=3
for i in range(n):
    print("*" * (n-i))  #prints * n-i times
"""


"""6.Write a python function that converts inches to cms.

"""
# METHOD1:
"""
def inches_to_cms(num):
    print("Length in Centi_Meter:",num*2.45)
inches_to_cms(1)
inches_to_cms(5)
"""

"""method2:
def inch_to_cm(inch):
    return inch * 2.54

if __name__ == "__main__":
    inch_value = int(input('Enter the value in inch: '))

    print(f'{inch_value}″ = {inch_to_cm(inch_value)}cm')
"""

"""7.Write a python function to remove a 
given word from a string and strip it at the same time.
"""
"""
def remove_and_split(string,word):
    newStr=string.replace(word, " ")
    return newStr.strip()
this="   munna is good    "
n=remove_and_split(this,"munna")     #munna ko uda diya
print(n)
#print(this)
#print(this.strip())
"""

"""8.Write a python function to print 
the multiplication table of a given number.
"""
"""
def multiply(num,count):
  return num * count

n = int(input("Enter any Number  :"));
i = 1
for i in range(1,11):
 print(n," * ",i," = ",multiply(n,i))
 i = i + 1
"""