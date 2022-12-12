#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project:  No-show appointments Data Analysis.
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# acacr# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.
# 
# >ScheduledDay : tells us on what day the patient set up their appointment.
# >Neighborhood : indicates the location of the hospital.
# >Scholarship : indicates whether or not the patient is enrolled in Brasilian welfare program Bolsa Família.
# 
# 
# ### Question(s) for Analysis
# > 1. What is the relationship between the Age of patients and the delay time for appointment?.
# > 2. How many patients showed up and didn't showed up for appointment?
# > 3. what's the distribution of Age_group among the gender of patients that was scheduled for appointment?
# > 4. which Age group showed up more for appointment and showed up less for appointment?
# > 5. What's the relationship between Age_group of patients and Delay time of appointments?
# 
# 

# In[1]:



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', 'inlineBackend.figure_sample = "reina"')


# The necessary library that will be used for both data analysis and visualization was imported into the Jupyter workspace.

# # <a id='wrangling'></a>
# ## Data Wrangling
# 
# 

# In[2]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.

df = pd.read_csv("noshowappointments-kagglev2-may-2016.csv")
df.head()

# This code is to read the no-show appointment data which is in CSV into a data frame


# In[3]:


df.describe()
# This code is to understand the no-show appointment better by using the describe function to show the aggregation of each coulmn.


# The code below is used to further understand the structure of each columnn in the no-show appointment data set. The info() function gives us the number of entries and data types of each column.

# In[4]:


df.info()


# In[5]:


df.shape


# I used the function shape() to know the number of columns and rows in the entire dataset.

# In[6]:


df.isna().any()


# The code above was used to further check for null in the dataset. This was achieved using the isna() function and the result shows that none of the column in the data set has a null value.

# In[7]:


df.duplicated()


# The data wrangling process will be incomplete without checking for duplicates data in the dataset. The code above was used to achieve this and the result shows that there is no duplicate data in the no- show appointment data.

# ## Data Cleaning.  

# In[8]:


df.head()


# In[9]:


df = df.drop(["PatientId","AppointmentID"],axis=1)


#  Considering the research questions for this project, the PatientId and the AppointmentID column were removed from the data set using the drop function.

# In[10]:


a = ["ScheduledDay","AppointmentDay"]

def change_date(x):
    for i in x:
        df[i] = df[i].apply(np.datetime64)
change_date(a)


# In[11]:


#a = ["ScheduledDay","AppointmentDay"]
#for i in a:
    #df[i] = df[i].apply(np.datetime64)


# The ScheduledDay and AppointmentDay column were converted from string to a datetime data type which is use for our analysis.

# In[12]:


df["delay_time"] = (df["AppointmentDay"] - df["ScheduledDay"]).dt.days


# The above code was used to add a new column named "delay_time" to the dataset. The column will contain the time between the appointment time and the scheduled time. This was done because it is important for answering our research question.

# In[13]:


df["No-show"] = df["No-show"].apply(lambda x: 0 if x == "No" else 1)


# In[14]:


df = df.loc[df["Age"] >= 0]

df["Age_group"] = pd.cut(df["Age"],bins=[0,14,24,64,200],labels=["children","youth","adults","seniors"])


# The Age column was grouped into different class which are : children,youth,adults and seniors. this is done using the code below and also because it's an important feature in our research question. The Age_group column was added to the dataset.

# In[15]:


df.head()


# The dataset was viewed after several cleaning using the code above.

# # <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# ### 1. What's the relationship between the Age of patients and the delay time for appointment?

# In[16]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findingsthe 


# In[17]:


df.plot(x="delay_time",y="Age",kind="scatter");
plt.title("Relationship between Age and Delay time")


# The relationship between the Age-group of the patients and the time between their appointment time and scheduled time is shown above. Looking at it, it is positively correlated

# ### 2. How many patients showed and didn't show up for appointment?

# In[18]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   invest


# In[19]:


print(df["No-show"].value_counts())


df["No-show"].value_counts().plot(kind="bar");
plt.xlabel("No-show")
plt.ylabel("Value_Count")
plt.title("A barchat showing those who kept and didn't keep the appointment")

The bar plot above showed that more patient showed up for their appointment.
0 represents Yes, 1 represents No.
# ### 3. What's the distribution of Age-group across the Gender of patients that was scheduled for appointment?

# In[20]:


sns.countplot(x="Age_group",hue="Gender", data=df);
plt.title("Distribution of Gender across the Age-group")


# In[21]:


df.Age_group.value_counts().plot(kind="bar");
plt.xlabel("Age_group")
plt.ylabel("Count")
plt.title("Distribution of Age-group")


# ###  4. Which Age group has the highest and lowest show up for appointment

# In[ ]:


sns.countplot(x="Age_group",hue="No-show", data=df);
plt.title("Relationship between the Age-group and No-show")


# ### 5. What's the relationship between the Age_group of patients and the delay time for appointment?

# In[ ]:


sns.boxplot(x="Age_group",y="delay_time",data=df)
plt.title("Relationship between the Age-group and delay time")


# # <a id='conclusions'></a>
# ## Conclusions
# At the end of the data analysis and visualization, I observed the following from the result:
# 1. I observed that the relationship between the age of patients scheduled for appointment and the delay time is probably correlated.
# 2. Also,more patients showed up for the scheduled appointment.
# 3. The Analysis and visualization also showed that more female adults patient are scheduled for appointment than the male.
# 4. It also showed that the youth showed up less for appointment and the adults showed up more.
# 
# 
# ## Limitation
# Enough information is not provided on the past datas of patients attendance which would have help conclude and determine a stronger factor for not showing up for appointments.
# 
# 
# 
# 
# 

# In[ ]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

