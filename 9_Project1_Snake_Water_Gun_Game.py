"""
Project 1: Snake, Water, Gun Game
We all have played snake, water gun game in our childhood.
If you haven’t, google the rules of this game
and write a Python program capable of playing this game with the user.
"""
import random
#snake water gun or rock paper scissors
def gameWin(comp,you):
#if two values are equal,decalre a tie!
    if comp==you:
      return None
#check for all possibilities when computer chose snake
    elif comp == 's':
     if you=='w':
        return False
    elif you=='g':
        return True
    #check for all possibilities when computer chose water
    elif comp =='w':
        if you=='g':
            return False
        elif you=='s':
            return True
        #check for all possibilities when computer chose gun
        elif comp =='g':
            if you=='s':
                return False
            elif you=='w':
                return True
print("comp turn:snake(s) water(w) or gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
 comp='s'
elif randNo==2:
 comp='w'
elif randNo==3:
 comp='g'
you=input("your turn:snake(s) water(w) or gun(g)?")
a=gameWin(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")
if a==None:
     print("the game is tie!")
elif a:
    print("you win!")
else:print("you lose!")