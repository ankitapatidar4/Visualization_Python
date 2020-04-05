#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd 
import numpy as np 


# In[4]:


#read the csv file
df = pd.read_csv("datasets/datasets/gradedata.csv")


# In[5]:


#display the number of rows and columns in the dataset
df.shape


# In[6]:


# random Sample of 500 rows from dataframe
df_sample = df.take(np.random.permutation(len(df))[:500])


# In[7]:


#display dimension of samples dataset
df_sample.shape


# In[9]:


# top 5 records of sampled dataset
df_sample.head()

