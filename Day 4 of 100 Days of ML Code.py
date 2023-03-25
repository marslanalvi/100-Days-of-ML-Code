#!/usr/bin/env python
# coding: utf-8

# # For and While Loop

# # For Loop

# In[1]:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# In[2]:


for i in range(3):
    print(i)


# In[3]:


for i in range(1, 10, 2):
    print(i)


# # While Loop

# In[4]:


i = 1
while i < 6:
    print(i)
    i += 1


# In[5]:


x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    if x == 8:
        break
    print(x)


# # Basic Exercises: for Loop

# In[6]:


# Print numbers from 1 to 10:
for i in range(1, 11):
    print(i)


# In[7]:


# Print the sum of numbers from 1 to 10:
sum = 0
for i in range(1, 11):
    sum += i
print(sum)


# In[8]:


# Print all the even numbers between 1 and 20:
for i in range(2, 21, 2):
    print(i)


# In[9]:


# Print the multiplication table of a number (up to 10):
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num*i)


# In[10]:


# Print the reverse of a string:
string = "hello"
reverse = ""
for char in string:
    reverse = char + reverse
print(reverse)


# In[11]:


# Print the length of each word in a sentence:
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
for word in words:
    print(word, len(word))


# # Basic Exercises: while Loop

# In[12]:


# Print numbers from 1 to 10:
i = 1
while i <= 10:
    print(i)
    i += 1


# In[13]:


# Print the sum of numbers from 1 to 10:
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum)


# In[14]:


# Print all the even numbers between 1 and 20:
i = 2
while i <= 20:
    print(i)
    i += 2


# In[15]:


# Print the multiplication table of a number (up to 10):
num = 5
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1


# In[16]:


# Print the reverse of a string:
string = "hello"
reverse = ""
i = len(string) - 1
while i >= 0:
    reverse += string[i]
    i -= 1
print(reverse)


# In[17]:


# Print the length of each word in a sentence:
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
i = 0
while i < len(words):
    print(words[i], len(words[i]))
    i += 1

