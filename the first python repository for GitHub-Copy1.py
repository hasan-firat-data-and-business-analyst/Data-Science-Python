#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(r'C:\Users\hasan\OneDrive\Masaüstü\Datasets\movies.csv')
df.head()


# In[7]:


#Let's see, if there is any missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col,pct_missing))


# In[8]:


for col in df.columns:
    pct_missing = np.sum(df[col].isnull())
    pct_absence = np.sum(df[col].notnull())
    print('{} : {} of {} rows is null in the {} column'.format(col,pct_missing,pct_absence,col))


# In[10]:


df.dtypes


# In[12]:


df1 = pd.read_csv(r'C:\Users\hasan\Downloads\mtcars.csv')
df1.head()


# In[13]:


df1.dtypes


# In[14]:


df1['mpg'] = df1['mpg'].astype('int64')


# In[15]:


df1.dtypes


# In[59]:


df1.head(20)


# In[16]:


df1.sort_values(by = ['disp'],inplace=False,ascending=False)


# In[38]:


df2 = pd.read_csv(r'C:\Users\hasan\OneDrive\Masaüstü\Datasets\TIFF_Festival_OFS_21-09-10 - in.csv')


# In[39]:


df2.head()


# In[40]:


df2['End Time'].drop_duplicates().sort_values(ascending=False)


# In[50]:


df2.drop_duplicates()


# In[61]:


plt.scatter(x= df1.disp, y=df1.hp)
plt.title('correlation')
plt.xlabel('displacement')
plt.ylabel('horse power')
plt.show()


# In[65]:


sns.regplot(x='disp',y='hp',data=df1,scatter_kws = {'color':'red'}, line_kws = {'color':'gray'} )


# In[66]:


df.corr()


# In[67]:


df1.corr()


# In[95]:


df1.iloc[:,0:5].corr()


# In[98]:


df1.iloc[:,[1,4]]


# In[99]:


df1.iloc[:,[1,4]].corr()


# In[105]:


df1[['mpg','hp']].corr()


# In[112]:


df.corr(method='kendall') #pearson, kendall,spearman


# In[113]:


df.corr(method='pearson')


# In[114]:


df.corr(method='spearman')


# In[117]:


correlation_matrix = df.corr(method='spearman')
sns.heatmap(correlation_matrix,annot=True)
plt.show()


# In[69]:


df2


# In[127]:


df3 =pd.read_csv(r'C:\Users\hasan\OneDrive\Masaüstü\Datasets\movies.csv')
df3


# In[135]:


df_numerized = df3

for col_name in df_numerized.columns:
    if (df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

df_numerized


# In[136]:


df3.info()


# In[137]:


df_numerized.info()


# In[138]:


correlation_mat = df_numerized.corr()
corr_pairs = correlation_mat.unstack()
corr_pairs


# In[139]:


sorted_pairs = corr_pairs.sort_values()
sorted_pairs


# In[141]:


high_cor = sorted_pairs[(sorted_pairs) > 0.5]
high_cor


# In[161]:


df_numerized.corr().unstack().sort_values()[(sorted_pairs) > 0.5]


# In[165]:


df.corr()


# In[182]:


#df1.iloc[:,[1,2,3,4]]
#[(df1.iloc[:,[1,2,3,4]].corr() > 0.5)]
df1.iloc[:,[1,2,3,4]].corr()


# In[178]:


df1[(df1.mpg > 18) & (df1.disp > 200)]


# In[ ]:




