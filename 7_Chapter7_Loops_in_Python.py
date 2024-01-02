"""
Chapter 7 – Loops in Python
"""
"""
WHILE LOOPS IN PYTHON
"""
"""
i=0
while i<10:
    print("yes" + str(i))
    i=i+1
    print("done")
"""
"""
QUIZ.1:
WAP TO PRINT 1 TO 50 
USING A WHILE LOPS
"""
"""
i=1
while i<=50:
    print(i)
    i=i+1
"""
"""
QUIZ.2:PRINT mahi 5 TIMES
"""
"""
i=0
while i<=5:
    print("mahi")
    i=i+1
"""
"""
QUIZ.3 WAP TO PRINT THE CONTENT OF A LIST USING WHILE LOP
"""
"""
fruits=['Bnana','watermelon','grapes','mangoes']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
    """
"""
FOR LOOP
"""
"""
Q.1.
"""
"""
l=[1,7,8]
for item in l:
    print(item)
    """
"""
Q.2.
"""
"""
fruits=['Bnana','watermelon','grapes','mangoes']
for item  in  fruits:
    print(item)
    """
"""
RANGE FUNCTION IN FOR LOOPS
"""
# for i in range(1,8,1):
#     #start=1 , stop=8,  step size=1
#     print(i)
"""
for with else
"""
"""
for i in range(10):
    print(i)
else:
    print("this is inside else of for")
"""
"""
BREAK STATEMENT IN PYTHON
"""
"""
for i in range(10):
    print(i)
    if i == 5:   
        break  # 0 ke aage no entry rok diya break statement ne
    else:
        print("this is inside else of for")
"""
"""
continue in loops
 """
"""
for i in range(10):
    if i == 5:
        continue  #5 ko chod diya
    print(i)
"""
"""
PASS STATEMENT IN PYTHON
"""
"""
i = 4
if i>0:
    pass   # kuch mat karo
while i>6:
    pass    # kuch mat karo
print("mahi is good cricketer")
def run(player):
    pass
def ouch(player):
    pass
if i>0:
    pass
while i>6:
    pass
print("mahi is good captain and he is the captain of team india")
"""
"""
PRACTICE SET:7
"""
"""
1.Write a program to print the multiplication
table of a given number using for loop.
"""
"""
num = int(input("enter the number:"))
for i in range(1,11):
        print(str(num)  + " X "  + str(i)  + "="  + str(i*num))   
 print(f"{num}X{i}={num*i}")
"""

"""

    2.Write a program to greet all the person names stored in a list l1 and which starts with S.
l1 = [“munna”, “sohan”, “sachin”, “Rahul”]

"""
"""
l1 = ["Munna","sohan","sachin","Rahul"]
for name in l1:
    if name in l1:
        if name.startswith("s"):
            print("bhai "  + name)
"""

"""
3.Attempt problem 1 using a while loop.
print the multiplication
table of a given number using while loop
"""
"""
n = int(input("Enter any Number  :"));
i = 1
while i < 11:
 value = n * i
 print(n," * ",i," = ",value)
 i = i + 1
"""
"""
num=int(input("enter the number: "))
prime = True
for i in range( 2,num):
    if(num%i == 0):
        prime = False
        break
    if prime:
            print("this number is prime")
    else:
            print("this number is not prime")
"""
"""
num = 407

# To take input from the user
# num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
"""


"""
4.Write a program to find whether a given number is prime or not.
Write a program to find the sum of first n natural numbers using a while loop.
"""

"""

    5.Write a program to find the sum of first n natural
    numbers using a while loop.

"""
#method1:
"""
n = int(input("enter a number: "))
i = 1
sum = 0
while (i <= n):
    sum = sum + i
    i = i + 1
print("The sum is: ", sum)
"""
#Method2:
# Sum of natural numbers up to num
"""
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number")
else:
    sum = 0

    # use while loop to iterate until zero
    while (num > 0):
        sum += num
        num -= 1
    print("The result is", sum)
"""



"""
        6.Write a program to calculate the factorial of a
        given number using for loop.
"""
#method 1
# n!=1 x 2 x 3 x 4 x 5 ....... x n
#  5!=1x2x3x4x5
"""
num=int(input("enter the number: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(f"The factorial of {num} is {factorial}")
"""
#method 2:
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
# num = 7

# To take input from the user
"""
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

"""




"""
            7.Write a program to print the following star pattern.
    *

  ***

*****     for n=3


"""
"""
n=3
for i in range(3):
    print(""  *  (n-i-1), end=" ")
    print("*"   *  (2*i+1), end=" ")
    print("  " * (n-i-1))
"""



"""

8.Write a program to print the following star pattern:
*

**

*** for n = 3

"""
"""

n=4
for i in range(4):
    print("*" * (i+1))
    
"""


"""

9.Write a program to print the following star pattern:
* * *
*   *             #For n=3
* * *

"""
"""
num = int(input("Enter number: "))
for i in range(num):
    for j in range(num):
        if i == num // 2 and j == num // 2:
            print("  ", end="")
        else:
            print("* ", end="")
    print("")

"""
"""
10.Write a program to print the multiplication table of n 
using for loop in reversed order.
"""
"""

MulNumber = int(input("Enter Multiplication Number :\n"))

for i in range(10, 0, -1):
    print(f"{MulNumber} X {i} = {MulNumber*i}")
"""

"""11:pyramid pattern"""
"""

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart(n)
"""


"""12:rograms to print number pattern
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
"""
"""
rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
"""


"""13:
Pyramid pattern of numbers
Let’s see how to print the following half-pyramid pattern of numbers

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Note: In each row, every next number is incremented by 1.
"""
"""
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
"""
"""13:
Inverted pyramid pattern of numbers
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""
"""
rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
"""
"""14:
Inverted Pyramid pattern with the same digit
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
"""
rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
"""
"""16:Another inverted half-pyramid pattern with a number
Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""
"""
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
"""
"""17:Alternate numbers pattern using a while loop
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
"""
"""
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
"""
"""18:Reverse number pattern
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
"""
rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
"""
"""19:Reverse Pyramid of Numbers
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
"""
rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
"""
"""20:
Another reverse number pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
"""
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
"""
"""21:Print reverse number from 10 to 1
1
3 2
6 5 4
10 9 8 7
"""
"""
start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
"""
"""22:
Number triangle pattern
Let’s see how to print the right-angled triangle pattern of numbers

Pattern: –

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
  """
"""
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")

"""
"""23:Pascal’s triangle pattern using numbers
To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a triangular pattern.

Each number is the numbers directly above it added together.

Pattern:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1"""
"""
def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)

"""
"""24:Square pattern with numbers
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
"""
"""
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
"""
"""25:
Multiplication table pattern
Pattern: –

1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
"""
"""
rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
"""
"""26:Simple half pyramid pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
"""
"""
# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")
"""
"""27:Right triangle pyramid of Stars
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
"""
# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")
"""
"""rows = 5
for j in range(1, rows+1):
    print("* " * j)
    """
"""28:Downward half-Pyramid Pattern of Star
Pattern: –

* * * * *  
* * * *  
* * *  
* *  
*
"""
"""
rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
"""
"""
29:Home » Python » Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Updated on: September 8, 2023 | 422 Comments

In this session, I will guide you through the process of effectively printing patterns in Python by using for loop, while loop, and the range() function. By the end of this lesson, you will clearly understand how to print patterns using these techniques. This lesson contains over 35+ patterns.

This article lets you know how to print the following patterns in Python.

Number pattern
Triangle pattern
Star (*) or asterisk pattern
Pyramid pattern
Inverted pyramid pattern
Half pyramid pattern
Diamond Shaped pattern
Characters or alphabets pattern
Square pattern
Print Pattern in Python
Print Pattern in Python
By printing different patterns, you can build a solid understanding of loops in Python. After reading this article, you can create various types of patterns.

Steps to Print Pattern in Python
Use the below steps to print a pattern in Python

Decide the number of rows and columns
There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops to print any pattern, i.e., use nested loops.

The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.

Accept the number of rows from a user using the input() function to decide the size of a pattern.

Iterate rows
Next, write an outer loop to Iterate the number of rows using a for loop and range() function.

Iterate columns
Next, write the inner loop or nested loop to handle the number of columns. The internal loop iteration depends on the values of the outer loop.

Print star or number
Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern (like a star (asterisk *) or number).

Add a new line after each iteration of the outer loop
Add a new line using the print() function after each iteration of the outer loop so that the pattern display appropriately

Algorithm to print pattern in Python
Algorithm to print pattern in Python
Also, Solve:

Python loop exercise
Python Basic Exercise for Beginners
Table of contents
Steps to Print Pattern in Python
Programs to print number pattern
Pyramid pattern of numbers
Inverted pyramid pattern of numbers
Inverted Pyramid pattern with the same digit
Another inverted half-pyramid pattern with a number
Alternate numbers pattern using a while loop
Reverse number pattern
Reverse Pyramid of Numbers
Another reverse number pattern
Print reverse number from 10 to 1
Number triangle pattern
Pascal’s triangle pattern using numbers
Square pattern with numbers
Multiplication table pattern
Pyramid pattern of stars in python
Right triangle pyramid of Stars
Downward half-Pyramid Pattern of Star
Downward full Pyramid Pattern of star
Right down mirror star Pattern
Equilateral triangle pattern of star
Print two pyramids of stars
Right start pattern of star
Left triangle pascal’s pattern
Sandglass pattern of star
Pant style pattern of stars
Diamond-shaped pattern of stars
Another diamond pattern of star
Alphabets and letters pattern
Pattern to display letter of the word
Equilateral triangle pattern of characters/alphabets
Pattern of same character
More miscellaneous Patterns
Pyramid of horizontal number tables
Double the number pattern
Random number pattern
Pyramid of numbers less than 10
Pyramid of numbers up to 10
Even number pattern
Unique pyramid pattern of digits
Pattern double number on each column
Number reduction pattern
Pant style pattern of numbers
Pattern with a combination of numbers and stars
Practice Problem
Next Steps
Programs to print number pattern
I have created various programs that print different styles of number patterns. Let’s see them one by one.

Let’s see the Python program to print the following simple number pattern using a for loop.

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Program:

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
 Run
In this number pattern, we displayed a single digit on the first row, the next two digits on the second row, And the following three numbers on the third row, and this process will repeat till the number of rows is reached.

Note:

The count of numbers on each row is equal to the current row number.
Also, each number is separated by space.
We used a nested loop to print the pattern
Pyramid pattern of numbers
Let’s see how to print the following half-pyramid pattern of numbers

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Note: In each row, every next number is incremented by 1.

Program:

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
 Run
Inverted pyramid pattern of numbers
An inverted pyramid is a downward pattern where numbers get reduced in each iteration, and on the last row, it shows only one number. Use reverse for loop to print this pattern.

Pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Program

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
 Run
Inverted Pyramid pattern with the same digit
Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Program: –

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Another inverted half-pyramid pattern with a number
Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Program

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
 Run
Alternate numbers pattern using a while loop
Let’s see how to use the while loop to print the number pattern.

Pattern: –

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Program: –

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
 Run
Reverse number pattern
Let’s see how to display the pattern of descending order of numbers

Pattern 1: –

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
This pattern is also called as a inverted pyramid of descending numbers.

Program: –

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Reverse Pyramid of Numbers
Pattern 2: –

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
Note: It is a downward increment pattern where numbers get increased in each iteration. At each row, the amount of number is equal to the current row number.

Program

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
 Run
Another reverse number pattern
Pattern: –

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
Program: –

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
 Run
Print reverse number from 10 to 1
Pattern: –

1
3 2
6 5 4
10 9 8 7
Program: –

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
 Run
Number triangle pattern
Let’s see how to print the right-angled triangle pattern of numbers

Pattern: –

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
Program: –

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
 Run
Pascal’s triangle pattern using numbers
To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a triangular pattern.

Each number is the numbers directly above it added together.

Pattern:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
Program: –

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)
 Run
Square pattern with numbers
Pattern: –

1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
Program: –

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
 Run
Multiplication table pattern
Pattern: –

1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
Program: –

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
 Run
Pyramid pattern of stars in python
This section will see how to print pyramid and Star (asterisk) patterns in Python. Here we will print the following pyramid pattern with Star (asterisk).

Half pyramid pattern with stars(*)
Full pyramid pattern with stars
Inverted pyramid Pattern with stars
Triangle pattern with stars
Right-angled triangle pattern with stars
Simple half pyramid pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
This pattern is also known as a right angle triangle pyramid.

Program: –

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")
 Run
Right triangle pyramid of Stars
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
This pattern is also called as mirrored right triangle

Program: –

# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")
 Run
Alternative Solution:

rows = 5
for j in range(1, rows+1):
    print("* " * j)
 Run
Downward half-Pyramid Pattern of Star
Pattern: –

* * * * *  
* * * *  
* * *  
* *  
*
Note: We need to use the reverse nested loop to print the downward pyramid pattern of stars

Program: –

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
 Run
Downward full Pyramid Pattern of star
Let’s see how to print reversed pyramid pattern in Python.

Pattern: –

        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
             """
"""
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

"""
"""30:
Right down mirror star Pattern
Pattern: –

*****
 ****
  ***
   **
    *
    """
"""
rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
"""
"""31.Equilateral triangle pattern of star
Pattern: –

            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  *   
      """
"""
print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
"""
"""32:
Print two pyramids of stars
Pattern: –

*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
"""
"""
rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
"""
"""33:
Right start pattern of star
Pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
"""rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
"""
"""34:Left triangle pascal’s pattern
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
"""
rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
"""
"""35:Sandglass pattern of star
Pattern: –

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
"""
"""rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
"""
"""36:Home » Python » Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Updated on: September 8, 2023 | 422 Comments

In this session, I will guide you through the process of effectively printing patterns in Python by using for loop, while loop, and the range() function. By the end of this lesson, you will clearly understand how to print patterns using these techniques. This lesson contains over 35+ patterns.

This article lets you know how to print the following patterns in Python.

Number pattern
Triangle pattern
Star (*) or asterisk pattern
Pyramid pattern
Inverted pyramid pattern
Half pyramid pattern
Diamond Shaped pattern
Characters or alphabets pattern
Square pattern
Print Pattern in Python
Print Pattern in Python
By printing different patterns, you can build a solid understanding of loops in Python. After reading this article, you can create various types of patterns.

Steps to Print Pattern in Python
Use the below steps to print a pattern in Python

Decide the number of rows and columns
There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops to print any pattern, i.e., use nested loops.

The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.

Accept the number of rows from a user using the input() function to decide the size of a pattern.

Iterate rows
Next, write an outer loop to Iterate the number of rows using a for loop and range() function.

Iterate columns
Next, write the inner loop or nested loop to handle the number of columns. The internal loop iteration depends on the values of the outer loop.

Print star or number
Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern (like a star (asterisk *) or number).

Add a new line after each iteration of the outer loop
Add a new line using the print() function after each iteration of the outer loop so that the pattern display appropriately

Algorithm to print pattern in Python
Algorithm to print pattern in Python
Also, Solve:

Python loop exercise
Python Basic Exercise for Beginners
Table of contents
Steps to Print Pattern in Python
Programs to print number pattern
Pyramid pattern of numbers
Inverted pyramid pattern of numbers
Inverted Pyramid pattern with the same digit
Another inverted half-pyramid pattern with a number
Alternate numbers pattern using a while loop
Reverse number pattern
Reverse Pyramid of Numbers
Another reverse number pattern
Print reverse number from 10 to 1
Number triangle pattern
Pascal’s triangle pattern using numbers
Square pattern with numbers
Multiplication table pattern
Pyramid pattern of stars in python
Right triangle pyramid of Stars
Downward half-Pyramid Pattern of Star
Downward full Pyramid Pattern of star
Right down mirror star Pattern
Equilateral triangle pattern of star
Print two pyramids of stars
Right start pattern of star
Left triangle pascal’s pattern
Sandglass pattern of star
Pant style pattern of stars
Diamond-shaped pattern of stars
Another diamond pattern of star
Alphabets and letters pattern
Pattern to display letter of the word
Equilateral triangle pattern of characters/alphabets
Pattern of same character
More miscellaneous Patterns
Pyramid of horizontal number tables
Double the number pattern
Random number pattern
Pyramid of numbers less than 10
Pyramid of numbers up to 10
Even number pattern
Unique pyramid pattern of digits
Pattern double number on each column
Number reduction pattern
Pant style pattern of numbers
Pattern with a combination of numbers and stars
Practice Problem
Next Steps
Programs to print number pattern
I have created various programs that print different styles of number patterns. Let’s see them one by one.

Let’s see the Python program to print the following simple number pattern using a for loop.

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Program:

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
 Run
In this number pattern, we displayed a single digit on the first row, the next two digits on the second row, And the following three numbers on the third row, and this process will repeat till the number of rows is reached.

Note:

The count of numbers on each row is equal to the current row number.
Also, each number is separated by space.
We used a nested loop to print the pattern
Pyramid pattern of numbers
Let’s see how to print the following half-pyramid pattern of numbers

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Note: In each row, every next number is incremented by 1.

Program:

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
 Run
Inverted pyramid pattern of numbers
An inverted pyramid is a downward pattern where numbers get reduced in each iteration, and on the last row, it shows only one number. Use reverse for loop to print this pattern.

Pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Program

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
 Run
Inverted Pyramid pattern with the same digit
Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Program: –

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Another inverted half-pyramid pattern with a number
Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Program

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
 Run
Alternate numbers pattern using a while loop
Let’s see how to use the while loop to print the number pattern.

Pattern: –

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Program: –

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
 Run
Reverse number pattern
Let’s see how to display the pattern of descending order of numbers

Pattern 1: –

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
This pattern is also called as a inverted pyramid of descending numbers.

Program: –

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Reverse Pyramid of Numbers
Pattern 2: –

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
Note: It is a downward increment pattern where numbers get increased in each iteration. At each row, the amount of number is equal to the current row number.

Program

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
 Run
Another reverse number pattern
Pattern: –

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
Program: –

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
 Run
Print reverse number from 10 to 1
Pattern: –

1
3 2
6 5 4
10 9 8 7
Program: –

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
 Run
Number triangle pattern
Let’s see how to print the right-angled triangle pattern of numbers

Pattern: –

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
Program: –

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
 Run
Pascal’s triangle pattern using numbers
To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a triangular pattern.

Each number is the numbers directly above it added together.

Pattern:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
Program: –

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)
 Run
Square pattern with numbers
Pattern: –

1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
Program: –

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
 Run
Multiplication table pattern
Pattern: –

1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
Program: –

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
 Run
Pyramid pattern of stars in python
This section will see how to print pyramid and Star (asterisk) patterns in Python. Here we will print the following pyramid pattern with Star (asterisk).

Half pyramid pattern with stars(*)
Full pyramid pattern with stars
Inverted pyramid Pattern with stars
Triangle pattern with stars
Right-angled triangle pattern with stars
Simple half pyramid pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
This pattern is also known as a right angle triangle pyramid.

Program: –

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")
 Run
Right triangle pyramid of Stars
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
This pattern is also called as mirrored right triangle

Program: –

# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")
 Run
Alternative Solution:

rows = 5
for j in range(1, rows+1):
    print("* " * j)
 Run
Downward half-Pyramid Pattern of Star
Pattern: –

* * * * *  
* * * *  
* * *  
* *  
*
Note: We need to use the reverse nested loop to print the downward pyramid pattern of stars

Program: –

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
 Run
Downward full Pyramid Pattern of star
Let’s see how to print reversed pyramid pattern in Python.

Pattern: –

        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
Program:

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
 Run
Right down mirror star Pattern
Pattern: –

*****
 ****
  ***
   **
    *
In this pattern, we need to use two nested while loops.

Program: –

rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
 Run
Equilateral triangle pattern of star
Pattern: –

            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  *   
Program: –

print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
 Run
Print two pyramids of stars
Pattern: –

*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
Program: –

rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
 Run
Right start pattern of star
Pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
We also call this pattern as a right pascal’s triangle.

Program: –

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
 Run
Left triangle pascal’s pattern
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
Program: –

rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
 Run
Sandglass pattern of star
Pattern: –

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
To print this pattern we need to use two set of three while loops.

Program: –

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
 Run
Pant style pattern of stars
Pattern: –

