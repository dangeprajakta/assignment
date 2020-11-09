#!/usr/bin/env python
# coding: utf-8

# In[ ]:


questio1:


# In[ ]:


Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18


# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


max=np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
min=np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])


# In[10]:


months = np.arange(12)
plt.plot(months,max)
plt.plot(months,min)


# In[ ]:


question2


# In[2]:


import pandas as pd
url = 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
titanic.head()


# In[3]:


#create apie chart to show male n female proportion


# In[4]:


gender=titanic['sex']


# In[17]:


gender.head()


# In[19]:


g1=gender.unique()


# In[20]:


g1


# In[21]:


plt.pie(gender.value_counts())


# In[8]:



name_col=gender.unique()


# In[9]:


name_col


# In[10]:


plt.title("male/female proportion")
plt.pie(gender.value_counts(), labels =['male','female'])


# In[11]:


#scatterplot with age and fare paid


# In[12]:


x=titanic['age']
y=titanic['fare']


# In[14]:


titanic.plot.scatter(x = 'age', y = 'fare')


# In[4]:


#plt.scatter(titanic['age'], titanic['fare'], c =  titanic['sex'].unique())
sns.scatterplot(x=titanic['age'], y=titanic['fare'], hue=titanic['sex'])


# In[ ]:




