#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd   #import pandas library


# In[2]:


health = pd.read_excel("HEA02.xls")   #read the excel file into pandas dataframe


# In[3]:


health.head()   #display first five rows of data


# In[4]:


health.shape  #displays dimensionality of the dataframe i.e dataframe health has 3198 rows and 34 columns

