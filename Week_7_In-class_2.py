#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[140]:


plt.style.use("seaborn-whitegrid")


# In[141]:


X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]


# In[142]:


plt.scatter(X,Y)

#Change axes ranges
plt.xlim(0,1000)
plt.ylim(0,100)

#scatter plot color
plt.scatter(X, Y, s=100, c='red', marker='+')

#Add title
plt.title('Relationship Between Temperature and Iced Coffee Sales',fontsize = 12)

#Add axis labels 
plt.xlabel('Sold Coffee', fontsize = 14)
plt.ylabel('Temperature in Fahrenheit', fontsize = 14)
plt.show()


# In[143]:


fig = plt.figure()
ax = plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x, np.sin(x))
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

# set the x and y axis range
plt.xlim(0,11)
plt.ylim(-2,2)
plt.axis("tight")

#add title
plt.title('Plotting data using sin and cos', fontsize = 14)


# In[144]:


#import seaborn library
import seaborn as sns   


# In[145]:


plt.style.use('classic')
plt.style.use('seaborn-whitegrid')


# In[146]:


# Create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],size=2000)
data = pd.DataFrame(data, columns=["x","y"])


# In[147]:


# Plot the data with seaborn
sns.distplot(data['x'])
sns.distplot(data['y']);


# In[148]:


#kernel density  plot using seaborn
for col in 'xy':
 sns.kdeplot(data[col], shade=True)


# In[149]:


#Passing the full two-dimensional data set to kdeplot
sns.kdeplot(data)


# In[150]:


#using the joint distribution and the marginal distributions together
with sns.axes_style("white"):
    sns.jointplot("x","y",data, kind="kde")


# In[151]:


# Using a hexagonally based histogram in the joint plot
with sns.axes_style("white"):
    sns.jointplot("x","y",data, kind="hex")


# In[152]:


# visualizing multidimensional relationships

sns.pairplot(data)


# In[153]:


# Importing and Using the Plotly Library
import plotly.graph_objs as go
import chart_studio.plotly as py


# In[154]:


x = np.random.randn(2000)
y = np.random.randn(2000)
iplot([go.Histogram2dContour(x=x, y=y,
contours=dict (coloring='heatmap')),
go.Scatter(x=x, y=y, mode='markers',
marker=dict(color='white', size=3,opacity=0.3))], show_link=False)


# In[155]:


import plotly.offline as offline
import plotly.graph_objs as go
offline.plot({'data': [{'y': [14, 22, 30,44]}],'layout': {'title': 'Offline Plotly', 'font':
 dict(size=16)}}, image='png')


# In[156]:


from plotly import __version__
from plotly.offline import download_plotlyjs,init_notebook_mode, plot, iplot,init_notebook_mode
print (__version__)


# In[157]:


import plotly.graph_objs as go
plot([go.Scatter(x=[95, 77, 84], y=[75, 67, 56])])


# In[158]:


#basic plotting
df = pd.DataFrame(np.random.randn(200,6),index= pd.date_range('1/9/2009', periods=200), columns= list('ABCDEF'))
df.plot(figsize=(20, 10)).legend(bbox_to_anchor=(1, 1))


# In[159]:


#bar graph
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May'])
df.plot.bar(figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[160]:


#stacked bar graph
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May']) 
df.plot.bar(stacked=True,figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[161]:


#horizontal bar-plot
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May']) 
df.plot.barh(stacked=True,figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[162]:


#Using the Bar’s bins Attribute 
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May'])
df.plot.hist(bins= 20, figsize=(10,8)).legendbbox_to_anchor=(1.2, 1)


# In[163]:


#Multiple Histograms per Column
df=pd.DataFrame({'April':np.random.randn(1000)+1,'May':np.random.randn(1000),'June': np.random.randn(1000) - 1}, columns=['April','May', 'June'])
df.hist(bins=20)


# In[164]:


#creating boxplot
df = pd.DataFrame(np.random.rand(20,5),columns=['Jan','Feb','March','April', 'May'])
df.plot.box()


# In[165]:


#creating area plot
df = pd.DataFrame(np.random.rand(20,5),columns= ['Jan','Feb','March','April', 'May'])
df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3, 1))


# In[166]:


#Creating a Scatter Plot
df = pd.DataFrame(np.random.rand(20,5),columns= ['Jan','Feb','March','April', 'May'])
df.plot.scatter(x='Feb', y='Jan', title='Temperature over two months ')


# In[167]:


#Exercise
salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
df = pd.DataFrame()
df ['Name'] =salesMen
df ['Mobile_Sales'] = Mobile_Sales
df['TV_Sales']=TV_Sales
df.set_index("Name",drop=True,inplace=True)


# In[168]:


df


# In[169]:


#Create a bar plot of the sales volume
df.plot.bar( figsize=(20, 10), rot=0).legend(bbox_to_anchor=(1.1, 1))
plt.xlabel('Salesmen') 
plt.ylabel('Sales')
plt.title('Sales Volume for two salesmen in \nJanuary and April 2017')
plt.show()


# In[170]:


#Create a pie chart of item sales
df.plot.pie(subplots=True)


# In[171]:


#Create a box plot of item sales
df.plot.box()


# In[172]:


#Create an area plot of item sales
df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3,1))


# In[173]:


#Create a stacked bar plot of item sales
df.plot.bar(stacked=True, figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))

