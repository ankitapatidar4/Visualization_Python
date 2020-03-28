#!/usr/bin/env python
# coding: utf-8

# In[24]:


#import libraries
import pandas as pd


# In[25]:


names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,-2,77,78,101]


# In[26]:


#creating a dataframe from above data
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades']) 
df


# In[27]:


# replace all the subzero grades with a grade of zero
df.loc[(df['Grades'] < 0,'Grades')] = 0


# In[28]:


df


# Jessica's grade -2 is changed to 0 
