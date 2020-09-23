#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#assignment 3
1.write a python program to implement your own myreduce 
function which works exactly same as pyhon built in function reduce()


# In[1]:


#python reduce function
from functools import reduce
lst =['sdfs','sdfsfsdf','sdf']
reduce(lambda a,b: a+b,lst)


# In[5]:


lst =['sdfs','sdfsfsdf','sdf']
def myreduce():
    sum=' '
    for i in lst:
        sum=sum+i
    return sum
myreduce()


# In[7]:


#python filter function
lst =[1,2,3,4,5,6,7,8]


list(filter(lambda x:x%2==0,lst))


# In[9]:


lst=[1,2,3,4,5,6,7,8]
lst1=[]
def myreduce():
    for i in lst:
        if(i%2==0):
         lst1.append(i)
    return lst1
myreduce()


# In[19]:


#implement list comprehension
letters = list('xyz')
pattern = []
for i in range(len(letters)):    
       for j in range(1,5):     
          pattern.append(letters[i]*j)
print(pattern)


# In[21]:


#using list comprehension
letters = list('xyz')
pattern = []

[pattern.append(letters[i]*j) for i in range(len(letters)) for j in range(1,5) ]
print(pattern)


# In[22]:


letters = list('xyz')
pattern = []

for i in range(1,5):
    for j in range(len(letters)):
        pattern.append(letters[j]*i)
print(pattern)


# In[23]:


#using list comprehension
letters = list('xyz')
pattern = []
[pattern.append(letters[j]*i) for i in range(1,5) for j in range(len(letters))]
print (pattern)


# In[6]:


list1=[1,2,3]
list2=[1,2,3]
for x in list1:
    for y in list2:
        print(y,x)
        


# In[8]:


# using list comprehension
list1=[1,2,3]
list2=[1,2,3]
op=[(y,x) for x in list1 for y in list2 ]
print(op)


# In[1]:


# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
lst3 = [[x + y] for y in range(3) for x in range(2, 5)]


# In[2]:


lst3


# In[3]:


# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
lst4 = [[a+b for b in range(2, 6)] for a in range(4)]
lst4


# In[ ]:




