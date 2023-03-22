#!/usr/bin/env python
# coding: utf-8

# # Basic Calculator using conditional statements

# In[1]:


print("Welcome to the Calculator Program!")


# In[2]:


# Input the first number
num1 = input("Enter the first number: ")


# In[3]:


# Get the operation to perform
op = input("Enter an operation (+, -, *, /): ")


# In[4]:


# Get the second number
num2 = input("Enter the second number: ")


# In[5]:


# Check if the numbers are digits (not characters or anything else)
if num1.isdigit() and num2.isdigit():
    num1 = float(num1)
    num2 = float(num2)

    # Operations
    if op == "+":
        result = num1 + num2
        print("Answer: ", result)
    elif op == "-":
        result = num1 - num2
        print("Answer: ", result)
    elif op == "*":
        result = num1 * num2
        print("Answer: ", result)
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            result = num1 / num2
            print("Answer: ", result)
    else:
        print("Invalid operation!")
else:
    print("Invalid numbers!")


# In[ ]:




