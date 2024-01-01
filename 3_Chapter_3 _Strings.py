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

