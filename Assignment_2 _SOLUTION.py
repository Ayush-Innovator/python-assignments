'''Assignment-2: Python Basics

1. Write a python script to add comments and print “Learning Python” on screen.
2. Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values.
3. Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
4. Write a python script to print the id of two variables containing the same integer
values.
5. Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable
6. Write a python script to print all the keywords
7. On Python shell use help() function and display the list of keywords
8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py
9. Name the keywords, used as data in the Python script.
10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)'''

##########################################"""Solution"""

#1 Write a python script to add comments and print “Learning Python” on screen.
"""print("Learning Python")"""
#2 Write a python script to add multi line comments and print values of four variables,
#each in a new line. Variable contains any values.
"""
a="Mahakaal"
b=33
c=2*3
d="God's child"
print(a,b,c,d,sep='\n')

#print(a.strip(), b.strip(), c.strip(), d.strip(), sep='\n')
⚡ Pro tip
sep='\n' → automatically puts each value on a new line
.strip() → removes unwanted spaces from start/end

"""
#3 Write a python script to print types of variables. Create 5 variables each of them
#containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
"""
a=33
b="Hey Keshav"
c=11.15
d=3+4j
e=11*3
print('\n',"type of a is:",type(a),'\n',"type of b is:",type(b),'\n',"type of c is:",type(c),'\n',"type of d is:",type(d),'\n',"type is:",type(a==c),'\n',)

"""
#4 Write a python script to print the id of two variables containing the same integer
#values.
"""
a=44
r=44
print(id(a),id(r),sep='\n')
print("same id=",id(a)==id(r))

"""

#5
"""
a=33
b="Hey Keshav"
c=11.15
d=3+4j
#print('\n','a=',a,"type of a is",type(a),"id of a=",id(a),'\n','b=',b,"type of b is",type(b),"id of b=",id(b),'\n','c=',c,"type of c is",type(c),"id of c=",id(c),'\n','d=',d,"type of d is",type(d),"id of d=",id(d))
print("value,type,id of a are as :",a,type(a),id(a),sep='  ')
print("value,type,id of b are as :",b,type(b),id(b),sep='  ')
print("value,type,id of c are as :",c,type(c),id(c),sep='  ')
print("value,type,id of d are as :",d,type(d),id(d),sep='  ')
"""

#6
"""
import keyword
print(keyword.kwlist)
"""
#7
#keyword.kwlist


#8
"""
from A1 import a
print(a)

"""
#9 Name the keywords, used as data in the Python script.
##Answer :
"""
True
False
None
"""

#10

"""
from datetime import datetime

now = datetime.now()

date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")

print("Date:", date)
print("Time:", time)
"""


"""
##Samajh lo (important for exams/interview)
##datetime.now() → current date + time deta hai
##strftime() → format change karta hai
##Format codes:
##%d → day (13)
##%m → month (08)
##%Y → year (2022)
##%I → hour (12-hour format)
##%M → minutes
##%p → AM/PM
"""

#coding
"""

from datetime import datetime

# current date and time store karna
now = datetime.now()

# date aur time alag variables me
current_date = now.strftime("%d-%m-%Y")
current_time = now.strftime("%I:%M %p")

# display
print("Date:", current_date)
print("Time:", current_time)
"""
