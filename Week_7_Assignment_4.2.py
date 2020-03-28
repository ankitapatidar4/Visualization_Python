#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd
import numpy as np


# In[2]:


#read the data into dataframe
df = pd.read_csv("datasets/datasets/gradedata.csv")
df.head()


# In[3]:


#create a column that shows busy if a student exercises more than 3hrs AND studies more than 17 hrs
df['isBusy'] = np.where((df['exercise']>3) & (df['hours'] > 17),'Yes', 'No')


# In[4]:


df.tail()

