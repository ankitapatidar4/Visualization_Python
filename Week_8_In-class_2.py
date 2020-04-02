#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import required libraries
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#read the data,here the data is of March 30
covid0330 = pd.read_csv("covid_19.csv")


# In[4]:


#display top 5 records
covid0330.head()


# In[5]:


#check for null value
covid0330.isna().sum()


# In[6]:


# fill the null values with NA for Province/State column
covid0330[['Province_State']] = covid0330[['Province_State']].fillna('NA')


# In[7]:


covid0330.isna().sum()


# Now, there are no null values for Province_State that we will use for analysis here

# In[8]:


#import library for plotting and map visualization
import plotly.express as px
import folium


# In[9]:


#cases across countries/states/province worldwide reported as of March 30
m = folium.Map(location=[0, 0], tiles='Stamen Toner',
               min_zoom=1, max_zoom=4, zoom_start=1,legend_name="Confirmed")

for i in range(0, len(covid0330)):
    folium.Circle(
        location=[covid0330.iloc[i]['Lat'], covid0330.iloc[i]['Long_']],
        color='crimson', 
        tooltip =   '<li><bold>Country : '+str(covid0330.iloc[i]['Country_Region'])+
                    '<li><bold>Province : '+str(covid0330.iloc[i]['Province_State'])+
                    '<li><bold>Confirmed : '+str(covid0330.iloc[i]['Confirmed'])+
                    '<li><bold>Deaths : '+str(covid0330.iloc[i]['Deaths'])+
                    '<li><bold>Recovered : '+str(covid0330.iloc[i]['Recovered']),

        radius=int(covid0330.iloc[i]['Confirmed'])).add_to(m)
    


# In[10]:


m

