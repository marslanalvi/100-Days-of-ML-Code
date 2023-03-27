#!/usr/bin/env python
# coding: utf-8

# # Pandas Excel Exercises, Practice, Solution

# In[1]:


import pandas as pd


# In[2]:


df_coal = pd.read_excel('D:/Python/Datasets/coalpublic2013.xlsx')


# In[3]:


df_coal.head(5)


# In[29]:


filt = df_coal['Mine_Name'].str.contains('Hill', na=False)
df_coal[filt]


# In[5]:


df_coal[['Year', 'MSHA ID']].head(5)


# In[6]:


Sum = df_coal['Production'].sum()
Sum


# In[7]:


Mean = df_coal['Production'].mean()
Mean


# In[8]:


Min = df_coal['Production'].min()
Min


# In[9]:


Max = df_coal['Production'].max()
Max


# In[10]:


import numpy as np
df_coal.insert(5, "column1", np.nan)


# In[11]:


df_coal.head(5)


# In[12]:


df_subtotal = df_coal[['MSHA ID', 'Labor_Hours']].groupby('MSHA ID').sum()
df_subtotal


# In[13]:


df_coal['MSHA ID'].head(5)


# In[14]:


df_coal[df_coal['MSHA ID'] == '103381'].head()


# In[15]:


filt = df_coal['Labor_Hours'] > 20000
df_coal[filt].head(10)


# In[16]:


filt = df_coal['Mine_Name'].map(lambda x: x.startswith('P'))
df_coal[filt].head(3)


# In[17]:


filt = df_coal['MSHA ID'].isin([102976,103380])
df_coal[filt]


# In[18]:


df_coal.query('Mine_Name == ["Shoal Creek Mine", "Piney Woods Preparation Plant"]')


# In[19]:


df_emp = pd.read_excel('D:/Python/Datasets/employee.xlsx')
df_emp.head(5)


# In[20]:


df_emp['hire_date'].head(5)


# In[21]:


filt = df_emp['hire_date'] <= '20070101'
df_emp[filt]


# In[22]:


df_emp.sort_values('hire_date').head(5)


# In[23]:


df_indexed = df_emp.set_index(['hire_date'])


# In[24]:


df_indexed['2005']

