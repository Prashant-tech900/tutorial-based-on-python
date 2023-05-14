#!/usr/bin/env python
# coding: utf-8

# # TASK 2

# 1. Write a Python program to find whether a given number
# (accept from the user) is even or odd, print out an
# appropriate message to the user. 

# In[3]:


x = eval(input("enter any digit to check odd or even number :- "))
if x%2==0:
    print("odd number")
else:
    print("even number")


# 2. Write a Python program to test whether a passed letter
# is a vowel or not.

# In[2]:


vowel = ["a","e","i","o","u","A","E","I","O","U"]
x = input("enter any alphabet :- ")
if x in vowel:
    print("it's a vowel", x )
else:
    print("it's not a vowel",x)


# 3. Write a Python Program basic calculator using python. 
# 

# In[26]:


a=eval(input("enter first digit:- "))
b=eval(input("enter second digit:- "))
opr=input("enter any opr (+,-,*,/):- ")
if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)
elif opr=="*":
    print(a*b)
elif opr=="/":
    print(a/b)
else:
    print("inviled opr")


# 5. Write a Python program to find maximum and minimum
# accept from the user two number. 

# In[2]:


x=eval(input("enter first digit x:- "))
y=eval(input("enter second digit y:- "))
if x>y:
    print('x is maximum number than y',x)
elif x<y:
    print('x is minimum number than y',y)
elif x==y:
    print('both are equal number')
else:
    print('inviled ...')


# 4.Write a Python program to calculate division obtained
# by student in overall 5 subject.

# In[3]:


per=float(input("Enter score of students:-"))
if per>=90:
    print("A+","Congratulations👍")
elif per>=80:
    print("A","First Division😘")
elif per>=60:
    print("B","Ohh! Below Average🤷‍♂️")
elif per>=50:
    print("C","Third Division🤦‍♂️")
else:
    print("F","Hey There Y😒u Are Fail")


# # TASK 1

# 1. Write a Python program which accepts the user's first
# and last name and print them in reverse order with a
# space between them. 

# In[3]:


x1 = input("enter first name: ")
x2 = input("enter second name: ")
print(x2," ",x1)


# 2. Write a Python program which accepts the radius of a
# circle from the user and compute the area.
# Sample Output :
# r = 6
# Area = 113.09734 

# In[10]:


r = eval(input("enter the radius: "))
A=(22/7)*r*r
print("Area of radius is:-",A)


# 3. Write a Python Program to Swap Two Variables.

# In[11]:


x = 6
y =16
temp = x
x = y
y = temp
print('the value of x after swapping: {}'.format(x))
print('the value of y after swapping: {}'.format(y))


# 4. Write a Python Program to Calculate the Area of a
# Triangle.
# - Using Base and Height.
# - The area of a triangle with 3 sides .

# In[14]:


base=eval(input("enter the base: "))
height=eval(input("enter the height: "))
print("area of triangle",0.5*base*height)


# In[15]:


a=eval(input("enter the base: "))
b=eval(input("enter the height: "))
c=eval(input("enter the base: "))
Area = (a+b+c)/2
print(Area)


# 5. Write a Python Program basic calculator using python
# using arithmetical operations. 

# In[16]:


a=eval(input("enter first digit:- "))
b=eval(input("enter second digit:- "))
opr=input("enter any opr (+,-,*,/):- ")
if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)
elif opr=="*":
    print(a*b)
elif opr=="/":
    print(a/b)
else:
    print("inviled opr")


# 6. Write a Python Program to solve quadratic equation.

# In[20]:


import cmath
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))   
d = (b**2) - (4*a*c)   
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2)) 


# # TASK 3

# 1. Write a Python program display the multiplication table
# of accept from the user.

# In[24]:


num = int(input("Display multiplication table of?: "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# 3. Write a Python program to find the factorial of a given
# number.

# In[28]:


num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)


# 4. Write a Python program to Count the total number of
# digits in a number accept from the user.

# In[30]:


n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)


# In[ ]:




