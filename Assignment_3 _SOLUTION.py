
"""
Assignment-3: Type Conversion
1. Write a python script to convert a number into str type.
2. Write a python script to print Unicode of the character ‘m’
3. Write a python script to print character representation of a given unicode 100.
4. Write a python script to print any number and its binary equivalent
5. Write a python script to print any number and its octal equivalent.
6. Write a python script to print any number and its hexadecimal equivalent.
7. Write a python script to store binary number 1100101 in a variable and print it in
decimal format.
8. Write a python script to store a hexadecimal number 2F in a variable and print it in
octal format.
9. Write a python script to store an octal number 125 in a variable and print it in binary
format.
10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format.

"""
#1
"""
a=5
b=str(a)
print(type(b))

"""
#2
'''
print(ord('m'))

'''
#3
"""
print(chr(100))

"""
#4
"""
a=44
print(bin(a))

"""
#5
"""
a=33
print(oct(a))
"""
#6
'''
a=13011999
print(hex(a))

'''

#7
#method-1
'''
a= 0b1100101
print(a)
'''
#Method -2
"""
a="1100101" #string m store kro
print(int(a,2))# a k baad jo comma h wo base 2 ko represent kr rha h

"""
#8
'''
a=0x2f
print(oct(a))
'''
"""
a="2f"
dec=int(a,16)
print(oct(dec))
"""

#9
'''
a="125"
d=int(a,8)
print(bin(d))

'''
#10
#M-1
'''
a="25" #oct
b="39" #hex
print(bin(int(a,8)+int(b,16)))
'''
a=0o25
b=0x39
print(bin(a+b))
