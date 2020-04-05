#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#create dataset
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,83,77,78,95] 
GradeList = zip(names,grades) 


# In[3]:


#create dataframe
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])


# In[4]:


df.plot()


# In[5]:


#plot and add an annotation to Bob's 76 that says “Wow!”

df.plot()
displayText = "Wow!" 
xloc = 1 
yloc = df['Grades'].max() 
xtext = -80
ytext = -20   
plt.annotate(displayText, xy=(0,df["Grades"].min()),arrowprops=dict(facecolor='black',shrink=0.05), xytext=(xtext,ytext), 
             xycoords=('axes fraction', 'data'),textcoords='offset points')

