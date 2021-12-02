#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv(r'Mall_Customers.csv')
df.head()


# # Univariate Analysis

# In[3]:


df.describe()


# In[4]:


sns.distplot(df['Annual Income (k$)'])


# In[5]:


df.columns


# In[6]:


columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    sns.distplot(df[i],bins= 10) 


# In[7]:


columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.distplot(df[i],label='columns',bins= 10)
    


# In[8]:


sns.kdeplot(df['Annual Income (k$)'],shade =True, hue = df['Gender'])


# In[9]:


columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    sns.kdeplot(df[i],shade =True, hue = df['Gender']) 


# In[10]:


columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.kdeplot(df[i],shade =True, hue = df['Gender']) 


# In[11]:


columns = ['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:    
    sns.boxplot(data = df,x='Gender',y = df[i])


# In[12]:


columns = ['Age', 'Spending Score (1-100)']
for i in columns:   
    plt.figure()
    sns.boxplot(data = df,x='Gender',y = df[i])


# In[13]:


df['Gender'].value_counts(normalize=True)


# # Bivariate Analysis

# In[14]:


sns.scatterplot(data=df, x = 'Annual Income (k$)',y ='Spending Score (1-100)')


# In[15]:


#df=df.drop('CustomerID',axis=1)


# In[16]:


sns.pairplot(df)


# In[17]:


sns.pairplot(df,hue= 'Gender')


# In[18]:


df.groupby(by='Gender',as_index=True)['Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()


# In[19]:


df.groupby(by='Gender',as_index=False)['Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()


# In[20]:


df.corr()


# In[21]:


df.groupby(by='Gender',as_index=False)['Age', 'Annual Income (k$)','Spending Score (1-100)'].corr()


# In[22]:


sns.heatmap(df.corr(),annot=True,cmap='coolwarm')


# # Clustering - Univariate, Bivariate, Multivariate

# In[23]:


clustering1 = KMeans(n_clusters = 6)


# In[24]:


clustering1.fit(df[['Annual Income (k$)']])


# In[25]:


clustering1.labels_


# In[26]:


df['Income Cluster'] = clustering1.labels_
df.head()


# In[27]:


df['Income Cluster'].value_counts()


# In[28]:


clustering1.inertia_


# In[29]:


intertia_score = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i)
    kmeans.fit((df[['Annual Income (k$)']]))
    intertia_score.append(kmeans.inertia_)


# In[30]:


intertia_score


# In[31]:


plt.plot(range(1,11),intertia_score)


# In[32]:


df.head()


# In[33]:


df.groupby('Income Cluster')['Age', 'Annual Income (k$)', 'Spending Score (1-100)'].mean()


# In[34]:


df.groupby('Income Cluster',as_index= False)['Age', 'Annual Income (k$)', 'Spending Score (1-100)'].mean()


# In[35]:


df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].corr()


# # Bivariate Clustering

# In[36]:


clustering2 = KMeans()
clustering2.fit(df[['Annual Income (k$)', 'Spending Score (1-100)']])
df['Spending and Income Cluster'] = clustering2.labels_
df.head()


# In[37]:


intertia_score2 = []
for i in range(1,11):
    kmeans2 = KMeans(n_clusters = i)
    kmeans2.fit((df[['Annual Income (k$)', 'Spending Score (1-100)']]))
    intertia_score2.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_score2)


# In[38]:


clustering2.cluster_centers_


# In[39]:


centers = pd.DataFrame(clustering2.cluster_centers_)
centers


# In[40]:


centers.corr()


# In[41]:


centers.columns= ['x','y']


# In[55]:


plt.figure(figsize= (12,10))
plt.scatter(x=centers['x'],y=centers['y'], s= 100, c= 'black',marker = '*')
sns.scatterplot(data=df,x ='Annual Income (k$)', y='Spending Score (1-100)' , hue ='Spending and Income Cluster' ,palette = 'tab10' )
plt.savefig('clustering_bivaraiate.png')


# In[43]:


pd.crosstab(df['Spending and Income Cluster'],df['Gender'],normalize='index')


# In[44]:


df.groupby('Spending and Income Cluster')['Age','Annual Income (k$)', 'Spending Score (1-100)'].mean()


# # Multivariate Clustering

# In[45]:


from sklearn.preprocessing import StandardScaler


# In[46]:


scale = StandardScaler


# In[47]:


df.head()


# In[48]:


dff = pd.get_dummies(df,drop_first=True)
dff.head()


# In[51]:


dff= dff[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender_Male']]
dff.head()


# In[52]:


dff = scale.fit_transform(dff)


# In[ ]:


dff = pd.DataFrame(scale.fit_transform(dff))


# In[53]:


intertia_score3 = []
for i in range(1,11):
    kmeans3 = KMeans(n_clusters = i)
    kmeans3.fit((df[['Annual Income (k$)', 'Spending Score (1-100)']]))
    intertia_score3.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_score2)


# In[54]:


df


# In[56]:


df.to_csv('clustering.csv')


# In[ ]:




