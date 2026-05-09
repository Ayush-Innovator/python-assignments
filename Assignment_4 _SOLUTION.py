
"""
Assignment - 4 Full Stack Web Development using Python MySirG

User Input Problems

1. Write a python script to take your name as input from the user and then print it.
2. Write a python script to take input from the user. Input must be a number.
3. Write a python script which takes two numbers from the user, then calculate their sum
and display the result.
4. Write a python script which takes the radius from the user and display area of a circle.
5. Write a python script to calculate the square of a number. Number is entered by the user.
6. Write a python script to calculate the area of Triangle. Number is entered by the user.
7. Write a python script to calculate average of three numbers, entered by the user
8. Write a python script to calculate simple interest
9. Write a python script to calculate the volume of a cuboid.
10. Write a python script to calculate area of a rectangle
"""
#1
'''
x=input("enter your name: ")
print("your name is -",x)
'''
#2
"""
x=int(input("Enter a number"))
print(x)
print(type(x))
"""

#3
'''
print("Enter two number")
a=int(input())
b=int(input())
print("sum is :", a+b)

'''

#4
'''
radius = int(input("Enter radius of circle"))
pi=22/7
print("area of circle :",pi*radius*radius )
'''
#5
'''
a=int(input("enter a number"))
print("square of a number: ",a*a)
'''
#6
'''
half=0.5
base=int(input("enter base of a triangle"))
height=int(input("enter base of a height"))
print("area of a triangle: ",half*base*height)
'''
#7
'''
print("Enter three number")
a=int(input())
b=int(input())
c=int(input())

print("average is :", (a+b+c)/3)
'''

#8
'''
print("Principle,rate,time respectively")
p=int(input())
r=int(input())
t=int(input())
s_i=(p*r*t)/100
print("simple interest is :", s_i)
'''

#9
'''
print("length,breadth,height respectively")
l=int(input())
b=int(input())
h=int(input())
print("volume of cubeoid is: ", l*b*h)
'''
#10
l=int(input("length of a triangle"))
b=int(input("breadth of a triangle"))
print("area of a rectangle: ",l*b)
