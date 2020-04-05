#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt 
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("datasets/datasets/gradedata.csv") 
df.head()


# In[4]:


df.hist(column="age", by="gender")

