#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


#create dataset
names = ['Bob','Jessica','Mary','John','Mel'] 
absences = [3,0,1,0,8] 
detentions = [2,1,0,0,1] 
warnings = [2,1,5,1,2]
GradeList = zip(names,absences,detentions,warnings) 
columns=['Names', 'Absences', 'Detentions','Warnings'] 


# In[22]:


#create dataframe
df = pd.DataFrame(data = GradeList, columns=columns) 
df


# In[23]:


# create a column to show the total violations
df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings'] 
df


# In[24]:


#highlighting best one ie.John instead of Mel
plt.pie(df['TotalDemerits'])
plt.pie(df['TotalDemerits'],labels=df['Names'],explode=(0,0,0,0.15,0),startangle=90,autopct='%1.1f%%',) 
plt.axis('equal')
plt.show()

