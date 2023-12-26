#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
from time import strftime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# In[2]:


base_data = pd.read_csv('Data.csv')


# In[3]:


base_data


# In[4]:


base_data.shape


# In[5]:


base_data.info()


# In[6]:


#modifying the date and time into standard form
base_data['ScheduledDay'] = pd.to_datetime(base_data['ScheduledDay']).dt.date.astype('datetime64[ns]')
base_data['AppointmentDay'] = pd.to_datetime(base_data['AppointmentDay']).dt.date.astype('datetime64[ns]')


# In[7]:


base_data.head(5)


# In[8]:


# 5 is Saturday, 6 is Sunday 

base_data['sch_weekday'] = base_data['ScheduledDay'].dt.dayofweek


# In[9]:


base_data['app_weekday'] = base_data['AppointmentDay'].dt.dayofweek


# In[10]:


base_data['sch_weekday'].value_counts()


# In[11]:


base_data['app_weekday'].value_counts()


# In[12]:


base_data.columns


# In[13]:


#changing the name of some cloumns
base_data= base_data.rename(columns={'Hipertension': 'Hypertension', 'Handcap': 'Handicap', 'SMS_received': 'SMSReceived', 'No-show': 'NOshow'})


# In[14]:


base_data.columns


# In[15]:


base_data.info()


# In[16]:


# dropping some columns which have no significance
base_data.drop(['PatientId', 'AppointmentID', 'Neighbourhood'], axis=1, inplace=True)


# In[17]:


base_data


# In[18]:


base_data.describe()


# In[19]:


base_data['NOshow'].value_counts().plot(kind='barh', figsize=(8, 6))
plt.xlabel("Count", labelpad=14)
plt.ylabel("Target Variable", labelpad=14)
plt.title("Count of TARGET Variable per category", y=1.02);


# In[20]:


# calculating the % of appointments or not 
100*base_data['NOshow'].value_counts()/len(base_data['NOshow'])


# In[27]:


base_data['NOshow'].value_counts()


# In[32]:


# Having a look that data contains missing values or not
missing = pd.DataFrame((base_data.isnull().sum())*100/base_data.shape[0]).reset_index()
plt.figure(figsize=(16, 5))
ax = sns.pointplot(x='index', y=0, data=missing)
plt.xticks(rotation=90, fontsize=7)
plt.title("Percentage of Missing values")
plt.ylabel("PERCENTAGE")
plt.show()


# In[33]:





# In[40]:


#Create a copy of base data for manupulation & processing
new_data = base_data.copy()


# In[34]:


new_data.info()


# In[ ]:





# In[41]:


# Get the max tenure
print(base_data['Age_group'].max()) #72


# In[48]:


list(base_data.columns)


# In[49]:


#having a loook into the values of count of each columns and there count in respect to NoShow column
for i, predictor in enumerate(base_data.drop(columns=['NOshow'])):
    print('-'*10,predictor,'-'*10)
    print(base_data[predictor].value_counts())    
    plt.figure(i)
    sns.countplot(data=base_data, x=predictor, hue='NOshow')

