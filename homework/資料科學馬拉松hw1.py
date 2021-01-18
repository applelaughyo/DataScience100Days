#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


array = np.linspace(0,20,21,dtype = 'int32')
array


# In[28]:


for i in range(0,20):
    if array[i] % 2 == 0:
        print(array[i] , end = ' ')
    elif array[i] == 0:
        print(array[i] , end = ' ')


# In[26]:


for i in range(0,20):
    if array[i] % 3 == 0:
        print(array[i] , end = ' ')
    elif array[i] == 0:
        print(array[i] , end = ' ')

