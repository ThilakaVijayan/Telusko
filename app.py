# Getting Started with Python
# terminal outout
"""
192-168-1-103:~ ThilakaHome$ python3
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 9 - 8
1
>>> 4 * 6
24
>>> 8 / 4
2.0
>>> 5 / 2
2.5
>>> 5 // 2  # outs only integer part of the answer
2
>>> 8 + 9 - 10
7
>>> 8 + 9 -
  File "<stdin>", line 1
    8 + 9 -
           ^
SyntaxError: invalid syntax
>>> 8 + 2 * 3
14
>>> (8 + 2) * 3
30
>>> 2 * 2 * 2
8
>>> 2 ** 3
8
>>> 10 // 3
3
>>> 10 % 3
1
>>> 'navin'
'navin'
>>> print('navin')
navin
>>> print('navin's laptop')
  File "<stdin>", line 1
    print('navin's laptop')
                 ^
SyntaxError: invalid syntax
>>> print("navin's laptop")
navin's laptop
>>> print('navin "laptop"')
navin "laptop"
>>> print('navin's "laptop"')
  File "<stdin>", line 1
    print('navin's "laptop"')
                 ^
SyntaxError: invalid syntax
>>> print('navin\'s "laptop"')
navin's "laptop"
>>> 'navin' + 'navin'
'navinnavin'
>>> 10 * 'navin'
'navinnavinnavinnavinnavinnavinnavinnavinnavinnavin'
>>> print('c:\docs\navin')
c:\docs
avin
>>> print(r'c:\docs\navin')  # r stands for raw. print the raw string and dont convert it.
c:\docs\navin

"""

# -----------------------------------------------------
# Variables in Python
# terminal outout
"""
192-168-1-103:~ ThilakaHome$ python3
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> x = 2
>>> x + 3
5
>>> y = 3
>>> x + y
5
>>> x = 9
>>> x + y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> x + 10
19
>>> _ + y   # previous output plus the variable 'y'
22
>>> name = 'youtube'
>>> name
'youtube'
>>> name + ' rocks'
'youtube rocks'
>>> name ' rocks'
  File "<stdin>", line 1
    name ' rocks'
         ^
SyntaxError: invalid syntax
>>> name[0]
'y'
>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> name[-1]
'e'
>>> name[-7]
'y'
>>> name[0:2]
'yo'
>>> name[0:4]
'yout'
>>> name[1:4]
'out'
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> name[3:10]
'tube'
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> name[0] = 'R'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 'my ' + name[3:]
'my tube'
>>> myname = 'Navin Reddy'
>>> len(myname)
11

"""

# -----------------------------------------------------
# List in Python
# terminal outout
"""
192-168-1-103:~ ThilakaHome$ python3
Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> nums = [25, 12, 36, 95, 14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[0]
25
>>> nums[54]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> nums[4]
14
>>> nums[2:]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-5]
25
>>> names = ['navin', 'kiran', 'john']
>>> names
['navin', 'kiran', 'john']
>>> values = [9.5, 'Navin', 25]
>>> mil = [ nums, names]
>>> mil
[[25, 12, 36, 95, 14], ['navin', 'kiran', 'john']]
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2, 77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 
"""

# -----------------------------------------------------
# Tuple & set
# terminal outout
"""

>>> tup = (21,36,14,25)  # iteration in tuple is faster than list, because  tuple is immutable.
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1] = 33
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> s = {22, 25, 14, 21, 5}
>>> s
{5, 14, 21, 22, 25}
>>> s = {25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}

"""

# -----------------------------------------------------
# Dictionary
# terminal outout
"""
>>> data = {1:'Navin',2:'Kiran',4:'Harsh'}
>>> data[4]
'Harsh'
>>> data[1]
'Navin'
>>> data[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
>>> data.get(1)
'Navin'
>>> data.get(3)
>>> print(data.get(3))
None
>>> data.get(1,'Not Found')
'Navin'
>>> data.get(3,'Not Found')
'Not Found'
>>> keys = ['Navin','Kiran','Harsh']
>>> values = ['Python', 'java', 'JS']
>>> data = dict(zip(keys,values))
>>> data
{'Navin': 'Python', 'Kiran': 'java', 'Harsh': 'JS'}
>>> data = dic(zip(keys,values))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dic' is not defined
>>> data = dict(zip(keys,values))
>>> data
{'Navin': 'Python', 'Kiran': 'java', 'Harsh': 'JS'}
>>> data['Kiran']
'java'
>>> data['Monika']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Monika'
>>> data['Monika'] = 'CS'
>>> data
{'Navin': 'Python', 'Kiran': 'java', 'Harsh': 'JS', 'Monika': 'CS'}
>>> del data['Harsh']
>>> data
{'Navin': 'Python', 'Kiran': 'java', 'Monika': 'CS'}
>>> prog = {'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
>>> prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog['JS']
'Atom'
>>> prog['Python']
['Pycharm', 'Sublime']
>>> prog['Python'][1]
'Sublime'
>>> >>> prog['Java']['JEE']
'Eclipse'
>>> 
"""

# -----------------------------------------------------
# Help
# terminal outout
"""

>>> help()
help> topics
help> LISTS
q
help> quit

"""

# -----------------------------------------------------
# Python Editor | Sublime Text
"""
# we can use Sublime text instead of PyCharm, which is light weight
"""

