#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import matplotlib.pyplot as plt 
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#create dataset
names = ['Bob','Jessica','Mary','John','Mel'] 
status = ['Senior','Freshman','Sophomore','Senior','Junior'] 
grades = [76,95,77,78,99] 
GradeList = zip(names,grades,status)


# In[3]:


#create dataframe
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades','Status'])


# In[4]:


#create a bar plot where the status is the label
df = df.set_index(df['Status'])
df.plot(kind="bar")

