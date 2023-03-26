#!/usr/bin/env python
# coding: utf-8

# # Function Exercises

# In[1]:


def new_func(name, age):
    print(name, age)


# In[2]:


new_func('Arslan', 28)


# In[3]:


def display_numbers_in_arguments(*numbers):
    for no in numbers:
        print(no)


# In[4]:


display_numbers_in_arguments(2, 3, 4, 5)


# In[5]:


display_numbers_in_arguments(2, 3)


# In[6]:


def calculations(a, b, e):
    c = a + b
    d = a - b
    f = a * e
    return (c, d, f)


# In[7]:


calculations(40, 10, 2)


# In[8]:


def employee():
    name_emp = input("Enter Employee's Name:" )
    emp_sal = int(input("Enter Employee's Salary: "))
    no_sal = 0
    if emp_sal == no_sal:
        emp_sal = emp_sal + 9000
        return emp_sal
    print(name_emp, emp_sal)


# In[9]:


employee()


# In[10]:


def employee2(name, salary = 9000):
    print('Name: ', name, 'Salary: ', salary)


# In[11]:


employee2('Arslan', )


# In[12]:


employee2('Arslan', 150000)


# In[13]:


def outer(a, b):
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5


# In[14]:


outer(5, 10)


# In[15]:


def addition(num):
    if num:
        return num + addition(num -1)
    else:
        return 0


# In[16]:


addition(150)


# In[17]:


def display_student(name, age):
    return (name, age)


# In[18]:


display_student('Arslan', 28)


# In[19]:


show_student = display_student


# In[20]:


show_student('Arslan', 28)


# In[21]:


print(list(range(4, 30, 2)))


# In[22]:


x = [4, 6, 8, 24, 12, 2]
max(x)


# In[23]:


salary = 8000

def printSalary():
  salary = 12000
  print("Salary:", salary)
  
printSalary()
print("Salary:", salary)


# In[24]:


def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)

