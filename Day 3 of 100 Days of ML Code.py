#!/usr/bin/env python
# coding: utf-8

# # List, Tuple, Set, Dictionary

# # List: A list is a collection of values that are ordered and changeable. Lists are written with square brackets.

# In[1]:


fruits = ["apple", "banana", "cherry"]
print(fruits)


# In[2]:


# Accessing items in a list through index
print(fruits[1])


# In[3]:


# Changing an item in a list
fruits[1] = "kiwi"
print(fruits)


# In[4]:


# Adding an item to a list
fruits.append("orange")
print(fruits)


# In[5]:


# Removing an item from a list
fruits.remove("cherry")
print(fruits)


# # Tuple: A tuple is a collection of values that are ordered and unchangeable. Tuples are written with parentheses.

# In[6]:


fruits = ("apple", "banana", "cherry")
print(fruits)


# In[7]:


# Accessing items in a tuple
print(fruits[1])


# # Set: A set is a collection of unique values that are unordered and changeable. Sets are written with curly brackets.

# In[8]:


fruits = {"apple", "banana", "cherry"}
print(fruits)


# In[9]:


# Adding an item to a set
fruits.add("orange")
print(fruits)


# In[10]:


# Removing an item from a set
fruits.remove("cherry")
print(fruits)


# # Dictionary: A dictionary is a collection of key-value pairs that are unordered and changeable. Dictionaries are written with curly brackets and each item is separated by a comma.

# In[11]:


fruits = {"apple": 1, "banana": 2, "cherry": 3}
print(fruits)


# In[12]:


# Accessing items in a dictionary
print(fruits["banana"])


# In[13]:


# Changing a value in a dictionary
fruits["banana"] = 4
print(fruits)


# In[14]:


# Adding an item to a dictionary
fruits["orange"] = 5
print(fruits)


# In[15]:


# Removing an item from a dictionary
del fruits["cherry"]
print(fruits)

