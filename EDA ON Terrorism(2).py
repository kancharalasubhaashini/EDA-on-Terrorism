#!/usr/bin/env python
# coding: utf-8

# # Task-Exploratory Data Analysis

# # Author: KANCHARALA SUBHAASHINI

# IMPORTING LIBRARIES

# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Importing the dataset

# In[24]:


terrorism_df=pd.read_csv(r"C:\Users\ksubh\OneDrive\Desktop\globalterrorismdb_0718dist.csv")


# In[25]:


pd.set_option('display.max_columns',None)


# In[26]:


terrorism_df


# In[27]:


terrorism_df.shape


# In[28]:


pd.set_option('display.max_columns',None)


# In[29]:


terrorism_df.info()


# In[30]:


terrorism_df.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'State','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','success':'Success','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)


# In[31]:


terrorism_df.columns


# # DATA CLEANING

# In[32]:


terrorism_df.isnull().sum()


# In[33]:


#filling null values
terrorism_df['Wounded'] = terrorism_df['Wounded'].fillna(0)
terrorism_df['Killed'] = terrorism_df['Killed'].fillna(0)
terrorism_df['Casualities'] = terrorism_df['Killed'] + terrorism_df['Wounded']
terrorism_df['State'].fillna("unknown", inplace = True)


# In[34]:


terrorism_df.head()


# In[35]:


terrorism_df.dropna(axis=1, inplace=True)


# In[36]:


terrorism_df


# In[37]:


terrorism_df


# In[38]:


terrorism_df.shape


# In[39]:


terrorism_df.describe()


# # DATA VISUALIZATION

# In[40]:


#countrywise attacks visualization 
plt.rcParams["figure.figsize"] = 15, 11
sns.barplot(x = terrorism_df["Country"].value_counts()[:20].index, y=terrorism_df["Country"].value_counts()[:20].values)
plt.ylabel("Number of Attacks", fontsize=18)
plt.xticks(rotation=90)
plt.xlabel("Attack Region", fontsize=18)
plt.title("Country wise Attacks", size=25, fontweight="bold")


# In[41]:


#number of deaths over the years Visualization
df =terrorism_df [['Year','Killed']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4)
plt.xticks(rotation = 50)
plt.title("People Died Due To Attack",fontsize=25)
plt.ylabel("Number of killed peope",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)


# In[42]:


# number of attacks over the years Visualization
year =terrorism_df['Year'].unique()
years_count = terrorism_df['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year,
           y = years_count,
           palette = "tab10")
plt.xticks(rotation = 50)
plt.xlabel('Attacking Year',fontsize=20)
plt.ylabel('No. of Attacks Each Year',fontsize=20)
plt.title('Attacks In Years',fontsize=30)
plt.show()


# In[43]:


#Total number of various terror attacks
Killed =terrorism_df.pivot_table(columns='AttackType', values='Killed', aggfunc='sum')
Killed


# In[44]:


#Total number of persons killed by terror attacks per country
countryKill =terrorism_df.pivot_table(columns='Country', values='Killed', aggfunc='sum')
countryKill


# RESULT

# Country with the most attacks: Iraq

# City with the most attacks: Baghdad

# Region with the most attacks: Middle East & North Africa

# In[ ]:




