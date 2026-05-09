"""

Assignment - 6 Full Stack Web Development using Python MySirG

Decision Control

1. Write a python script to check whether a given number is positive or non-positive
2. Write a python script to check whether a given number is divisible by 5 or not
3. Write a python script to check whether a given number is even or odd
4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
5. Write a python script to print two given words in dictionary order
6. Write a python script to check whether a given number is a three digit number or not.
7. Write a python script to check whether a given number is positive, negative or zero.
8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
9. Write a python script to check whether a given year is a leap year or not.
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
11. Write a python script to take the month value in numeric format and display the
number of days in it.
12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
"""
#1
#M-1 if if
"""
x=int(input("Enter a number"))
if x>0:
    print("enter number is positive")
if x<=0:
    print("enter number is non-positive")
"""     
#M-2 if-else
'''
x=int(input("Enter a number"))
if x<=0:
    print("non-positive") 

else:
    print("positive")
'''
#M-3 if-elif-else
"""
a=int(input("Enter a number"))
if a>0:
    print("positive")

elif a<0:
    print("negative")

else:
    print("neither positive nor negative, it's zero")
"""
#M-4 single line if else, it is an expression.
"""

a=int(input("Enter a number"))
x="positive " if a>0 else "non-negative"
print(x)

"""

#2
"""
x=int(input("Enter a number"))
if x%5==0:
    print("d")
else:
    print("nd")
"""
#3
"""
x=int(input("Enter a number"))
print("even"if x%2==0 else "odd")

"""
#4
"""
x=int(input("Enter a number"))
y=int(input("Enter a number"))
print(x if x >= y else y)
"""
#5
"""
x=input("Enter a words")
y=input("Enter a words")
print(x,y if x < y else y,x)

"""
#6
"""
x=int(input("Enter a number"))
if x>99 and x <1000:
    print("Entered no is 3 digit no.")
elif x>-1000 and x<-99:
    print("Entered no is 3 digit no.")
else:
    print("invalid no.")
"""

#7
"""
x=int(input("Enter a number"))
if x>0:
    print("enter no. is positive")
elif x == 0:
    print("enter no. is zero")
else:
    print("enter no is negative")
    
"""

#8
"""
print("Enter the value of coefficient of quadratic equation, i.e a,b,c in ax^2+bx+c")
a,b,c = int(input()),int(input()),int(input())
d=b*b - 4*a*c
if d>0:
    print("real and different roots")
elif d==0:
    print("real and equal roots")
else :
    print("imaginary roots")
"""


#9
"""
x=int(input("Enter year"))
if x%400 == 0:
    print("leap year")
elif x%4:
    print("non-leap year")
else:
    print("leap year")
    
"""

#10
"""
    
print("Enter three number")
a,b,c = int(input()),int(input()),int(input())
if a >= b:
    if a >= c:
        print("greater among these are : ",a)
    else :
        print("greater among these are :",c)
        
elif b>=c:
      print("greater among these are :",b)
else :
    print("greater among these are :",c)
    
"""
#11
"""
print("Enter month number")
month = int(input())
if month in (1,3,5,7,8,10,12):
    print("Month contain 31 days ")
elif month in (4,6,9,11):
    print("Month contain 30 days ")
else:
    print("Month contain 28 or 29 days ")
"""
#12
"""

x = complex(input("enter a complex no."))
print(x.real)if x.real > x.imag else print(x.imag)

"""














