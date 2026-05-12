"""
1. Write a python script to print the first 10 multiples of 5.
2. Write a python script to print first 10 multiples of N
3. Write a python script to print first M multiples of N.
4. Write a python script to print the first 10 multiples of N in reverse order.
5. Write a python script to print table of user’s choice
6. Write a python script to print first N even natural numbers.
7. Write a python script to print first N odd natural numbers
8. Write a python script to print squares of first N natural numbers.
9. Write a python script to print cubes of first N natural numbers.
10. Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45
"""
#1. Write a python script to print the first 10 multiples of 5.
"""
print("the first 10 multiples of 5 is: ")
for i in range(1,11):
    
    print(5*i,end=' ')
"""
#2 Write a python script to print first 10 multiples of N
"""
n= int(input("Enter a number"))
print("the first 10 multiples of" ,n, "is: ")
for i in range(1,11):
    
    print(n*i,end=' ')
"""

#3. Write a python script to print first M multiples of N.
"""
n,m= int(input("Enter a number")),int(input("how many multiples of entered number"))
print("the first",m,"multiples of" ,n, "is: ")
for i in range(1,m+1):
    
    print(n*i,end=' ')
"""
#4. Write a python script to print the first 10 multiples of N in reverse order.
"""
n= int(input("Enter a number"))
print("the first 10 multiples of" ,n, "in reverse order is: ")
for i in range(10,0,-1):
    
    print(n*i,end=' ')
"""
#5. Write a python script to print table of user’s choice
'''
n= int(input("Enter a number  to print table of : "))
print("the table of" ,n, "is: ")
for i in range(1,11):
    
    print(n,"*",i, "=", n*i)
'''
# OUTPUT :
'''
Enter a number  to print table of : 2
the table of 2 is: 
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
'''
#6. Write a python script to print first N even natural numbers.
"""

n= int(input("Enter a number : "))
print("the first" ,n, "even natural numbers is: ")
for i in range(2,2*n +1,2):
    
    print(i,end=' ')
"""
#7. Write a python script to print first N odd natural numbers 
"""
n= int(input("Enter a number : "))
print("the first" ,n, "odd natural numbers is: ")
for i in range(1,2*n,2):
    
    print(i,end=' ')
"""
#8. Write a python script to print squares of first N natural numbers.
"""
n= int(input("Enter a number : "))
print("the squares of first" ,n, "natural numbers is: ")
for i in range(1,n+1,1):
    
    print(i**2,end=' ')
"""
#9. Write a python script to print cubes of first N natural numbers.
"""
n= int(input("Enter a number : "))
print("the cubes of first" ,n, "natural numbers is: ")
for i in range(1,n+1,1):
    
    print(i**3,end=' ')
"""
#10. Write a python script to display all prime numbers within a range.
n= int(input("Enter a number : "))
for i in range(2,n+1):
    count = 0
    for k in range(1,i+1,1):
        if i %k == 0:
            count+=1
    if count == 2:
        print(i,end=' ')
   