# -----------------------------------------------------
# More on Variables in Python
# terminal outout
"""

>>> num = 5
>>> id(num)
4437125904
>>> name = 'navin'
>>> id(name)
4441496240
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
4437126064
>>> id(b)
4437126064
>>> id(10)
4437126064
>>> k = 10
>>> id(k)
4437126064
>>> a = 9
>>> id(a)
4437126032
>>> id(b)
4437126064
>>> k = a
>>> id(k)
4437126032
>>> b
10
>>> b = 8
>>> id(10) 
4437126064  # this will be garbage collected in sometime, as no one is pointing to it

>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15  # constants are represented by capital valriable, but there is no cocept of constant, it can still be changed
>>> type(PI)
<class 'float'>
"""

# -----------------------------------------------------
# Data Types in Python
# terminal outout
"""

>>> num = 2.5
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num)
<class 'int'>
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k=float(b)
>>> k
5.0
>>> k = 6
>>> c = complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool = b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> int(True)
1
>>> int(False)
0
>>> lst = [25,36,45,12]
>>> type(lst)
<class 'list'>
>>> s = {25,36,45,15,12,25}
>>> s
{36, 12, 45, 15, 25}
>>> type(s)
<class 'set'>
>>> t = (25,36,4,57,12)
>>> type(t)
<class 'tuple'>
>>> str = "navin"
>>> st = 'a'
>>> type(st)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> d = {'navin':'samsung','rahul':'Iphone','kiran':'Oneplus'}
>>> d.keys()
dict_keys(['navin', 'rahul', 'kiran'])
>>> d.values()
dict_values(['samsung', 'Iphone', 'Oneplus'])
>>> d['rahul']
'Iphone'
>>> d.get('kiran')
'Oneplus'
>>> 

"""

# -----------------------------------------------------
# Operators in Python
# terminal outout
"""
# Arithmetic Operator
>>> x=2
>>> y=3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x/4
0.5

# Assignment Operator
>>> x = x+2
>>> x
4
>>> x+=2
>>> x
6
>>> x*=3
>>> x
18
>>> a,b=5,6
>>> a
5
>>> b
6
>>> 

#Unary Operator

>>> n = 7
>>> n
7
>>> n = -n
>>> n
-7
>>>

#Relational Operator
>>> a<b
True
>>> a>b
False
>>> a==b
False
>>> a=6
>>> a==b
True
>>> a<=b
True
>>> a>=b
True
>>> a!=b
False
>>> b=7
>>> a!=b
True
>>> 

#Logical Operator
>>> a = 5
>>> b = 4
>>> a < 8 and b < 5
True
>>> a < 8 and b < 2
False
>>> a < 8 or b < 2
True
>>> a = True
>>> a
True
>>> not a
False
>>> a = not a
>>> a
False
>>>

"""

# -----------------------------------------------------
# Number System Conversion in Python
# terminal outout
"""
>>> bin(25)
'0b11001'
>>> 0b0101
5
>>> oct(25)
'0o31'
>>> hex(25)
'0x19'
>>> hex(10)
'0xa'
>>> 0xf
15
>>> 

"""

# -----------------------------------------------------
# Swap 2 Variables in Python
"""
#approch #1
a = 5
b = 6

a = a + b
b = a - b
a = a - b

print(a)
print(b)
#approch #2
a = 5
b = 6

a = a ^ b

b = a ^ b
a = a ^ b
#approch #3
print(a)
print(b)

a = 5
b = 6

a,b = b,a

print(a)
print(b)


"""

# -----------------------------------------------------
# Python BitWise Operators
# terminal outout

"""
>>> ~12
-13
>>> 12 & 13
12
>>> 12 | 13
13
>>> 24 & 30
24
>>> 12 ^ 13
1
>>> 25^30
7
>>> 10<<2
40
>>> 10>>2
2
>>> 

"""

# -----------------------------------------------------
# Import Math Functions in Python
# terminal outout

"""

>>> x = sqrt(25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> import math
>>> x = math.sqrt(25)
>>> x
5.0
>>> x = math.sqrt(15)
>>> x
3.872983346207417
>>> print(math.floor(2.9))
2
>>> print(math.ceil(2.2))
3
>>> 3**2
9
>>> print(math.pow(3,2))
9.0
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> m.sqrt(25)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'm' is not defined
>>> import math as m
>>> math.sqrt(25)
5.0
>>> m.sqrt(25)
5.0
>>> from math import sqrt, pow
>>> pow(4,5)
1024.0
>>> help('math')

"""

# -----------------------------------------------------
# Working with PyCharm | Run | Debug | Trace | py file
"""
x = 5
y = 6
z = x + y
print(z)

"""

# -----------------------------------------------------
# User input in Python | Command Line Input
"""
x = input("Enter first number: ")
y = input("Enter second number: ")
z = x + y
print(z)  # gives output as string

x = input("Enter first number: ")
a = int(x)
y = input("Enter second number: ")
b = int(y)
z = a + b
print(z)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = x + y
print(z)

ch = input('Enter a char')
print(ch)

ch = input('Enter a char')
print(ch[0])

ch = input('Enter a char')[0]
print(ch)


result = eval(input('Enter an expression: '))
print(result)



# getting input from command line. Give input in the 'Edit configuration -> Parameters'
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)

"""

# -----------------------------------------------------
# If Elif Else Statement in Python
x = 8
r = x % 2
if r == 0:
    print("Even")

print("Bye")

x = 2

if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
else:
    print("wrong input")