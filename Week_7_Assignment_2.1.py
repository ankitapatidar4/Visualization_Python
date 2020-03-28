#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd
import numpy as np
import glob                    


# In[2]:


#create an empty dataframe
full_data = pd.DataFrame()


# In[3]:


#loop through all the files matching the pattern, load file f into df and append the contents of df to full data
for f in glob.glob("datasets/datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    full_data = full_data.append(df,ignore_index=True)


# In[4]:


#display first five records
full_data.head() 


# In[5]:


#display dimension of new dataframe that combines all the excel files in the folder
full_data.shape

