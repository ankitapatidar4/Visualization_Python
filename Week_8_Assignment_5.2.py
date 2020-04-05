#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd 
import numpy as np 


# In[2]:


# creating dataset
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees) 
df = pd.DataFrame(data=GradeList,columns=['Name','Grade','BS','MS','PhD']) 
df


# ### computing summary statistics 

# In[3]:


# number of values
df.count() 


# In[4]:


# calculating arithmetic average 
df.mean()


# In[5]:


#calculating median
df.median()


# In[6]:



df.mode()


# In[7]:


# standard deviation 
df.std()


# In[8]:


#minimum
df.min()


# In[9]:


#maximum
df.max()


# In[10]:


# first quantile
df.quantile(.25)


# In[11]:


# second quantile
df.quantile(.5)


# In[12]:


# third quantile
df.quantile(.75)


# In[13]:


# another pandas in-built function to view the summary statistics for numerical data type columns
df.describe()

