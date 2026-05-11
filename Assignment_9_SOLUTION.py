"""
While Loop

1. Write a python script to print MySirG N times on the screen
2. Write a python script to print first N natural numbers
3. Write a python script to print first N natural numbers in reverse order
4. Write a python script to print first N odd natural numbers
5. Write a python script to print first N odd natural numbers in reverse order
6. Write a python script to print first N even natural numbers
7. Write a python script to print first N even natural numbers in reverse order
8. Write a python script to print squares of first N natural numbers
9. Write a python script to print cubes of first N natural numbers
10. Write a python script to print first 10 multiples of N
"""
#1. Write a python script to print MySirG N times on the screen
"""
n = int(input("Enter a number"))
i=1
while i<=n:
    print(i,"MySirG")
    i+=1
"""
#2. Write a python script to print first N natural numbers
"""
n = int(input("Enter a number"))
i=1
print("first",n, "natural numbers is : ")
while i<=n:
    print(i,end = ' ')
    i+=1
"""
#3. Write a python script to print first N natural numbers in reverse order
"""
n = int(input("Enter a number"))
i=n
print("first",n, "natural numbers in reverse order is : ")
while i>=1:
    print(i,end = ' ')
    i-=1
"""
#4. Write a python script to print first N odd natural numbers
"""
n = int(input("Enter a number"))
i=1
print("first",n, "odd natural numbers is : ")
while i<=2*n:
    print(i,end = ' ')
    i+=2
"""
#5. Write a python script to print first N odd natural numbers in reverse order
"""
n = int(input("Enter a number"))
i=2*n -1
print("first",n, "odd natural numbers in reverse order is : ")
while i>=1:
    print(i,end = ' ')
    i-=2
"""
#6. Write a python script to print first N even natural numbers
"""
n = int(input("Enter a number"))
i=2
print("first",n, "even natural numbers is : ")
while i<=2*n:
    print(i,end = ' ')
    i+=2

"""
#7. Write a python script to print first N even natural numbers in reverse order
"""
n = int(input("Enter a number"))
i=2*n
print("first",n, "even natural numbers  in reverse order is : ")
while i>=2:
    print(i,end = ' ')
    i-=2
"""
#8. Write a python script to print squares of first N natural numbers
"""
n = int(input("Enter a number"))
i=1
print("squares of first",n, "natural numbers is : ")
while i<=n:
    print(i**2,end = ' ')
    i+=1
"""
#9. Write a python script to print cubes of first N natural numbers
"""
n = int(input("Enter a number"))
i=1
print("cube of first",n, "natural numbers is : ")
while i<=n:
    print(i**3,end = ' ')
    i+=1
"""
#10. Write a python script to print first 10 multiples of N

n = int(input("Enter a number"))
i=1
print("first 10 multiples of",n, " is : ")
while i<=10:
    print(i*n,end = ' ')
    i+=1