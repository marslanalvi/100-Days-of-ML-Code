#!/usr/bin/env python
# coding: utf-8

# # OOP - Classes and Instances

# In[1]:


class Employee:
    def __init__(self, first, last, pay, age):
        self.first = first
        self.last = last
        self.pay = pay
        self.age = age
        self.email = first + '.' + last + '@gmail.com'
        
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# In[2]:


emp1 = Employee('Muhammad', 'Arslan', 60000, 29)
emp2 = Employee('Hamza', 'Sipra', 65000, 30)


# In[3]:


emp1.email


# In[4]:


emp2.fullname()


# In[5]:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        print("The engine is running!")
        
    def stop_engine(self):
        print("The engine has stopped!")


# In[6]:


mycar = Car("Toyota", "Corolla", 2017)


# In[7]:


mycar.make


# In[8]:


mycar.model


# In[9]:


mycar.year


# In[10]:


mycar.start_engine()


# In[11]:


mycar.stop_engine()

