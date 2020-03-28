#!/usr/bin/env python
# coding: utf-8

# In[9]:


#import required libraries
import pandas as pd
import numpy as np


# In[3]:


#read the data into dataframe
df = pd.read_csv("datasets/datasets/gradedata.csv")
df.head()


# In[14]:


# create a column classifying the row as pass or fail
df["Result"] = np.where(df["grade"] >= 80, "Pass", "Fail")


# In[15]:


df.head()

