#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#iris dataset into 3 dimwntions an plot 3d chart with transformed dimentions color each point with specific class


# In[36]:



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn.decomposition import PCA as sklearnPCA


# In[37]:



iris = datasets.load_iris()


# In[38]:


x = iris.data
y = iris.target


# In[41]:


pca = decomposition.PCA(n_components=3)
pca.fit(x)


# In[42]:


print(pca.explained_variance_ratio_)


# In[43]:


x = pca.transform(x)


# In[44]:


x


# In[53]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y, edgecolor='k')
plt.show()


# In[50]:





# In[ ]:




