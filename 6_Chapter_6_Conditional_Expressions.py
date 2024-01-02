"""
CHAPTER-6-CONDITIONAL EXPRESSIONS
"""
"""
1-if-elif-else ladder in python
"""
"""
a=8
if(a<3):
    print("the value of a is greter than 3")
elif(a>13):
    print("the value of a is greter than 13 ")
elif(a>7):
    print("the value of a is greter than 7")
elif(a>17):
    print("the value of a is greter than 17")
else:
    print("the value is not greter than 3 or 7")
"""
"""
2.Multiple if statements
"""
"""
a = 44
if(a<133):
    print("the value of a is greter than 3")
    if(a>13):
        print("the value of a is greter than 13")
        if(a>7):
            print("the value of a is greter than 7")
            if(a>17):
                print("the value of a is greter than 17")
            else:
                print("the value is not greter than 3 or 7")
                print("done")
"""
"""
QUICK QUIZ:
WAP TO PRINT YES WHEN 
THE AGE ENTERED BY THE USER IS GRETER THAN 
OR EQUAL TO 18
"""
"""
age=int(input("Enter your age: "))
if age>=18:
    print("yes")
else:
    print("no")
"""
"""
RELATIONAL OPERATORS AND LOGICAL OPERATOR
"""
"""
Q.AGE ENTERED BY USER 
"""
"""
age=int(input("enter your age:"))
if(age>34 or age<56):
    print("you can work with us")
else:
    print("you cannot work with us")
"""
"""
in and is 
"""
"""
a=None
if(a is None):
    print("Yes")
else:
    print("No")
"""
"""
a=[45,36,6]
print(435 in a)
print(36 in a)
"""
"""
is else optional-yes
"""
"""
a=6
if(a==7):
    print("yes")
elif(a>56):
    print("no and yes")
else:
    print("I am optional")
"""
"""
CHAPTER 6-PRACTICE SET
"""
"""
1.Write a program to find the greatest of 
four numbers entered by the user.
CRICKET WC MATCH LOGIC-SEMI FINAL( +ve numbers)
"""
"""
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number:3"))
num4=int(input("enter number:4"))
if(num1>num4):
    f1=num1
else:
    f1=num4
    if(num2>num3):
        f2=num2
    else:
        f2=num3
        if(f1>f2):
            print(str(f1)+" is gretest")
        else:
          print(str(f2)+ " is gretest")
"""


"""
2.Write a program to find 
out whether a student is pass or fail if
 it requires a total of 40% and at least 
 33% in each subject to pass. Assume 3 
 subjects and take marks as an input from the user.
"""
"""
sub1=int(input("enter first subject maarks:\n"))
sub2=int(input("enter second subject marks:\n"))
sub3=int(input("enter third subject marks:\n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3<40:
    print("you are fail due to total percentage less than 40")
else:
    print("congradution! you passed the exam")
    """
"""
out of 50
5 subjects total marks=250
34+33+45+40+41=193
percentage=((marksobtained)/totalmarks)*100
"""

"""
3.A spam comment is defined as a text containing
 the following keywords:
“make a lot of money”, “buy now”, “subscribe this”, “click this”. 
Write a program to detect these spams.
"""
"""
text = input("enter the text\n")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click`this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False
if(spam):
    print("this text is spam")
else:
    print("this text is not spam")
    """
"""
4.Write a program to find whether a given username contains 
less than 10 characters or not.
"""
"""
name = input("Enter your name")


if(len(name)<10):
    print("Your username is Correct ")
else:
    print("Your username is too long"
"""

"""
5.Write a program that finds
 out whether a given name is present in a list or not.
"""
"""
names=["harry","shubham","rohit","rohan","aditi","shipra"]
name=input("enter the name to check\n")
if name in names:
    print("your name is present in the list")
else:
    print("your name is not present in the list")
"""
"""
6.Write a program to calculate the grade of a student
 from his marks from the following scheme:
90-100	Ex
80-90	A
70-80	B
60-70	C
50-60	D
<50	F
"""
"""
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
    """
"""
7.Write a program to find out whether a 
given post is talking about “munna” or not.
"""
"""
post = input("Enter a post: ")
if ("MUNNA" in post):
    print("Yes! the post contains the name Harry.")
elif ("munna" in post):
    print("Yes! the post contains the name Harry.")
else:
    print("No! the post does not contain the name MUNNA")
"""