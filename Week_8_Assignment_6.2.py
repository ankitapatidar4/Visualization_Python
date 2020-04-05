#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd 
import numpy as np 


# In[2]:


#read the csv file
df = pd.read_csv("datasets/datasets/gradedata.csv") 
df.head()


# In[3]:


import statsmodels.formula.api as sm 


# In[4]:


# regression on age, exercise, hours
result = sm.ols(formula='grade ~ age + exercise + hours',data=df).fit()
result.summary()


# In[5]:


# regression on exercise, hours
result_2 = sm.ols(formula='grade ~ exercise + hours',data=df).fit()
result_2.summary()


# In[6]:


# assigning the gender column values to numeric, as in 0 for male and 1 for female
df["gender"]=df['gender'].replace("male",0)
df["gender"]=df['gender'].replace("female",1)


# In[7]:


df.head()


# In[8]:


#df.gender = df.gender.astype("category")
df.info()


# In[9]:


# add gender to regression
result_3 = sm.ols(formula='grade ~ gender + exercise + hours',data=df).fit()
result_3.summary()


# There is very slight variation to the third decimal place of R-squared value from .664 to .665 on adding gender into the regression.It doesn't really add any significance to our model.
# So now the equation will be:-
# 
# grade = 0.447(if female) + 1.917 * hours of study +.984 * hours of exercise + 58.3145.
#  
