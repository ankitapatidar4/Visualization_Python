#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd  #import pandas library


# In[3]:


county = pd.read_csv("all_050_in_01.P1.csv")  #read the csv file into pandas dataframe


# In[4]:


county.head() #display first five rows of data


# In[5]:


county.shape  #displays dimensionality of the dataframe i.e county has 67 rows and 15 columns

