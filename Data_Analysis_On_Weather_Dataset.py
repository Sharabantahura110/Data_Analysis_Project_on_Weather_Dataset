#!/usr/bin/env python
# coding: utf-8

# # The Weather Dataset
# 
# Here, The Weather Dataset is a time-series data set with per hour information about the weather condition at a particular location. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure and Conditions. 
# 
# This data is available as a CSV file. I have analysed this data set using the Pandas Data frame.

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"/Users/sharabantahura/Downloads/file.csv")


# 

# In[3]:


data


# In[4]:


data.head()


# In[6]:


data.shape


# In[7]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[12]:


data['Weather'].unique()


# In[13]:


data.nunique()


# In[14]:


data.count()


# In[16]:


data['Weather'].value_counts()


# # Question 1
# Find all the unique ‘Wind Speed’ values in the data

# In[19]:


data.head(3)


# In[18]:


data.info()


# In[20]:


data['Wind Speed_km/h'].nunique()


# In[21]:


data['Wind Speed_km/h'].unique()


# # Question 2
# Find the number of times when the ‘Weather is exactly Clear’.

# In[22]:


#value_counts()
data.Weather.value_counts()


# In[25]:


#filtering
data[data.Weather == 'Clear']


# In[26]:


#groupby()
data.groupby('Weather').get_group('Clear')


# # Question 3
# Find the number of times when the ‘Wind Speed was exactly 4km/h’

# In[38]:


data[data['Wind Speed_km/h'] == 4]


# # Question 4
# Find out all the Null Values in the data.

# In[41]:


data.isnull().sum()


# In[43]:


data.notnull().sum()


# # Question 5
# Rename the column name ‘Weather’ of the data frame to ‘Weather Condition.’

# In[49]:


data.rename(columns = {'Weather' :'Weather Condition'}, inplace = True)


# In[50]:


data.head(5)


# # Question 6
# What is the mean ‘Visibility’?

# In[51]:


data.Visibility_km.mean()


# # Question 7
# What is the Standard Deviation of ‘Pressure’ in this data?

# In[52]:


data.Press_kPa.std()


# # Question 8
# What is the Variance of ‘Relative Humidity’ in this data?

# In[53]:


data['Rel Hum_%'].var()


# # Question 9
# Find all instances when ’Snow’ was recorded.

# In[54]:


data['Weather Condition'].value_counts()


# In[55]:


data[data['Weather Condition'] == 'Snow']


# In[56]:


data[data['Weather Condition'].str.contains('Snow')]


# In[57]:


data.head(50)


# In[59]:


data.tail(3)


# # Question 10
# Find all instances when ‘Wind Speed is above 24’ and ‘Visibility is 25’.

# In[61]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[65]:


data.head(7)


# In[71]:


data.groupby(Visibility_km).mean()


# In[72]:


data.columns


# In[1]:


data.groupby('Weather Condition').max()


# # Question 11
# What is the Minimum & Maximum value of each column against each ‘Weather Condition’?

# In[78]:


data.groupby('Weather Condition').min()


# In[80]:


data.groupby('Weather Condition').max()


# # Question 12
# Show all the Records where Weather Condition is Fog.

# In[84]:


data[data['Weather Condition'] == 'Fog']


# # Question 13
# Find all instances when ‘Weather is Clear’ or ‘Visibility is above 40.’

# In[86]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] == 40)]


# # Question 14
# Find all instances when:
# A. ‘Weather is Clear’ and ‘Relative Humidity is greater than 50’
# 
# Or
# 
# B. ‘Visibility is above 40’

# In[89]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]


# In[93]:


data.groupby('Weather Condition').min()


# In[ ]:




