"""
Assignment - 5 Full Stack Web Development using Python MySirG

Operators

1. Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)
2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)
3. Write a python script to swap data of two variables
4. Write a python script to find x power y, where values of x and y are given by user
5. Write a python script which takes a three digit number from the user and displays
only its first digit.
6. Write a python script which takes a three digit number from the user and displays
only its middle digit.
7. Write a python script which takes a three digit number from the user and displays
only its last digit.
8. Write a python script to use IN operator to display the data present in the list
9. Write a python script to use NOT IN operator to display the data not present in list
10. Write a python script to use IS operator to display if both variables are the same
object or not?

"""
#1
"""
x=int(input("Enter a number"))
a=x//10 #// floor division
print(a)

"""

#2
'''
x=int(input("Enter a number"))
a=x%10 #'%' - gives remainder
print("last digit of a entered number is: ",a)

'''
#3
#M-1
"""
x=int(input("Enter a number"))
y=int(input("Enter a number"))
x,y=y,x
print("swapped number is: ",x,y)

"""
#M-2
"""
x=int(input("Enter a number"))
y=int(input("Enter a number"))
temp=x
x=y
y=temp
print("swapped number is: ",x,y)

"""
#4
"""
x=int(input("Enter a number"))
y=int(input("Enter a number"))
print("desired no is:", x**y)

"""
#5
"""
x=int(input("Enter a three digit number"))
print(int(x/100))
"""
#6
"""
x=int(input("Enter a three digit number"))
x=x%100
#print(int(x/10))
print(x//10)

"""
#7
"""
x=int(input("Enter a three digit number"))
print("last digit is : ",x%10)
"""

#8
"""
list_1 =[0,1,33,44,767,66,]
x=int(input("enter a number "))
print(x in list_1)
"""

#9
"""
list_1 =[0,1,33,44,767,66,]
x=int(input("enter a number "))
print(x not in list_1)

"""
#10
x=int(input("Enter a number"))
y=int(input("Enter a number"))
print(x is y)

"""
>>> x=5
>>> y=5
>>> id(x)
2934397299120
>>> id(y)
2934397299120
>>> l1=[0,3,4,6]
>>> l2=[0,3,4,6]
>>> id(l1)
2934410567040
>>> id(l2)
2934438804416
>>> l1==l2
True
>>> l1 is l2
False
>>> #is id check kr rha h while "==" l1 and l2 ki value.
"""
