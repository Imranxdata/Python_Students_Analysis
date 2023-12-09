#!/usr/bin/env python
# coding: utf-8

# # STUDENTS SCORES ANALYSIS

# In[6]:


# Install necessary libraries using pip
# Make sure to run this in your command prompt or terminalif not alreayd installed

# Install NumPy for numerical operations
# pip install numpy

# Install Pandas for data manipulation and analysis
# pip install pandas

# Install Matplotlib for creating visualizations
# pip install matplotlib

# Install Seaborn for statistical data visualization
# pip install seaborn


# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # DATA STUDY AND IMPORTING

# In[6]:


df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# # DATA CLEANING

# In[10]:


# Check if the column exists before dropping
if 'Unnamed: 0' in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

# Print the DataFrame after dropping the column
print(df.head())


# # Transfromation

# In[11]:


# Replace value in the "WklyStudyHours" column
df['WklyStudyHours'] = df['WklyStudyHours'].str.replace(" 05-Oct", "5-10")

# Print the DataFrame after making the change
print(df.head())


# # ANALYSIS

# In[12]:


#1.GENDER DISTRIBTUION

# Set the size of the plot
plt.figure(figsize=(8, 6))

# GENDER DISTRIBUTION
ax = sns.countplot(data=df, x="Gender")

# Show count values on top of the bars
ax.bar_label(ax.containers[0])

plt.xlabel("Gender")  # Add x-axis label for clarity
plt.title("Gender Distribution") #for chart title
plt.show()


# In[ ]:


#FROM THE ABOVE CHART WE HAVE ANALYSED THAT NUMBER OF FEMALE IN DATA IS MORE THAN MALES


# In[13]:


#2 IMPACT OF PARENTS EDUCATION ON STUDENTS SCORE
gb = df.groupby("ParentEduc").agg({
    "MathScore": 'mean',
    "ReadingScore": 'mean',
    "WritingScore": 'mean'
})
print(gb)


# In[14]:


#To see the Above infoamtion in visual form
sns.heatmap(gb, annot = True)
plt.title("Relationship between Parent Education and student Score") #for chart title
plt.show()


# In[ ]:


#The chart analysis indicates that the education level of parents has a positive influence on their children's scores.


# In[15]:


#3 IMPACT OF PARENTS MARITAL STATUS ON STUDENTS SCORE
gb1 = df.groupby("ParentMaritalStatus").agg({
    "MathScore": 'mean',
    "ReadingScore": 'mean',
    "WritingScore": 'mean'
})
print(gb1)

#To see the Above infoamtion in visual form
sns.heatmap(gb1, annot = True)
plt.title("Relationship between Parent Marital status and student Score") #for chart title
plt.show()


# In[ ]:


#Both table and heat chart show same informtion
#WE have concluded that there is no/negligible impact on the student's score due to their parents marital status


# In[16]:


#4 Outliers subjectwise
#boxplot is a useful visualization for identifying outliers in a dataset
#for Mathcscore
sns.boxplot(data = df,x ="MathScore")
plt.show()

#for Readingscore
sns.boxplot(data = df,x ="ReadingScore")
plt.show()

#for Writingscore
sns.boxplot(data = df,x ="WritingScore")
plt.show()


# In[18]:


#5.Distribution of Ethnic Group 
print(df["EthnicGroup"].unique())


# In[81]:


# Count occurrences for each ethnic group
group_counts = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
group_labels = [f'{label}\n({count} - {100 * count / sum(group_counts):.1f}%)' for label, count in zip(["Group A", "Group B", "Group C", "Group D", "Group E"], group_counts)]

# Plot a pie chart without specifying colors
plt.figure(figsize=(8, 8))
plt.pie(group_counts, labels=group_labels, autopct='', startangle=140)
plt.title('Distribution of Ethnic Groups')
plt.show()


# In[ ]:


#"The pie chart illustrates the distribution of ethnic groups, indicating the count and percentage representation
#of each group among the surveyed population."

