#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import pandas as pd
from sqlalchemy import create_engine


# In[2]:


# Connect to sqlite db
db_file  = r'C:/users/ankit/datasets/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))


# In[3]:


# query the name of the table
sql = "select name from sqlite_master"  
"where type = 'table';"
sql


# In[4]:


sales_data_df = pd.read_sql(sql,engine) 
sales_data_df


# In[5]:


# query all the record from the table scores
sql = "select * from scores;" 


# In[6]:


#read the data into dataframe
sales_data_df = pd.read_sql(sql,engine) 
sales_data_df