****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
"""
"""
rows = 14
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2
        """
"""36:
Diamond-shaped pattern of stars
Pattern: –

        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        """
"""
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    """
"""37:Another diamond pattern of star
Pattern: –

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
"""
rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1
"""
"""
38:Home » Python » Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Updated on: September 8, 2023 | 422 Comments

In this session, I will guide you through the process of effectively printing patterns in Python by using for loop, while loop, and the range() function. By the end of this lesson, you will clearly understand how to print patterns using these techniques. This lesson contains over 35+ patterns.

This article lets you know how to print the following patterns in Python.

Number pattern
Triangle pattern
Star (*) or asterisk pattern
Pyramid pattern
Inverted pyramid pattern
Half pyramid pattern
Diamond Shaped pattern
Characters or alphabets pattern
Square pattern
Print Pattern in Python
Print Pattern in Python
By printing different patterns, you can build a solid understanding of loops in Python. After reading this article, you can create various types of patterns.

Steps to Print Pattern in Python
Use the below steps to print a pattern in Python

Decide the number of rows and columns
There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops to print any pattern, i.e., use nested loops.

The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.

Accept the number of rows from a user using the input() function to decide the size of a pattern.

Iterate rows
Next, write an outer loop to Iterate the number of rows using a for loop and range() function.

Iterate columns
Next, write the inner loop or nested loop to handle the number of columns. The internal loop iteration depends on the values of the outer loop.

Print star or number
Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern (like a star (asterisk *) or number).

Add a new line after each iteration of the outer loop
Add a new line using the print() function after each iteration of the outer loop so that the pattern display appropriately

Algorithm to print pattern in Python
Algorithm to print pattern in Python
Also, Solve:

Python loop exercise
Python Basic Exercise for Beginners
Table of contents
Steps to Print Pattern in Python
Programs to print number pattern
Pyramid pattern of numbers
Inverted pyramid pattern of numbers
Inverted Pyramid pattern with the same digit
Another inverted half-pyramid pattern with a number
Alternate numbers pattern using a while loop
Reverse number pattern
Reverse Pyramid of Numbers
Another reverse number pattern
Print reverse number from 10 to 1
Number triangle pattern
Pascal’s triangle pattern using numbers
Square pattern with numbers
Multiplication table pattern
Pyramid pattern of stars in python
Right triangle pyramid of Stars
Downward half-Pyramid Pattern of Star
Downward full Pyramid Pattern of star
Right down mirror star Pattern
Equilateral triangle pattern of star
Print two pyramids of stars
Right start pattern of star
Left triangle pascal’s pattern
Sandglass pattern of star
Pant style pattern of stars
Diamond-shaped pattern of stars
Another diamond pattern of star
Alphabets and letters pattern
Pattern to display letter of the word
Equilateral triangle pattern of characters/alphabets
Pattern of same character
More miscellaneous Patterns
Pyramid of horizontal number tables
Double the number pattern
Random number pattern
Pyramid of numbers less than 10
Pyramid of numbers up to 10
Even number pattern
Unique pyramid pattern of digits
Pattern double number on each column
Number reduction pattern
Pant style pattern of numbers
Pattern with a combination of numbers and stars
Practice Problem
Next Steps
Programs to print number pattern
I have created various programs that print different styles of number patterns. Let’s see them one by one.

Let’s see the Python program to print the following simple number pattern using a for loop.

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Program:

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
 Run
In this number pattern, we displayed a single digit on the first row, the next two digits on the second row, And the following three numbers on the third row, and this process will repeat till the number of rows is reached.

Note:

The count of numbers on each row is equal to the current row number.
Also, each number is separated by space.
We used a nested loop to print the pattern
Pyramid pattern of numbers
Let’s see how to print the following half-pyramid pattern of numbers

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Note: In each row, every next number is incremented by 1.

Program:

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
 Run
Inverted pyramid pattern of numbers
An inverted pyramid is a downward pattern where numbers get reduced in each iteration, and on the last row, it shows only one number. Use reverse for loop to print this pattern.

Pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Program

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
 Run
Inverted Pyramid pattern with the same digit
Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Program: –

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Another inverted half-pyramid pattern with a number
Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Program

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
 Run
Alternate numbers pattern using a while loop
Let’s see how to use the while loop to print the number pattern.

Pattern: –

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Program: –

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
 Run
Reverse number pattern
Let’s see how to display the pattern of descending order of numbers

Pattern 1: –

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
This pattern is also called as a inverted pyramid of descending numbers.

Program: –

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Reverse Pyramid of Numbers
Pattern 2: –

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
Note: It is a downward increment pattern where numbers get increased in each iteration. At each row, the amount of number is equal to the current row number.

Program

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
 Run
Another reverse number pattern
Pattern: –

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
Program: –

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
 Run
Print reverse number from 10 to 1
Pattern: –

1
3 2
6 5 4
10 9 8 7
Program: –

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
 Run
Number triangle pattern
Let’s see how to print the right-angled triangle pattern of numbers

Pattern: –

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
Program: –

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
 Run
Pascal’s triangle pattern using numbers
To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a triangular pattern.

Each number is the numbers directly above it added together.

Pattern:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
Program: –

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)
 Run
Square pattern with numbers
Pattern: –

1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
Program: –

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
 Run
Multiplication table pattern
Pattern: –

1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
Program: –

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
 Run
Pyramid pattern of stars in python
This section will see how to print pyramid and Star (asterisk) patterns in Python. Here we will print the following pyramid pattern with Star (asterisk).

Half pyramid pattern with stars(*)
Full pyramid pattern with stars
Inverted pyramid Pattern with stars
Triangle pattern with stars
Right-angled triangle pattern with stars
Simple half pyramid pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
This pattern is also known as a right angle triangle pyramid.

Program: –

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")
 Run
Right triangle pyramid of Stars
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
This pattern is also called as mirrored right triangle

Program: –

# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")
 Run
Alternative Solution:

rows = 5
for j in range(1, rows+1):
    print("* " * j)
 Run
Downward half-Pyramid Pattern of Star
Pattern: –

* * * * *  
* * * *  
* * *  
* *  
*
Note: We need to use the reverse nested loop to print the downward pyramid pattern of stars

Program: –

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
 Run
Downward full Pyramid Pattern of star
Let’s see how to print reversed pyramid pattern in Python.

Pattern: –

        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
Program:

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
 Run
Right down mirror star Pattern
Pattern: –

*****
 ****
  ***
   **
    *
In this pattern, we need to use two nested while loops.

Program: –

rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
 Run
Equilateral triangle pattern of star
Pattern: –

            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  *   
Program: –

print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
 Run
Print two pyramids of stars
Pattern: –

*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
Program: –

rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
 Run
Right start pattern of star
Pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
We also call this pattern as a right pascal’s triangle.

Program: –

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
 Run
Left triangle pascal’s pattern
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
Program: –

rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
 Run
Sandglass pattern of star
Pattern: –

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
To print this pattern we need to use two set of three while loops.

Program: –

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
 Run
Pant style pattern of stars
Pattern: –

****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
Program: –

rows = 14
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2
 Run
Diamond-shaped pattern of stars
Pattern: –

        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
Program: –

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
 Run
Another diamond pattern of star
Pattern: –

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
Program: –

rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1
 Run
Alphabets and letters pattern
In Python, there are ASCII values for each letter. To print the patterns of letters and alphabets, we need to convert them to their ASCII values.

Decide the number of rows
Start with ASCII number 65 ( ‘A’)
Iterate a loop and in nested for loop use the char function to convert ASCII number to its equivalent letter.
Let’ see now how to print alphabets and letters patterns in Python.

Pattern: –

A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \ 
This pattern is knows as right-angled pattern with characters.

Program: –

# ASCII number of 'A'
ascii_number = 65
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")"""
"""39:Pattern to display letter of the word
Let’s see how to print word ‘Python’ in Pattern: –

P
Py
Pyt
Pyth
Pytho
Python
Program: –

word = "Python"
x = ""
for i in word:
    x += i
    print(x)"""
"""40:
Equilateral triangle pattern of characters/alphabets
Pattern: –

            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \  
Program: –

print("Print equilateral triangle Pyramid with characters ")
size = 7
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")"""
"""41:Pattern of same character
Pattern: –

V 
V V 
V V V 
V V V V 
V V V V V 
Program: –

# Same character pattern
character = 'V'
# convert char to ASCII
char_ascii_no = ord(character)
for i in range(0, 5):
    for j in range(0, i + 1):
        # Convert the ASCII value to the character
        user_char = chr(char_ascii_no)
        print(user_char, end=' ')
    print()"""
"""42:Pyramid of horizontal number tables
Pattern: –

1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
Program: –

# Pyramid of horizontal tables of numbers
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()"""
"""43:Double the number pattern
Pattern: –

   1 
   2    1 
   4    2    1 
   8    4    2    1 
  16    8    4    2    1 
  32   16    8    4    2    1 
  64   32   16    8    4    2    1 
 128   64   32   16    8    4    2    1 
Note: In each column, every number is double it’s the preceding number.

Program: –

rows = 9
for i in range(1, rows):
    for j in range(-1 + i, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    print("")"""
"""44:Random number pattern
   1 
   1    2    1 
   1    2    4    2    1 
   1    2    4    8    4    2    1 
   1    2    4    8   16    8    4    2    1 
   1    2    4    8   16   32   16    8    4    2    1 
   1    2    4    8   16   32   64   32   16    8    4    2    1 
   1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 
Program: –

rows = 9
for i in range(1, rows):
    for i in range(0, i, 1):
        print(format(2 ** i, "4d"), end=' ')
    for i in range(-1 + i, -1, -1):
        print(format(2 ** i, "4d"), end=' ')
    print("")"""
"""44:Pyramid of numbers less than 10
Pattern: –

1 
2 3 4 
5 6 7 8 9
Program: –

current_num = 1
stop = 2
rows = 3

for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 2"""
"""45:Pyramid of numbers up to 10
Pattern: –

1 
2 3 
4 5 6 
7 8 9 10
Program: –

current_num = 1
rows = 4
stop = 2
for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 1"""
"""46:Even number pattern
Pattern: –

10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
Programs: –

rows = 5
last_num = 2 * rows
even_num = last_num
for i in range(1, rows + 1):
    even_num = last_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print("\r")"""
"""47:
Unique pyramid pattern of digits
Pattern: –

1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
Program: –

rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()"""
"""48:Pattern double number on each column
Pattern: –

0  
0  1  
0  2  4  
0  3  6   9  
0  4  8   12  16  
0  5  10  15  20  25  
0  6  12  18  24  30  36
Program: –

rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        print(i * j, end='  ')
    print()"""
"""49:
Number reduction pattern
Pattern: –

1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5
Program: –

rows = 5
for i in range(0, rows + 1, 1):
    for j in range(i + 1, rows + 1, 1):
        print(j, end=' ')
    print()"""
