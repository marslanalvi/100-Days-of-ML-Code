#!/usr/bin/env python
# coding: utf-8

# # Day 1: 100 Days of ML Code

# ## Variables

# A Variable is a storing point of any character, string, number (integer / float), operation, booleans. A variable name can be anyone's own choice, but the best way to name the variable is to give that variable a relavent name, so that, anyone reading your code can easily understand what, why and how you used the variables in your code. Write variable names in lower case and should not consider writing variable names such as x, y or any other single character, which doesn't reflect any meaningful meaning.

# In[1]:


#String
name = "arslan"
print(name)


# In[2]:


#integer
number = 5
print(5)


# In[3]:


#float
float_number = 5.5
print(float_number)


# In[4]:


#operations
addition = 5 + 5
print(addition)

substraction = addition - 0
print(substraction)

division = substraction / 5
print(int(division))

multiplication = division * addition
print(float(multiplication))

square = multiplication ** 2
print(int(square))

modulo = square // 3
print(modulo)


# In[5]:


#boolean
value_is = True
print(value_is)


# # Expressions

# In[6]:


x = 5
y = 10
z = 15
formula = (2 * x + (y + z - x))/ 2
formula


# 1. Arithmetic Operators: + - / % * // **
# 2. Comparisons: == != < > <= >=
# 3. Compound Assignment: = += -= *= /=
# 4. Logical Operators: and or not

# # Conditional Statements

# In[7]:


#if statement
age = 25
if age >= 18:
    print("You are old enough to vote.")


# In[8]:


#if-else statement
x = 5
if x % 2 == 0:
    print("x is even.")
else:
    print("x is odd.")


# In[9]:


#if-elif-else
x = 10
if x < 0:
    print("x is negative.")
elif x == 0:
    print("x is zero.")
else:
    print("x is positive.")

