#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import required libraries
import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# read the csv into the dataframe
df = pd.read_csv("datasets/datasets/gradedata.csv") 
df.head()


# In[6]:


plt.scatter(df["hours"],df["grade"])


# Yes, there is a linear relationship between hours of study and grades, as we can see from the above scatter plot that as the number hours of study 
