#!/usr/bin/env python
# coding: utf-8

# # OOP - Classes, Instances & Class Variables

# In[1]:


class Employee:
    
    num_of_emps = 0
    raise_amount = 1.1
    def __init__(self, first, last, pay, age):
        self.first = first
        self.last = last
        self.pay = pay
        self.age = age
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# In[2]:


emp1 = Employee('Muhammad', 'Arslan', 60000, 29)
emp2 = Employee('Hamza', 'Sipra', 65000, 30)


# In[3]:


emp1.email


# In[4]:


emp2.first


# In[5]:


emp1.raise_amount


# In[6]:


emp1.pay


# In[7]:


emp1.apply_raise()


# In[8]:


emp1.pay


# In[9]:


emp2.apply_raise()


# In[10]:


emp2.pay


# In[11]:


emp1.__dict__


# In[12]:


Employee.__dict__


# In[13]:


Employee.num_of_emps