"""49:Pant style pattern of numbers
Pattern: –

5 4 3 2 1 1 2 3 4 5 

5 4 3 2     2 3 4 5 

5 4 3         3 4 5 

5 4             4 5 

5                 5
Program: –

rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')"""
"""50:Home » Python » Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Python Programs to Print Pattern – Print Number, Pyramid, Star, Triangle, Diamond, and Alphabets Patterns
Updated on: September 8, 2023 | 422 Comments

In this session, I will guide you through the process of effectively printing patterns in Python by using for loop, while loop, and the range() function. By the end of this lesson, you will clearly understand how to print patterns using these techniques. This lesson contains over 35+ patterns.

This article lets you know how to print the following patterns in Python.

Number pattern
Triangle pattern
Star (*) or asterisk pattern
Pyramid pattern
Inverted pyramid pattern
Half pyramid pattern
Diamond Shaped pattern
Characters or alphabets pattern
Square pattern
Print Pattern in Python
Print Pattern in Python
By printing different patterns, you can build a solid understanding of loops in Python. After reading this article, you can create various types of patterns.

Steps to Print Pattern in Python
Use the below steps to print a pattern in Python

Decide the number of rows and columns
There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops to print any pattern, i.e., use nested loops.

The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.

Accept the number of rows from a user using the input() function to decide the size of a pattern.

Iterate rows
Next, write an outer loop to Iterate the number of rows using a for loop and range() function.

Iterate columns
Next, write the inner loop or nested loop to handle the number of columns. The internal loop iteration depends on the values of the outer loop.

Print star or number
Use the print() function in each iteration of nested for loop to display the symbol or number of a pattern (like a star (asterisk *) or number).

Add a new line after each iteration of the outer loop
Add a new line using the print() function after each iteration of the outer loop so that the pattern display appropriately

Algorithm to print pattern in Python
Algorithm to print pattern in Python
Also, Solve:

Python loop exercise
Python Basic Exercise for Beginners
Table of contents
Steps to Print Pattern in Python
Programs to print number pattern
Pyramid pattern of numbers
Inverted pyramid pattern of numbers
Inverted Pyramid pattern with the same digit
Another inverted half-pyramid pattern with a number
Alternate numbers pattern using a while loop
Reverse number pattern
Reverse Pyramid of Numbers
Another reverse number pattern
Print reverse number from 10 to 1
Number triangle pattern
Pascal’s triangle pattern using numbers
Square pattern with numbers
Multiplication table pattern
Pyramid pattern of stars in python
Right triangle pyramid of Stars
Downward half-Pyramid Pattern of Star
Downward full Pyramid Pattern of star
Right down mirror star Pattern
Equilateral triangle pattern of star
Print two pyramids of stars
Right start pattern of star
Left triangle pascal’s pattern
Sandglass pattern of star
Pant style pattern of stars
Diamond-shaped pattern of stars
Another diamond pattern of star
Alphabets and letters pattern
Pattern to display letter of the word
Equilateral triangle pattern of characters/alphabets
Pattern of same character
More miscellaneous Patterns
Pyramid of horizontal number tables
Double the number pattern
Random number pattern
Pyramid of numbers less than 10
Pyramid of numbers up to 10
Even number pattern
Unique pyramid pattern of digits
Pattern double number on each column
Number reduction pattern
Pant style pattern of numbers
Pattern with a combination of numbers and stars
Practice Problem
Next Steps
Programs to print number pattern
I have created various programs that print different styles of number patterns. Let’s see them one by one.

Let’s see the Python program to print the following simple number pattern using a for loop.

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Program:

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
 Run
In this number pattern, we displayed a single digit on the first row, the next two digits on the second row, And the following three numbers on the third row, and this process will repeat till the number of rows is reached.

Note:

The count of numbers on each row is equal to the current row number.
Also, each number is separated by space.
We used a nested loop to print the pattern
Pyramid pattern of numbers
Let’s see how to print the following half-pyramid pattern of numbers

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Note: In each row, every next number is incremented by 1.

Program:

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
 Run
Inverted pyramid pattern of numbers
An inverted pyramid is a downward pattern where numbers get reduced in each iteration, and on the last row, it shows only one number. Use reverse for loop to print this pattern.

Pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Program

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
 Run
Inverted Pyramid pattern with the same digit
Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Program: –

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Another inverted half-pyramid pattern with a number
Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Program

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
 Run
Alternate numbers pattern using a while loop
Let’s see how to use the while loop to print the number pattern.

Pattern: –

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Program: –

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
 Run
Reverse number pattern
Let’s see how to display the pattern of descending order of numbers

Pattern 1: –

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
This pattern is also called as a inverted pyramid of descending numbers.

Program: –

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 Run
Reverse Pyramid of Numbers
Pattern 2: –

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
Note: It is a downward increment pattern where numbers get increased in each iteration. At each row, the amount of number is equal to the current row number.

Program

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
 Run
Another reverse number pattern
Pattern: –

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
Program: –

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
 Run
Print reverse number from 10 to 1
Pattern: –

1
3 2
6 5 4
10 9 8 7
Program: –

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
 Run
Number triangle pattern
Let’s see how to print the right-angled triangle pattern of numbers

Pattern: –

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
Program: –

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
 Run
Pascal’s triangle pattern using numbers
To build the pascal triangle, start with “1” at the top, then continue placing numbers below it in a triangular pattern.

Each number is the numbers directly above it added together.

Pattern:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
Program: –

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)
 Run
Square pattern with numbers
Pattern: –

1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
Program: –

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
 Run
Multiplication table pattern
Pattern: –

1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
Program: –

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
 Run
Pyramid pattern of stars in python
This section will see how to print pyramid and Star (asterisk) patterns in Python. Here we will print the following pyramid pattern with Star (asterisk).

Half pyramid pattern with stars(*)
Full pyramid pattern with stars
Inverted pyramid Pattern with stars
Triangle pattern with stars
Right-angled triangle pattern with stars
Simple half pyramid pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
This pattern is also known as a right angle triangle pyramid.

Program: –

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")
 Run
Right triangle pyramid of Stars
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
This pattern is also called as mirrored right triangle

Program: –

# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")
 Run
Alternative Solution:

rows = 5
for j in range(1, rows+1):
    print("* " * j)
 Run
Downward half-Pyramid Pattern of Star
Pattern: –

* * * * *  
* * * *  
* * *  
* *  
*
Note: We need to use the reverse nested loop to print the downward pyramid pattern of stars

Program: –

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
 Run
Downward full Pyramid Pattern of star
Let’s see how to print reversed pyramid pattern in Python.

Pattern: –

        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
Program:

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
 Run
Right down mirror star Pattern
Pattern: –

*****
 ****
  ***
   **
    *
In this pattern, we need to use two nested while loops.

Program: –

rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1
 Run
Equilateral triangle pattern of star
Pattern: –

            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  *   
Program: –

print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
 Run
Print two pyramids of stars
Pattern: –

*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
Program: –

rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
 Run
Right start pattern of star
Pattern: –

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
We also call this pattern as a right pascal’s triangle.

Program: –

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
 Run
Left triangle pascal’s pattern
Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
Program: –

rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
 Run
Sandglass pattern of star
Pattern: –

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
To print this pattern we need to use two set of three while loops.

Program: –

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1
 Run
Pant style pattern of stars
Pattern: –

****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
Program: –

rows = 14
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2
 Run
Diamond-shaped pattern of stars
Pattern: –

        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
Program: –

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
 Run
Another diamond pattern of star
Pattern: –

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
Program: –

rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1
 Run
Alphabets and letters pattern
In Python, there are ASCII values for each letter. To print the patterns of letters and alphabets, we need to convert them to their ASCII values.

Decide the number of rows
Start with ASCII number 65 ( ‘A’)
Iterate a loop and in nested for loop use the char function to convert ASCII number to its equivalent letter.
Let’ see now how to print alphabets and letters patterns in Python.

Pattern: –

A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \ 
This pattern is knows as right-angled pattern with characters.

Program: –

# ASCII number of 'A'
ascii_number = 65
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")
 Run
Pattern to display letter of the word
Let’s see how to print word ‘Python’ in Pattern: –

P
Py
Pyt
Pyth
Pytho
Python
Program: –

word = "Python"
x = ""
for i in word:
    x += i
    print(x)
 Run
Equilateral triangle pattern of characters/alphabets
Pattern: –

            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \  
Program: –

print("Print equilateral triangle Pyramid with characters ")
size = 7
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")
 Run
Pattern of same character
Pattern: –

V 
V V 
V V V 
V V V V 
V V V V V 
Program: –

# Same character pattern
character = 'V'
# convert char to ASCII
char_ascii_no = ord(character)
for i in range(0, 5):
    for j in range(0, i + 1):
        # Convert the ASCII value to the character
        user_char = chr(char_ascii_no)
        print(user_char, end=' ')
    print()
 Run
Let’s see some more miscellaneous patterns

More miscellaneous Patterns
Pyramid of horizontal number tables
Pattern: –

1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
Program: –

# Pyramid of horizontal tables of numbers
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()
 Run
Double the number pattern
Pattern: –

   1 
   2    1 
   4    2    1 
   8    4    2    1 
  16    8    4    2    1 
  32   16    8    4    2    1 
  64   32   16    8    4    2    1 
 128   64   32   16    8    4    2    1 
Note: In each column, every number is double it’s the preceding number.

Program: –

rows = 9
for i in range(1, rows):
    for j in range(-1 + i, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    print("")
 Run
Random number pattern
   1 
   1    2    1 
   1    2    4    2    1 
   1    2    4    8    4    2    1 
   1    2    4    8   16    8    4    2    1 
   1    2    4    8   16   32   16    8    4    2    1 
   1    2    4    8   16   32   64   32   16    8    4    2    1 
   1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 
Program: –

rows = 9
for i in range(1, rows):
    for i in range(0, i, 1):
        print(format(2 ** i, "4d"), end=' ')
    for i in range(-1 + i, -1, -1):
        print(format(2 ** i, "4d"), end=' ')
    print("")
 Run
Pyramid of numbers less than 10
Pattern: –

1 
2 3 4 
5 6 7 8 9
Program: –

current_num = 1
stop = 2
rows = 3

for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 2
 Run
Pyramid of numbers up to 10
Pattern: –

1 
2 3 
4 5 6 
7 8 9 10
Program: –

current_num = 1
rows = 4
stop = 2
for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 1
 Run
Even number pattern
Pattern: –

10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2
Programs: –

rows = 5
last_num = 2 * rows
even_num = last_num
for i in range(1, rows + 1):
    even_num = last_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print("\r")
 Run
Unique pyramid pattern of digits
Pattern: –

1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
Program: –

rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
 Run
Pattern double number on each column
Pattern: –

0  
0  1  
0  2  4  
0  3  6   9  
0  4  8   12  16  
0  5  10  15  20  25  
0  6  12  18  24  30  36
Program: –

rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        print(i * j, end='  ')
    print()
 Run
Number reduction pattern
Pattern: –

1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5
Program: –

rows = 5
for i in range(0, rows + 1, 1):
    for j in range(i + 1, rows + 1, 1):
        print(j, end=' ')
    print()
 Run
Pant style pattern of numbers
Pattern: –

5 4 3 2 1 1 2 3 4 5 

5 4 3 2     2 3 4 5 

5 4 3         3 4 5 

5 4             4 5 

5                 5
Program: –

rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')
 Run
Pattern with a combination of numbers and stars
Pattern: –

1 * 2 * 3 * 4 

1 * 2 * 3 

1 * 2 

1
Program: –

row = 4
for i in range(0, row):
    c = 1
    print(c, end=' ')
    for j in range(row - i - 1, 0, -1):
        print('*', end=' ')
        c = c + 1
        print(c, end=' ')
    print('\n')"""
"""51:Practice Problem
Pattern: –

0 
2 4 
4 8 8 
8 16 16 16
Solution: –

num = 4
counter = 0
for x in range(0, num):
    for y in range(0, x + 1):
        print(counter, end=" ")
        counter = 2 ** (x + 1)
    print()"""

