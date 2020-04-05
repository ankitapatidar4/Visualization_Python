#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd 
import numpy as np 


# In[4]:


#read the csv file
df = pd.read_csv("datasets/datasets/gradedata.csv") 
df.head()


# In[5]:


# sorting the dataframe to order it by name, age, and then grade
df = df.sort_values(by=['fname', 'age','grade'],        
                    ascending=[True, True,True]) 
df.head()

