"""

1. Write a python script to display the number of days in a given month number.
2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement
7. Write a python program to check whether a given number is positive, negative or
zero using match case statement
8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday

"""
#1
"""
month = int(input("Enter a month number"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif  month in (4,6,9,11):
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("invalid month")
    
"""

#2
"""
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
x = int(input("Enter your choice"))
a,b=int(input("Enter 1st number")),int(input("Enter 2nd number"))
match x:
    case 1 :
        print(a+b)
    case 2 :
        print(a-b)
    case 3 :
        print(a*b)
    case 4 :
        print(a/b)
    case _ :
        print("invalid")
    
    

"""
#3
"""
print("1. Check whether a given set of three numbers are lengths of an isosceles triangle or not")
print("2. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("3. Check whether a given set of three numbers are equilateral triangle or not")
print("4. Exit.")
x = int(input("Enter your choice")) 
if x not in (1,2,3,4):
    print("invalid choice")
elif x==4:
    exit()
else:
    a,b,c=int(input("Enter 1st number")),int(input("Enter 2nd number")),int(input("Enter 3rd number"))
match x:    
    case 1 :
        if a==b or b==c or c==a:
            print("isosceles triangle")
        else:
            print("not an isosceles triangle")
    case 2 :
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("right angled triangle")
        else:
            print("not a right angled triangle")
    case 3 :
        if a==b==c:
            print("equilateral triangle")
        else:
            print("not an equilateral triangle")
    case _ :
        print("invalid choice")
"""

#4
"""
x = int(input("Enter age "))
match x:
    case x if x<10:
              print("you are a kid")
    case x if x>=10 and x<20:
               print("you are a teen")
    case x if x>=20 and x<40:
               print("you are young")
    case x if x<60 and x>=40:
               print("you are experienced")
    case x if x>=60:
                print("you are an senior citizen")
    case _ :
                print("invalid")
"""
#5 
'''Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
 '''
"""
num = int(input("enter a number"))
if num % 2 == 0:
    print("Saurabh Shukla")
elif num > 0:
    print("Aditya Choudhary")
else:
    print("Prateek Jain")
"""

#6 
'''
Write a python program to check whether a given string is a multiword string or single
word string using match case statement

'''
"""
s = input(" enter a string : ")
match s:
    case s if ' ' in s:
        print("Multiword string")
    case s if ' ' not in s:
        print("Single Word string")

"""       
#7
'''
Write a python program to check whether a given number is positive, negative or
zero using match case statement
'''
"""
num = int(input("Enter a number : "))
match num:
    case num if num>0:
        print("Positive")
    case num if num<0:
        print("negative")
    case num if num == 0:
        print("Zero")

"""

#8
'''
Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
'''
"""
s1= input("Enter 1st string")
s2= input("Enter 2st string")
match(s1,s2):
    case (s1,s2) if s1==s2:
        print("identical")
    case(s1,s2) if s1<s2:
        print("{} comes before {}".format(s1,s2))
    case(s1,s2) if s1>s2:
        print("{} comes before {}".format(s2,s1))

"""
#9
'''
Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
'''
"""
year = int(input(" Enter a year"))
if year%100 == 0:
    if year%400 == 0:
        print("Century leap year")
    else:
        print("century non-leap year")
elif year%4 == 0:
    print("Non-century leap year")
else:
    print("Non-century non leap year")
"""
#output:
'''
 Enter a year2000
Century leap year
Enter a year2016
Non-century leap year
Enter a year1999
Non-century non leap year
Enter a year1700
century non-leap year
'''
#10.
'''
Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
'''

"""
s1 = input(" what's your favorite colour?").lower()          
l1 = ["yellow","blue","orange","white","black","red"]
for colour in l1:
    if colour in s1:
        c=colour
        break
    else:
        c="other"
match c :
    case "yellow" :
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case other:
        print("Sunday")
"""