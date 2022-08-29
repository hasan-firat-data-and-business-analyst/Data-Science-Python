#!/usr/bin/env python
# coding: utf-8

# # <div class="alert alert-success" role="alert"><b> HASAN FIRAT - Data Analyst & Engineer </div>

# <div class="alert alert-success" role="alert"><b>      
#     
# [LinkedIn](https://www.linkedin.com/in/hasan-firat-1952a0224/)  
#     
# </div>

# <div class="alert alert-success" role="alert"><b>      
#     
# [GitHub](https://github.com/hasan-firat-data-and-business-analyst) 
#     
# </div>    

# <div class="alert alert-success" role="alert"><b>      
#     
# [Dataset](https://github.com/hasan-firat-data-and-business-analyst/Data-Science-Python/blob/main/auto.csv) 
#   
# </div>      
#  

# # <div class="alert alert-block alert-info"><b> Pandas: Zero to Hero </div> 

# ## <div class="alert alert-block alert-info"><b> 1 - Introduction </div> 

# ### <div class="alert alert-block alert-info"><b> Pandas </div> 

# <div class="alert alert-block alert-info"><b>  Pandas</b> is <b>fast, powerful, flexible </b> and <b>easy to use</b> open source library for data manipulation and analysis. It is a Python package that offers various data structures and operations for manipulating numerical data and time series. It is mainly popular for importing and analyzing data much easier. Pandas is fast and it has high-performance & productivity for users.
# 
# [Reference](https://pandas.pydata.org/)
#     
# [Reference](https://www.geeksforgeeks.org/pandas-tutorial/?ref=lbp) </div>

# ### <div class="alert alert-block alert-info"><b> History </div> 

# <div class="alert alert-block alert-info"><b></b> Developer Wes McKinney started working on pandas in 2008 while at AQR Capital Management out of the need for a high performance, flexible tool to perform quantitative analysis on financial data. Before leaving AQR he was able to convince management to allow him to open source the library.
# 
# [Reference](https://en.wikipedia.org/wiki/Pandas_(software))  </div> 

# ### <div class="alert alert-block alert-info"><b> A. Data Structures in Python </div> 

# ![Python%20Data%20Structures.png](attachment:Python%20Data%20Structures.png)

# ##### <div class="alert alert-block alert-info"><b> 1. Primitive Data Structures </b> 

# ######  <div class="alert alert-block alert-info"><b> a. Float or Floating Point </div> 

# <div class="alert alert-block alert-info"><b> A floating point (known as a float) number </b> has decimal points even if that decimal point value is 0. Such as, 8.85 , 458.001 or 521.10002 for example.   </div> 
# 
# 

# In[1]:


floating_point = 11.0
print(floating_point)
print(type(floating_point))


# ###### <div class="alert alert-block alert-info"><b> b. Integer </div> 

# <div class="alert alert-block alert-info"><b>An integer </b> does not have a decimal point. If we are willing to use 45.99 as an integer, it would be stored as 45. Such as, in integer types 9999.999 would be stored as 9999 or 10.0000000001 would be stored as 10, for example.
# 
# <b>Note:</b> You will often see the data type **Int64** in Python which stands for 64 bit integer. The 64 refers to the memory allocated to store data in each cell which effectively relates to how many digits it can store in each “cell”. Allocating space ahead of time allows computers to optimize storage and processing efficiency.
# [Reference](https://datacarpentry.org/python-ecology-lesson/04-data-types-and-format/#numeric-data-types)    
# 
# [For more knowledge](https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html)
# 
# </div>
# 

# In[2]:


integer = 11
print(integer)
print(type(integer))


# ###### <div class="alert alert-block alert-info"><b> c. Boolean </div> 

# <div class="alert alert-block alert-info"> In computer science, <b>the Boolean</b> (sometimes shortened to <b>Bool</b>) is a data type that has one of two possible values (usually denoted true and false) which is intended to represent the two truth values of logic and Boolean algebra.  
#     
# [Reference](https://en.wikipedia.org/wiki/Boolean_data_type) </div>

# In[3]:


print(2 > 1)
print(15 == 16)
print(100 < 19) 


# ###### <div class="alert alert-block alert-info"><b> d. String (Text) Data Types </div> 

# <div class="alert alert-block alert-info"> <b>Text data type</b> is known as <b> Strings in Python</b>, or <b>Objects in Pandas</b>. Strings can contain numbers and / or characters. For example, a string might be a word, a sentence, or several sentences.
# 
# Note: Strings that contain numbers can not be used for mathematical operations!!!
# 
# [Reference](https://datacarpentry.org/python-ecology-lesson/04-data-types-and-format/#numeric-data-types) </div>

# In[4]:


text_data_types = "1,2,"'DATA'""
print(text_data_types)
print(type(text_data_types))


# ##### <div class="alert alert-block alert-info"><b> 2. Non - Primitive Data Structures </b> 

# ###### <div class="alert alert-block alert-info"><b> 2.1 Built-In Data Structures </b> 

# ######  <div class="alert alert-block alert-info"><b> a. List </div> 

# <div class="alert alert-block alert-info"> <b>A list </b> in Python is a collection of items which can contain elements of multiple data types, which may be either numeric, character logical values, etc. 
#     
# [Reference](https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/) 
# 
# Lists have a number of important characteristics:
# 
#  1. List items are <b>enclosed </b> in square brackets, like this [item1, item2, item3].
# 
#  2. Lists are <b>ordered</b> – i.e. the items in the list appear in a specific order. This enables us to use an index to access to any item.
# 
#  3. Lists are <b>mutable</b>, which means you can add or remove items after a list's creation.
# 
#  4. List elements <b>do not need to be unique</b>. Item duplication is possible, as each element has its own distinct place and can be accessed separately through the index.
# 
#  5. Elements can be of <b>different data types</b>: you can combine strings, integers, and objects in the same list.
# 
# [Reference](https://learnpython.com/blog/python-array-vs-list/)
# 
# </div>

# In[5]:


List_example_1 = [1,2.72,3,'Zurich','Toronto','San Francisco',True]

print(List_example_1)
print(type(List_example_1))


# ######  <div class="alert alert-block alert-info"><b> b. Tuple </div> 

# <div class="alert alert-block alert-info"> 
# <b>Tuples </b> are used to store multiple items in a single variable.
# 
# A tuple is a collection which is <b>ordered</b> and <b>unchangeable/immutable</b>.
#     
# A tuple can have any number of items and they may be of different types (<b>integer, float, list, string, etc.</b>).
# 
# Tuples are written with <b>round brackets</b>.
#     
# [Reference](https://www.w3schools.com/python/python_tuples.asp)
#     
# [Reference](https://www.programiz.com/python-programming/tuple)
# 
# 
# 
# </div>

# In[6]:


Tuple_example_1 = (1,2,3,'Toronto','Zurich','Paris')
print(Tuple_example_1)
print(type(Tuple_example_1))


# ######  <div class="alert alert-block alert-info"><b> c. Dictionary </div> 

# <div class="alert alert-block alert-info">
# <b>Dictionaries </b> are used to store data values in key:value pairs.
# 
# A dictionary, which is <b>ordered, changeable and do not allow duplicates</b>, is a collection.[Reference](https://www.w3schools.com/python/python_dictionaries.asp)
# 
#      
# Creating a dictionary is as simple as placing items inside <b>curly braces {} </b>separated by commas.
# 
# An item has a key and a corresponding value that is expressed as <b>a pair (key: value)</b>.[Reference](https://www.programiz.com/python-programming/dictionary)
#  
# 
# <b>Note:</b> As of Python version 3.7, dictionaries are <b>ordered</b>. In Python 3.6 and earlier, dictionaries are unordered.
# [Reference](https://www.w3schools.com/python/python_dictionaries.asp)
# 
# 
# 
# 
# 
#  </div> 

# In[7]:


Dictionary_example = {'City':['Zurich','Toronto'], 
                      'Country':['Swiss','Canada'], 
                      'Continental':['Europa','North America']}
print(Dictionary_example)
print(type(Dictionary_example))


# ######  <div class="alert alert-block alert-info"><b> d. Set </div> 

# <div class="alert alert-block alert-info">  
# 
# <b> A set</b> is an unordered collection of items. Every set element is <b> unique (no duplicates)</b> and must be <b>immutable (cannot be changed)</b> and <b>unindexed</b>.
# 
# However, a set itself is mutable. We can <b>add</b> or <b>remove</b> items from it.
# 
# Sets can also be used to perform<b> mathematical</b> set operations like union, intersection, symmetric difference, etc.
# 
# It can have any number of items and they may be of <b>different types (integer, float, tuple, string etc.)</b>. But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
# </div>

# In[8]:


Set_example = {1,2,3,'Basel',1.1}
print(Set_example)
print(type(Set_example))


# ######  <div class="alert alert-block alert-info"><b> The Summary of Data Structures' Features </div> 

# <div class="alert alert-block alert-info">
# 
# | LIST | TUPLE | DICTIONARY | SET |
# | :- | -: | :- | -: |
# | Mutable | Immutable | Mutable | Immutable |
# | Ordered | Ordered | Ordered | Unordered |
# | Int., Boole, String, Float, etc. | Int., Boole, String, Float, etc. | Int., Boole, String, Float, etc. | Int., Boole, String, Float, etc. |
# |Square Brackets  | Round Brackets | Curvy Braces | Curvy Braces |
# | List_1 = [1, 2.22, 'exp']  | Tuple_1 = (1, 2.22, 'exp') | Dictionary_1 = {'City':[1, 2.2, 'exp']} | Set_1 = {1, 2.2, 'exp'} | 
#     
#     
# </div> 
# 

# ###  <div class="alert alert-block alert-info"><b> B. Data Structures in Pandas </div> 

# <div class="alert alert-block alert-info"><b> </b> A data structure is a collection of data values and defines the relationship between the data, and the operations that can be performed on the data. 
# 
# There are three main data structures in pandas:
#  - 1. Series - 1D
#  - 2. DataFrame - 2D
#  - 3. Panel - 3D
#  
# [Reference](https://medium.com/data-science-365/pandas-for-data-science-part-1-89bc231b3478) </div>
# 
# 
# 

# ####  <div class="alert alert-block alert-info"><b> 1. Series - 1D </div> 

# <div class="alert alert-block alert-info"><b> </b> One-dimensional ndarray with axis labels (including time series).
# 
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) </div>

# In[9]:


import pandas as pd
import numpy as np


# In[10]:


series = {'a':[1,11], 'b':[2,22], 'c':[3,33]}

pandas_series = pd.Series(series)
print(pandas_series)

print(type(pandas_series))


# ####  <div class="alert alert-block alert-info"><b> 2. DataFrame - 2D </div>

# <div class="alert alert-block alert-info"><b> </b> Two-dimensional, size-mutable, potentially heterogeneous tabular data.
# 
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) </div>
# 
# 

# In[11]:


pandas_dataframe = pd.DataFrame(series)
pandas_dataframe


# In[12]:


type(pandas_dataframe)


# #### <div class="alert alert-block alert-info"><b> 3. Panel - 3D </div>

# <div class="alert alert-block alert-info"><b> </b> Represents wide format panel data, stored as 3-dimensional array.                    
#     
# [Reference](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.Panel.html)
# 
# 
#     
# Panel is deprecated. Hence, the recommended way to represent these types of 3-dimensional data is to use multi-indexing in DataFrames instead of Panels. A multi-indexed DataFrame can be directly converted to a Panel via DataFrame.to_panel() method.
#     
# [Reference](https://medium.com/data-science-365/pandas-for-data-science-part-1-89bc231b3478)
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html)    
# 
# [Reference](https://pandas.pydata.org/docs/user_guide/advanced.html)    
#     
# 
# Note: The panel has been removed from Pandas module 0.25.0 onwards.
#     
#     
# [Reference](https://www.geeksforgeeks.org/python-pandas-panel-shape/)
#  </div>

# ![Screenshot%202022-05-25%20at%2017-51-51%20Python%20Pandas%20-%20Panel.png](attachment:Screenshot%202022-05-25%20at%2017-51-51%20Python%20Pandas%20-%20Panel.png)
# 
# 
# [For more knowledge](https://www.tutorialspoint.com/python_pandas/python_pandas_panel.htm)

# ## <div class="alert alert-success" role="alert"> 2 - Reading CSV Files </div>

# <div class="alert alert-success" role="alert"> Import Pandas Library and label it as 'pd' </div>

# In[13]:


import pandas as pd


# <div class="alert alert-success" role="alert"> 
# In this part, you need to download the dataset. Keep in mind where the file is on your computer because as we need to specify the location of the file in Jupyter notebook in order to load the data.
#     
# [dataset](https://github.com/hasan-firat-data-and-business-analyst/Data-Science-Python/blob/main/auto.csv). 
# 
# 
# </div>

# In[14]:


reading_csv_files_example = pd.read_csv(r'auto.csv') 


# <div class="alert alert-success" role="alert"> 'head()' shows the first five rows of the dataframe by default but you can specify the number of rows in the parenthesis.
#  </div>

# In[15]:


reading_csv_files_example.head()


# <div class="alert alert-success" role="alert"> 'tail()' shows the bottom five rows by default.
#  </div>

# In[16]:


reading_csv_files_example.tail()


# <div class="alert alert-success" role="alert"> we are good to use in the function of 'head()' and 'tail()' in any numbers.
#  </div>

# In[17]:


reading_csv_files_example.head(3)


# In[18]:


reading_csv_files_example.tail(7)


# <div class="alert alert-success" role="alert"> 'shape' function tells us how many rows and columns exist in a dataframe.
#  </div>

# In[19]:


reading_csv_files_example.shape


# ## <div class="alert alert-warning" role="alert"> 3 - Pandas DataFrame 
# ###  <div class="alert alert-warning" role="alert"> 3.1 - Data Structure Transformation in Pandas 
# #### <div class="alert alert-warning" role="alert"> 3.1.1 - Dictionary to DataFrame </div>

# <div class="alert alert-warning" role="alert"> Checking the Pandas Version out </div>

# In[20]:


print(pd.__version__)


# <div class="alert alert-warning" role="alert"> Creating dictionary for using in the example and checking the data structure's type of example out  </div>

# In[21]:


dict_example = { 'Country': ["Canada", "Germany", "Japan"],
               'Continent': ["North America", "Europe", "Asia"]}


# In[22]:


print(dict_example)
print(type(dict_example))


# <div class="alert alert-warning" role="alert"> Changing types of dictionary to Pandas DataFrame and checking out the last data structure  </div>

# In[23]:


dictionary_to_df = pd.DataFrame(dict_example)
dictionary_to_df


# In[24]:


type(dictionary_to_df)


# #### <div class="alert alert-warning" role="alert"> 3.1.2 - Dictionary to Pandas Series  </div>

# <div class="alert alert-warning" role="alert"> Creating the new dictionary for new example  </div>

# In[25]:


dict_example_for_Pandas_Series = {'Name': ["John","Sebastian","Rayn"],
                                 'Place': ["London", "Vienna","Oslo"]}

print(dict_example_for_Pandas_Series)
print(type(dict_example_for_Pandas_Series))


# <div class="alert alert-warning" role="alert"> Changing the dictionary data structure to Pandas Series  </div>

# In[26]:


dictionary_to_series = pd.Series(dict_example_for_Pandas_Series)

print(dictionary_to_series)
print(type(dictionary_to_series))


# #### <div class="alert alert-warning" role="alert"> 3.1.3 - List to DataFrame  </div>

# <div class="alert alert-warning" role="alert"> Creating the list with only number elements </div>

# In[27]:


list_example = [1,2,3,4,5,6,7,8,9]

print(list_example)
print(type(list_example))


# <div class="alert alert-warning" role="alert"> Transformation of the list to Pandas DataFrame  </div>

# In[28]:


list_example_df = pd.DataFrame(list_example)


# In[29]:


list_example_df


# In[30]:


type(list_example_df)


# <div class="alert alert-warning" role="alert"> Creating the other list with both numbers and string elements </div>

# In[31]:


list_example2 = [1,2,3,4,"Zurich"]

list_example2


# <div class="alert alert-warning" role="alert"> The transformation of the new list to Pandas DataFrame </div>

# In[32]:


list_example_df2 = pd.DataFrame(list_example2)
list_example_df2


# In[33]:


type(list_example_df2)


# #### <div class="alert alert-warning" role="alert"> 3.1.4 - List to Pandas Series </div>

# <div class="alert alert-warning" role="alert"> Creating the new list with only numbers </div>

# In[34]:


list_example_for_series = [11,22,33,44,55,66,77,88,99]

print(list_example_for_series)
print(type(list_example_for_series))


# <div class="alert alert-warning" role="alert"> The list to Pandas Series </div>

# In[35]:


list_to_series = pd.Series(list_example_for_series)

print(list_to_series)
print(type(list_to_series))


# <div class="alert alert-warning" role="alert"> Creating the other list with numbers and strings </div>

# In[36]:


list_example_for_series2 = [11,22,33,"Asia","Africa"]

print(list_example_for_series2)
print(type(list_example_for_series2))


# <div class="alert alert-warning" role="alert"> List to Pandas Series </div>

# In[37]:


list_to_series2 = pd.Series(list_example_for_series2)

print(list_to_series2)
print(type(list_to_series2))


# ### <div class="alert alert-warning" role="alert"> 3.2 Creating the Pandas DataFrame </div>

# #### <div class="alert alert-warning" role="alert"> 3.2.1 - Text Dataframe </div>

# In[38]:


dict_for_dataframe_text = {'Name':["Carlos","David","Emma"],
                           'City':["New York","Tokyo","Berlin"]}

pandas_dataframe_example_text = pd.DataFrame(dict_for_dataframe_text, index = ['User 1','User 2','User 3'])

pandas_dataframe_example_text


# #### <div class="alert alert-warning" role="alert"> 3.2.2 - The First Way </div>

# In[39]:


pandas_dataframe_example = pd.DataFrame({'ID':  [100,101,102,103],
                                         'Math':[99,76,88,98],
                                         'Geo': [78,98,90,89],
                                         'Literature':[98,87,76,77]
                                        })
                                         
pandas_dataframe_example                           


# #### <div class="alert alert-warning" role="alert"> 3.2.3 - The Second Way </div>

# In[40]:


dict_for_dataframe = {'ID':[100,101,102,103],'Math':[99,76,88,98],'Geo': [78,98,90,89],'Literature':[98,87,76,77]}

pandas_dataframe_example2 = pd.DataFrame(dict_for_dataframe)
pandas_dataframe_example2


# #### <div class="alert alert-warning" role="alert"> 3.2.4 - The Third Way </div>

# In[41]:


import numpy as np
pandas_dataframe_example3 = pd.DataFrame([[100,99,78,98],[101,76,98,87],[102,88,90,76],[103,98,89,77]],
                                         columns =['ID','Math','Geo','Literature'],index = np.random.rand(4))

pandas_dataframe_example3


# #### <div class="alert alert-warning" role="alert"> 3.2.5 - Using Orient Index and Columns </div>

# In[42]:


dict_for_dataframe2 = {'ID':[100,101,102,103],'Math':[99,76,88,98],'Geo': [78,98,90,89],'Literature':[98,87,76,77]}
pandas_dataframe_example4 = pd.DataFrame.from_dict(dict_for_dataframe2,orient = 'columns')
pandas_dataframe_example4


# In[43]:


dict_for_dataframe2 = {'ID':[100,101,102,103],'Math':[99,76,88,98],'Geo': [78,98,90,89],'Literature':[98,87,76,77]}
pandas_dataframe_example4 = pd.DataFrame.from_dict(dict_for_dataframe2,orient = 'index')
pandas_dataframe_example4


# ### <div class="alert alert-warning" role="alert"> 3.3 The Columns in Pandas </div>

# #### <div class="alert alert-warning" role="alert"> 3.3.1 - Creating The DataFrame Example </div>

# In[44]:


dict_for_dataframe = {'ID':[100,101,102,103],'Math':[99,76,88,98],'Geo': [78,98,90,89],'Literature':[98,87,76,77]}

dataframe_column_example = pd.DataFrame(dict_for_dataframe)
dataframe_column_example


# #### <div class="alert alert-warning" role="alert"> 3.3.2 - Renaming The Columns </div>

# In[45]:


renanaming_column_example = dataframe_column_example.rename(columns = {'Geo': 'Geography'}  )

renanaming_column_example


# #### <div class="alert alert-warning" role="alert"> 3.3.3 - Dropping The Columns  </div>

# In[46]:


dropping_example = dataframe_column_example.drop(columns = 'Literature')

dropping_example


# #### <div class="alert alert-warning" role="alert"> 3.3.4 - Adding The Columns  </div>

# In[47]:


dataframe_column_example['Data Science'] = [99,96,94,100]

dataframe_column_example


# ### <div class="alert alert-warning" role="alert"> 3.4 - Index in Pandas and Indexing </div>

# #### <div class="alert alert-warning" role="alert"> 3.4.1 - Creating the New DataFrame </div>

# In[48]:


dataframe_index_example = pd.DataFrame({
    
    'Name':["Emma","Maddy","Cassy","Tony","Montana","Carl"],
    'Location':["Toronto","Toronto","Zurich","Zurich","New York","Zurich"],
    'Sex':["Female","Female","Female","Male","Male","Male"],
    'Education':['PhD','Bachelor','Master','PhD','Master','Postgrad'],
    'Marital Status':['Single','Married','Divorced','Divorced','Single','Married'],
    'Profession':['Teacher','Lawyer','Engineer','Medical Doctor','Nurse','Business Owner'],
    'Annual Revenue - USD':[100000, 456000,768000,560000,240000,7600000],
    'Children Status':["yes","yes","no","yes","yes","yes"],
    'The Number of Children':[1,1,2,4,2,3],
    'Far from home - km':[124,36,85,777,25,12]
    
                                       })

dataframe_index_example


# #### <div class="alert alert-warning" role="alert"> 3.4.2 - Set Index </div>

# <div class="alert alert-warning" role="alert"> 
# 
# To set a column as index for a DataFrame, use DataFrame.set_index() function, with the column name passed as argument.
# Pandas DataFrame - Set Column as Index
# 
# You can also setup MultiIndex with multiple columns in the index. In this case, pass the array of column names required for index, to set_index() method.
# 
# [Reference](https://pythonexamples.org/pandas-set-column-as-index/)
# 
# </div>

# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# In[49]:


dataframe_index_example2 = dataframe_index_example.set_index('The Number of Children' )
dataframe_index_example2


# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# In[50]:


dataframe_index_example3 = dataframe_index_example.set_index((dataframe_index_example['The Number of Children'] == 2) )
dataframe_index_example3


# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# In[51]:


dataframe_index_example4 = dataframe_index_example.set_index((dataframe_index_example['Children Status'] == 'yes') )
dataframe_index_example4


# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# In[52]:


dataframe_set_index_example5 = dataframe_index_example.set_index(['Education','Location'])
dataframe_set_index_example5


# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# In[53]:


dataframe_set_index_example6 = dataframe_index_example.set_index(
    ['Marital Status',
    dataframe_index_example['Annual Revenue - USD'] > 300000])

dataframe_set_index_example6


# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# In[54]:


dataframe_set_index_example7 = dataframe_index_example.set_index(
    ['Marital Status',
    dataframe_index_example['Annual Revenue - USD'] > 300000,'Location'])

dataframe_set_index_example7


# In[55]:


dataframe_set_index_example8 = dataframe_index_example.set_index(
    ['Marital Status',
    dataframe_index_example['Annual Revenue - USD'] > 300000,
     'Location',
    dataframe_index_example['Far from home - km'] > 75
    ])

dataframe_set_index_example8


# <div class="alert alert-warning" role="alert"> 
# Set Index Example 
# 
# </div>

# <div class="alert alert-warning" role="alert"> 
#     NOTE:
# If we do not use ' [ ] ' (square brackets) with multiple column selection, as you are able to see on the below example, we can get only the first columns name, which is written in the set_index function.
#     
#    
# 
# </div>

# In[56]:


dataframe_set_index_example9 = dataframe_index_example.set_index('Sex','Location')
dataframe_set_index_example9


# #### <div class="alert alert-warning" role="alert"> 3.4.3 - Dropping the Rows </div>

# <div class="alert alert-warning" role="alert"> 
# 
# The drop() function is used to drop specified labels from rows or columns.
# 
# Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level. 
#     
# [Reference](https://www.w3resource.com/pandas/dataframe/dataframe-drop.php)
#     
#    
# 
#     
# The drop() method removes the specified row or column.
# 
# By specifying the column axis (axis='columns'), the drop() method removes the specified column.
# 
# By specifying the row axis (axis='index'), the drop() method removes the specified row.
#     
# [Reference](https://www.w3schools.com/python/pandas/ref_df_drop.asp)
#     
# </div>

# In[57]:


dataframe_index_example


# <div class="alert alert-warning" role="alert"> Dropping the row </div>

# In[58]:


dataframe_index_dropping_example6 = dataframe_index_example.drop(0)
dataframe_index_dropping_example6


# <div class="alert alert-warning" role="alert"> 
# Above example, we has dropped the first row, the number of index is 0 (zero). Please, check " dataframe_index_example " example out.
# 
#     
# NOTE: This method is used for only " ONE ROW ". If you want to add more row or index number for dropping, it needs to be written in " [ ] " square brackets.
# </div>

# In[59]:


dataframe_index_dropping_example6_more_rows = dataframe_index_example.drop([0,2,3])
dataframe_index_dropping_example6_more_rows


# <div class="alert alert-warning" role="alert"> 
# 
# 
#     
# NOTE: This method is used for only " ONE ROW ". If you want to add more row or index number, it needs to be written in " [] " square brackets.
# </div>

# <div class="alert alert-warning" role="alert"> Dropping the row </div>

# In[60]:


dataframe_index_dropping_example7 = dataframe_index_example.drop(5, axis='index')
dataframe_index_dropping_example7


# <div class="alert alert-warning" role="alert"> 
# In above example, we has dropped the fifth row by using the other way of dropping function, the number of index is 5 (five). 
#     
# Please, check " dataframe_index_example " example out.
# 
# </div>

# In[61]:


dataframe_index_dropping_example8 = dataframe_index_example.drop(index=([1,4,5]))
dataframe_index_dropping_example8


# <div class="alert alert-warning" role="alert"> 
# In the last example, we has dropped the first, fourth and fifth rows by using the dropping function with index, the number of index is 1,4, and 5. 
#     
# Please, check " dataframe_index_example " example out.
# 
# </div>

# <div class="alert alert-warning" role="alert"> 
# Dropping the column
# </div>

# In[62]:


dataframe_index_dropping_example9 = dataframe_index_example.drop("Profession" , axis='columns')
dataframe_index_dropping_example9


# <div class="alert alert-warning" role="alert"> 
# In the first dropping column example, we used " axis = 'columns' " in " drop() method " to remove the specified column.
# </div>

# In[63]:


dataframe_index_dropping_example10 = dataframe_index_example.drop(["Children Status", "Education"], axis=1)
dataframe_index_dropping_example10


# <div class="alert alert-warning" role="alert"> 
# In the second example to drop the column, we used " drop() method " to remove the "Children Status", and "Education" columns.
# </div>

# In[64]:


dataframe_index_dropping_example11 = dataframe_index_example.drop(columns = ["Sex","Location"])
dataframe_index_dropping_example11


# <div class="alert alert-warning" role="alert"> 
# In the last example, we used " columns = ["_","_"] " in " drop() method " to remove the "Sex", and "Location" columns.
# </div>

# 

# In[65]:


dataframe_index_dropping_example11 = dataframe_index_example.drop(1, axis='index')
dataframe_index_dropping_example11


# <div class="alert alert-warning" role="alert"> 
# Dropping the row and column at the same time
# </div>

# In[66]:


dataframe_index_dropping_example12 = dataframe_index_example.drop(
    index = [1,3,5],
    columns=["Sex","Marital Status", "Annual Revenue - USD"])

dataframe_index_dropping_example12


# <div class="alert alert-warning" role="alert"> 
# In this example, we have learned how to drop both the rows and columns at the same time in the same code block. This examples can be extended with the other kind of dropping syntax.
# </div>

# #### <div class="alert alert-warning" role="alert"> 3.4.4 - Adding the Rows </div>

# #### <div class="alert alert-warning" role="alert"> Adding the Rows  </div>

# In[67]:


df_for_adding_example = pd.DataFrame({
    'Name':["Albert"],
    'Location':["London"],
    'Sex':["Male"],
    'Education':["Bachelor"],
    'Marital Status':["Single"],
    'Profession':["Lawyer"],
    'Annual Revenue - USD': [158000],
    'Children Status': ["no"],
    'The Number of Children': [0]
}) 

df_for_adding_example


# In[68]:


dataframe_index_adding_example = dataframe_index_example.append(df_for_adding_example,ignore_index=False)
dataframe_index_adding_example


# <div class="alert alert-warning" role="alert"> 
#     
# In the above example, if we use " ignore_index " as " False ", the new row, that has added, is shown as " zero (0) " on the last row in the DataFrame.    
# 
# </div>

# In[69]:


dataframe_index_adding_example2 = dataframe_index_example.append(df_for_adding_example,ignore_index=True)
dataframe_index_adding_example2


# <div class="alert alert-warning" role="alert"> 
#     
# In the above example, if we use " ignore_index " as " True ", the new row, that has added, is shown as " 6 " on the last row in the DataFrame.    
# 
# </div>

# <div class="alert alert-warning" role="alert"> 
#     
# Renaming the Index   
# 
# </div>

# In[70]:


giving_a_name_for_index_example = pd.DataFrame({'Name':['Carlos','David','Emma'],
                                              'City':['New York','London','Berlin'],
                                              'Sex':['Male','Male','Female']},
                                            index = ['Status 1','Status 2', 'Status3']
                                            )

giving_a_name_for_index_example


# <div class="alert alert-warning" role="alert"> 
#     
# The Second Example for Renaming the Index   
# 
# </div>

# In[71]:


giving_a_name_for_index_example2 = pd.DataFrame({'Name':['Carlos','David','Emma'],
                                              'City':['New York','London','Berlin'],
                                              'Sex':['Male','Male','Female']},
                                            index = ['The first row','the 2nd Row',3]
                                            )

giving_a_name_for_index_example2


# <div class="alert alert-warning" role="alert"> 
#     
# The Third Example for Renaming the Index   
# 
# </div>

# In[72]:


example_label = [99,88,77,66,55,44,33,22,11]
example_label


# In[73]:


type(example_label)


# In[74]:


labels = pd.Series(example_label, index = ["a","b","c",4,5,6,"x","y","z"])
labels


# In[75]:


type(labels)


# In[76]:


labels2 = pd.DataFrame(example_label, index = ["a","b","c",4,5,6,"x","y","z"])
labels2


# In[77]:


type(labels2)


# <div class="alert alert-warning" role="alert"> 
#     Creating the example for reset index function
# </div>

# In[78]:


reset_index_example = pd.DataFrame({'Name':['Carlos','David','Emma'],
                                              'City':['New York','London','Berlin'],
                                              'Sex':['Male','Male','Female']},
                                            index = ['The first row','the 2nd Row',3]
                                            )

reset_index_example


# <div class="alert alert-warning" role="alert"> 
#     Using the reset index function
# </div>

# In[79]:


reset_index_example.reset_index(drop=True,inplace=True)

reset_index_example


# ### <div class="alert alert-warning" role="alert"> 3.5 - Selecting and Filtering Columns and Rows in a Data Frame
# </div>

# #### <div class="alert alert-warning" role="alert"> 3.5.1 - Index-Based Selection with iloc
# </div>

#  <div class="alert alert-warning" role="alert"> ILOC : 
#     
# Purely integer-location based indexing for selection by position.
#     
# .iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
#  
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
# </div>

#  <div class="alert alert-warning" role="alert"> 
# Using the existence dataframe
# </div>

# In[80]:


reading_csv_files_example.head()


#  <div class="alert alert-warning" role="alert"> 
#     
#     
# The Row Selection
#     
#     
# In this below example, we are going to select the second and the third row.
# </div>

# In[81]:


reading_csv_files_example.iloc[2:4]


#  <div class="alert alert-warning" role="alert"> 
#     
#     
# The Column Selection
#     
# In this below example, we are going to select the columns, that are in between second and the sixth columns with all rows.
#     
# NOTE: Be careful, " num-of-doors " is the 5th column, not the 6th. When we apply this code block as you are going to see that, the column selection will stop the fifth column, even if we have written " 6 (six) " in the code block. It is a Pandas feature.
# </div>

# In[82]:


reading_csv_files_example.iloc[:,2:6]


#  <div class="alert alert-warning" role="alert"> 
#     
#     
# The Column and The Row Selection
#     
# In this below example, we are going to select the rows, that are in between the sixth and the eleventh rows, and the columns, like " wheel-base, lenght, and width".
#     
# NOTE: Be careful, the last column " width " is the 11th column, not the 12th. More information about it has been given in the previous example.
# </div>

# In[83]:


reading_csv_files_example.iloc[6:12,9:12]


#  <div class="alert alert-warning" role="alert"> 
#  Reverse Row Selection with iloc
# </div>

# In[84]:


reading_csv_files_example.iloc[-7:]


#  <div class="alert alert-warning" role="alert"> 
# When it comes to selection of the column reversely, you do not need to start counting at the zero, you good to start at one (1). In above example, the seventh rows is 194 and do not forget to use " - (minus) ".
#     
# On the other hand, when we apply " reverse selection ", as you can see that numbers start at minus one, but when it comes to, normal selection, it starts at zero.
# </div>

# ![PythonStringindex.JPEG](attachment:PythonStringindex.JPEG)

#  <div class="alert alert-warning" role="alert"> 
#  Reverse Column Selection with iloc
# </div>

# In[85]:


reading_csv_files_example.iloc[77:81,-3:]


#  <div class="alert alert-warning" role="alert"> 
#  In this above example, we have selected the rows, being between 77th and 81st rows, and the columns starting at the last one to the third one. The minus in this code block provides the REVERSE selection. That's why the DataFrame is being shown as reversely. 
# </div>

#  <div class="alert alert-warning" role="alert"> 
#  The Second Example for Reverse Column Selection with iloc
# </div>

# In[86]:


reading_csv_files_example.iloc[-2:,-2:]


#  <div class="alert alert-warning" role="alert"> 
# In this second example, we have selected the last two columns and rows in the DataFrame. If I need to draw an analogy, we selected the right bottom edge of  the DataFrame.
# </div>

#  <div class="alert alert-warning" role="alert"> 
# The Third Example with iloc
# </div>

# In[87]:


reading_csv_files_example.iloc[-44:-40,-5:-2]


# <div class="alert alert-warning" role="alert"> 
#     
# In this third example, 
#     
# we have started to select at 44th, the name of rows is 160, and it has stopped at 40, namely the name of row is 157. 
#   
# When it comes to columns, it has started at 5, that is " city-mpg " and it has stopped at 5 or " horsepower ".
#     
# Do not forget that when you apply the reverse selection, you need to think the process reversely.
#     
# </div>

# #### <div class="alert alert-warning" role="alert"> 3.5.2 - Label-based Selection with loc function
# </div>

# <div class="alert alert-warning" role="alert"> 
# Access a group of rows and columns by label(s) or a boolean array.
# 
# .loc[] is primarily label based, but may also be used with a boolean array.   
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
#     
# </div>

# In[88]:


loc_function_example = pd.DataFrame({
    'Name':['Carlos','David','Emma','Chaplin','Gogol','Gabriel'],
     'City':['New York','London','Berlin','Tokyo','Moscow','Aracataca'],
      'Sex':['Male','Male','Female','Male','Male','Male']},
       index = ['The first row','the 2nd Row',3,'okay','The Overcoat','One Hundred Years of solitude']
                                            )

loc_function_example


# <div class="alert alert-warning" role="alert"> 
#     
# The Row Selection with loc 
# </div>

# In[89]:


loc_function_example.loc[[3,'okay','The Overcoat']]


# <div class="alert alert-warning" role="alert"> 
#     
# In this above example, when we apply the loc function in Pandas, we need to write the exact column name inside quotes down, othervise we fail to get the DataFrame.
#     
# On the other hand, as you can see that, we are able to get the column name in order to in code block.
# </div>

# <div class="alert alert-warning" role="alert"> 
#     
# The Column Selection
# </div>

# In[90]:


loc_function_example.loc[:,['Name']]


# In[91]:


loc_function_example.loc[:,['Name','Sex']]


# <div class="alert alert-warning" role="alert"> 
#     
# The Row and Column Selection
# </div>

# In[92]:


loc_function_example.loc[['One Hundred Years of solitude'],['Name','City']]


# <div class="alert alert-warning" role="alert"> 
#     
# Conditional Selection
# </div>

# In[93]:


reading_csv_files_example.head()


# <div class="alert alert-warning" role="alert"> 
#     
# The First Example
# </div>

# In[94]:


reading_csv_files_example[reading_csv_files_example['horsepower'] == 111]


# <div class="alert alert-warning" role="alert"> 
#     
# The Second Example
# </div>

# In[95]:


reading_csv_files_example[
    
        (reading_csv_files_example.bore == 3.47) & 
        (reading_csv_files_example.price == 16500)
    
    ]


# <div class="alert alert-warning" role="alert"> 
#     
# Multiple Conditional Selection
# </div>

# In[96]:


reading_csv_files_example[
    (reading_csv_files_example['normalized-losses'] > 170) & 
    ((reading_csv_files_example['wheel-base'] > 90) & (reading_csv_files_example['wheel-base'] < 100) &
    ((reading_csv_files_example.stroke > 3.11) | (reading_csv_files_example.stroke<= 3.40)))
]


# <div class="alert alert-warning" role="alert"> 
#     
# Multiple Conditional Selection - 2
# </div>

# In[97]:


reading_csv_files_example[ 
    ((reading_csv_files_example['aspiration'] == 'std') & (reading_csv_files_example['body-style'] == 'convertible')) |
    ((reading_csv_files_example['drive-wheels'] == 'rwd') & (reading_csv_files_example['fuel-system'] == 'spdi'))]


# <div class="alert alert-warning" role="alert"> 
#     
# isin function
# </div>

# <div class="alert alert-warning" role="alert"> 
# isin is used to filter data frames. isin() method helps in selecting rows with having a particular(or Multiple) value in a particular column.
#   
# [Reference](https://www.geeksforgeeks.org/python-pandas-dataframe-isin/)
# </div>

# In[98]:


isin_function_example = pd.DataFrame({'Legs': [2, 4,2], 'Wings': [2, 0,2]},
                  index=['Eagle', 'Dog','Ostrich'])
isin_function_example 


# In[99]:


isin_function_example.isin([1])


# In[100]:


isin_function_example.isin([1,2,3])


# In[101]:


isin_function_example.isin({'Wings':[0,3,5]})


# In[102]:


isin_function_example.isin({'Wings':[1],'Legs':[4,2]})


# <div class="alert alert-warning" role="alert"> 
# 
# In above five examples, we have applied many kind of different legs and wings' numbers for filtering in the DataFrame. If the number, has been written down by ourself is correct, we can see that, it is being written as " True ". If not, we are able to get " False " as output.
# </div>

# In[103]:


isin_function_example2 = reading_csv_files_example["make"].isin(['isuzu'])

reading_csv_files_example[isin_function_example2]


# <div class="alert alert-warning" role="alert"> 
# 
# In above example, we have selected " isuzu ", which is being in the row of " make ".
#     
# </div>

# In[104]:


isin_function_example3 = reading_csv_files_example["make"].isin(['renault','saab'])

reading_csv_files_example[isin_function_example3]


# <div class="alert alert-warning" role="alert"> 
# 
# In above example, we have selected " renault " and " saab " , which is being in the row of " make ".
#     
# </div>

# <div class="alert alert-warning" role="alert"> 
# 
# Str Accessor
#     
#     
# </div>

# <div class="alert alert-warning" role="alert"> 
# 
# Pandas is a highly efficient library on textual data as well. 
# The functions and methods under the str accessor provide flexible ways to filter rows based on strings.
# For instance, we can select the names that starts with the words “do” in below example.
#     
# </div>

# In[105]:


reading_csv_files_example[reading_csv_files_example['make'].str.startswith('do')]


# <div class="alert alert-warning" role="alert"> 
# 
# In above example, we have filtered the cars starting with two letters, like " do ",  in make column. 
#     
# </div>

# In[106]:


reading_csv_files_example[reading_csv_files_example['make'].str.endswith('ge')]


# <div class="alert alert-warning" role="alert"> 
# 
# In above example, we have selected the cars, ending with " ge " in make column by using " endswith() ".
#     
# </div>

# In[107]:


reading_csv_files_example[reading_csv_files_example['body-style'].str.startswith('c')]


# In[108]:


reading_csv_files_example[reading_csv_files_example['make'].str.endswith('u')]


# In[208]:


reading_csv_files_example[reading_csv_files_example['engine-location'].str.startswith('r')]


# In[221]:


reading_csv_files_example[reading_csv_files_example['body-style'].str.startswith('c')]


# <div class="alert alert-warning" role="alert"> 
# 
# Query
#     
# </div>

# <div class="alert alert-warning" role="alert"> 
# 
# The query() method allows you to query the DataFrame and takes a query expression as a string parameter, which has to evaluate to either True of False.
#     
# [Reference](https://www.w3schools.com/python/pandas/ref_df_query.asp)
# 
#  
#     
#     
# The query function offers a little more flexibility at writing the conditions for filtering. 
# We can pass the conditions as a string.
# 
# </div>
# 
# 
# 
# 
# 

# <div class="alert alert-warning" role="alert"> 
# 
# The below example is a basic example for query method. 
# 
# </div>

# In[111]:


reading_csv_files_example.query('horsepower > 200')


# <div class="alert alert-warning" role="alert"> 
# 
# In the second example, we are going to learn how to apply " Multiple Condtion Filtering " .
# </div>

# In[112]:


reading_csv_files_example.query('stroke > 3.5 and price < 15000 and aspiration == "turbo" ')


# <div class="alert alert-warning" role="alert"> 
# 
# In the third example, we are going to combine the filtering with using query method and filtering without using query method.
# </div>

# <div class="alert alert-warning" role="alert"> 
# 
# Combining the filtering with using query method 
# </div>

# In[113]:


reading_csv_files_example.query('bore == stroke')


# <div class="alert alert-warning" role="alert"> 
# 
# Combining the filtering without using query method 
# </div>

# In[114]:


reading_csv_files_example[reading_csv_files_example['bore'] == reading_csv_files_example['stroke']]


# <div class="alert alert-warning" role="alert"> 
# 
# In the above last two examples, as we can see that, we good to filter DataFrame with both using or not using query method.
# </div>

# In[115]:


reading_csv_files_example[
    (reading_csv_files_example['stroke'] > 3.5) &
    (reading_csv_files_example['price'] < 15000)&
    (reading_csv_files_example['aspiration'] == 'turbo')]


# <div class="alert alert-warning" role="alert"> 
# 
# In the above last two examples, we have operate the Multiple Condition Filtering without using query method.
# 
# NOTE: More knowledge and examples will be given in the next chapter.
# </div>

# <div class="alert alert-warning" role="alert"> 
# 
# Nlargest or nsmallest
# </div>

# <div class="alert alert-warning" role="alert"> 
# 
# 
# 
# In some cases, we do not have a specific range for filtering but just need the largest or smallest values. 
# 
# The nlargest and nsmallest functions allow for selecting rows that have the largest or smallest values in a column,respectively.
# 
#     
#     
# </div>

# In[116]:


reading_csv_files_example.nlargest(4, 'wheel-base')


# In[117]:


reading_csv_files_example.nsmallest(3, 'normalized-losses') 


# In[118]:


reading_csv_files_example.nsmallest(7,'engine-size')


# <div class="alert alert-warning" role="alert"> select_dtypes() Method
# </div>

# <div class="alert alert-warning" role="alert"> 
# This function return a subset of the DataFrame’s columns based on the column dtypes. The parameters of this function can be set to include all the columns having some specific data type or it could be set to exclude all those columns which has some specific data types.
#     
#     
# [Reference](https://www.geeksforgeeks.org/python-pandas-dataframe-select_dtypes/)
# </div>

# In[119]:


reading_csv_files_example.info()


# In[120]:


select_dtypes_example = reading_csv_files_example.select_dtypes(include='float64')

select_dtypes_example


# In[121]:


select_dtypes_example2 = reading_csv_files_example.select_dtypes(include='bool')

select_dtypes_example2


# In[122]:


select_dtypes_example3 = reading_csv_files_example.select_dtypes(include='int64')

select_dtypes_example3


# In[123]:


select_dtypes_example4 = reading_csv_files_example.select_dtypes(include='object')

select_dtypes_example4


# ## <div class="alert alert-block alert-info"><g>    4 - Math and Descriptive Statistics </div> 

# <div class="alert alert-block alert-info"><g>   Import the Dataset </div> 

# In[124]:


reading_csv_files_example.head()


# <div class="alert alert-block alert-info"><g>   Shape Method:
#     
# Return a tuple representing the dimensionality of the DataFrame.
# 
# [Reference](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.shape.html)
#     </div> 

# In[125]:


reading_csv_files_example.shape


# <div class="alert alert-block alert-info"><g>   Describe Method:
#     
# It returns description of the data in the DataFrame.
# 
# If the DataFrame contains numerical data, the description contains these information for each column:
# 
# count - The number of not-empty values.
# mean - The average (mean) value.
# std - The standard deviation.
# min - the minimum value.
# 25% - The 25% percentile*.
# 50% - The 50% percentile*.
# 75% - The 75% percentile*.
# max - the maximum value.
# 
# *Percentile meaning: how many of the values are less than the given percentile. Read more about percentiles in our Machine Learning Percentile chapter.
#   
# [Reference](https://www.w3schools.com/python/pandas/ref_df_describe.asp)
# 
# </div> 

# In[126]:


reading_csv_files_example.describe()


# <div class="alert alert-block alert-info"><g>   In question columns with " describe()" method </div> 

# In[127]:


reading_csv_files_example[['bore','stroke','price']].describe()


# <div class="alert alert-block alert-info"><g>   Info method:
#     
#     
# It prints information about the DataFrame.
# 
#     
# The information contains the number of columns, column labels, column data types, memory usage, range index, and the number of cells in each column (non-null values).
# 
# [Reference](https://www.w3schools.com/python/pandas/ref_df_info.asp)
#     
#     
#     
# </div> 

# In[128]:


reading_csv_files_example.info()


# <div class="alert alert-block alert-info"><g>   Unique method:
#     
# Return unique values based on a hash table.    
# 
#     
#     
#     
# </div> 

# In[129]:


reading_csv_files_example["make"].unique()


# <div class="alert alert-block alert-info"><g>   Nunique method:
#     
# The nunique() method returns the number of unique values for each column.
# 
# By specifying the column axis (axis='columns'), the nunique() method searches column-wise and returns the number of unique values for each row.
#     
# [Reference](https://www.w3schools.com/python/pandas/ref_df_nunique.asp)
#     
#     
# </div> 

# In[130]:


reading_csv_files_example["make"].nunique()


# <div class="alert alert-block alert-info"><g>   value_counts() method:
#     
# Return a Series containing counts of unique values.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)
#     
# </div> 

# In[131]:


reading_csv_files_example["make"].value_counts()


# <div class="alert alert-block alert-info"><g>   Sum() method:
#     
# Return the sum of the values over the requested axis.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)
#     
# </div> 

# In[132]:


reading_csv_files_example["horsepower"].sum()


# <div class="alert alert-block alert-info"><g>   count() method:
#     
# Count non-NA cells for each column or row.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html)
#     
# </div> 

# In[133]:


reading_csv_files_example["horsepower"].count()


# <div class="alert alert-block alert-info"><g>   max() method:
#     
# Return the maximum of the values over the requested axis.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html)
#     
# </div> 

# In[134]:


reading_csv_files_example[['horsepower']].max()


# <div class="alert alert-block alert-info"><g>   min() method:
#     
# Return the minimum of the values over the requested axis.    
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html)
#     
# </div> 

# In[135]:


reading_csv_files_example[['horsepower']].min()


# <div class="alert alert-block alert-info"><g>   mean() method:
#     
# Count non-NA cells for each column or row.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html)
#     
# </div> 

# In[136]:


reading_csv_files_example[['horsepower']].mean()


# <div class="alert alert-block alert-info"><g>   median() method:
#     
# Return the median of the values over the requested axis.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)
#     
# </div> 

# In[137]:


reading_csv_files_example[['horsepower']].median()


# <div class="alert alert-block alert-info"><g>   mode() method:
#     
# Get the mode(s) of each element along the selected axis.
# 
# The mode of a set of values is the value that appears most often. It can be multiple values.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html)
#     
# </div> 

# In[138]:


reading_csv_files_example[['horsepower']].mode()


# <div class="alert alert-block alert-info"><g>   std() method:
#     
# Return sample standard deviation over requested axis.
# 
# Normalized by N-1 by default. This can be changed using the ddof argument.
# 
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)
#     
# </div> 

# In[139]:


reading_csv_files_example[['horsepower']].std()


# <div class="alert alert-block alert-info"><g>   std() method:
# Aggregate
#     
# </div> 

# <div class="alert alert-block alert-info"><g>   
# Aggregate function:
# That is used to apply some aggregation across one or more column. Aggregate using callable, string, dict, or list of string/callables. Most frequently used aggregations are:
# 
# sum: Return the sum of the values for the requested axis
# min: Return the minimum of the values for the requested axis
# max: Return the maximum of the values for the requested axis
#     
# [Reference](https://www.geeksforgeeks.org/python-pandas-dataframe-aggregate/)
#     
# </div>  
#  
#  
#  
#  

# In[140]:


reading_csv_files_example[["horsepower"]].aggregate(['min'])


# In[141]:


reading_csv_files_example[["horsepower"]].aggregate(['max'])


# In[142]:


reading_csv_files_example[["horsepower"]].aggregate(['sum'])


# In[143]:


reading_csv_files_example[["horsepower"]].aggregate(['count'])


# In[144]:


reading_csv_files_example[["horsepower"]].aggregate(['std'])


# In[145]:


reading_csv_files_example[["horsepower"]].aggregate(['median'])


# In[146]:


reading_csv_files_example[["horsepower"]].aggregate(['mode'])


# <div class="alert alert-block alert-info"><g>   
# Aggregate function with Groupby method:
# 
# Grouping and aggregating will help to achieve data analysis easily using various functions. These methods will help us to the group and summarize our data and make complex analysis comparatively easy. 
#     
#     
# [Reference](https://www.geeksforgeeks.org/grouping-and-aggregating-with-pandas/)
# </div>  
#  
#  
#  
#  

# In[147]:


reading_csv_files_example.groupby(by = "make")[['horsepower']].aggregate(['min'])


# In[148]:


reading_csv_files_example.groupby(by = "make")[['horsepower']].aggregate(['max'])


# In[149]:


reading_csv_files_example.groupby(by = "make")[['horsepower']].aggregate(['median'])


# In[150]:


reading_csv_files_example.groupby(by = "make")[['horsepower']].aggregate(['mean'])


# <div class="alert alert-block alert-info"><g>   
# corr() method:
# That is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
# 
# [Reference](https://www.geeksforgeeks.org/python-pandas-dataframe-corr/)
# 
# 
# 
# </div>  
#  
#  
#  
#  

# In[151]:


reading_csv_files_example.corr()


# ## <div class="alert alert-success" role="alert"> 5 - Date Time </div>

# <div class="alert alert-success" role="alert"> Convert argument to datetime </div>
# 

# In[152]:


import datetime


# <div class="alert alert-success" role="alert"> " now() " method provides the current date and time </div>
# 

# In[153]:


date_time_example = pd.DataFrame({'Date':[datetime.datetime.now()]})

date_time_example


# <div class="alert alert-success" role="alert"> " now().year " method provides the current year </div>
# 

# In[154]:


date_time_example2 = pd.DataFrame({'Date':[datetime.datetime.now().year]})

date_time_example2


# <div class="alert alert-success" role="alert"> " strftime("%A") " method provides the current day </div>
# 

# In[155]:


date_time_example3 = pd.DataFrame({'Date':[datetime.datetime.now().strftime("%A")]})

date_time_example3


# <div class="alert alert-success" role="alert"> " strftime("%B") " method provides the current month </div>

# In[156]:


date_time_example4 = pd.DataFrame({'Date':[datetime.datetime.now().strftime("%B")]})

date_time_example4


# <div class="alert alert-success" role="alert"> " strftime("%C") " method provides the current year </div>
# 

# In[157]:


date_time_example5 = pd.DataFrame({'Date':[datetime.datetime.now().strftime("%C")]})

date_time_example5


# <div class="alert alert-success" role="alert"> " strftime("%A") " method provides the current date </div>
# 

# In[158]:


date_time_example6 = pd.DataFrame({'Date':[datetime.datetime.now().strftime("%D")]})

date_time_example6


# <div class="alert alert-success" role="alert"> The other example with " strftime("%A") " method for specific date </div>
# 

# In[159]:


date_time_example_current_time = pd.DataFrame({'Date':[datetime.datetime(2022,5,10)]})

date_time_example_current_time


# In[160]:


date_time_example7 = pd.DataFrame({'Date':[datetime.datetime(2022,5,10).strftime("%A")]})

date_time_example7


# In[161]:


date_time_example8 = pd.DataFrame({'Date':[datetime.datetime(2022,5,10).strftime("%B")]})

date_time_example8


# In[162]:


date_time_example9 = pd.DataFrame({'Date':[datetime.datetime(2022,5,10).strftime("%C")]})

date_time_example9


# In[163]:


date_time_example10 = pd.DataFrame({'Date':[datetime.datetime(2022,5,10).strftime("%D")]})

date_time_example10


# In[164]:


date_time_example11 = pd.DataFrame({'Date':[datetime.datetime(2022,9,2),
                                           datetime.datetime(2021,8,3),
                                           datetime.datetime(2020,7,4),
                                           datetime.datetime(2019,6,5),
                                           datetime.datetime(2018,5,6)],
                                   'City':['London','Berlin','Toronto','New York','Zurich']
                                  })

date_time_example11


# <div class="alert alert-success" role="alert"> The determination of the exact year, month, day and day of week in datetime method() example</div>
# 

# In[165]:


date_time_example11['Year'] = date_time_example11['Date'].dt.year
date_time_example11['Month'] = date_time_example11['Date'].dt.month
date_time_example11['Day'] = date_time_example11['Date'].dt.day
date_time_example11['Day of week'] = date_time_example11['Date'].dt.dayofweek

date_time_example11


# ##  <div class="alert alert-block alert-info"><g> 6 - Grouping and Sorting </div> 

# In[166]:


reading_csv_files_example.head(2)


# ###  <div class="alert alert-block alert-info"><g> 6.1 - Groupby </div> 

# <div class="alert alert-block alert-info"><g> A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
#  
# </div> 

# In[167]:


reading_csv_files_example.groupby('make')[['horsepower']].mean()


# ###   <div class="alert alert-block alert-info"><g> 6.2 - Sort_values Function  </div> 

# <div class="alert alert-block alert-info"><g> Sort by the values along either axis
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
#     </div> 

# In[168]:


reading_csv_files_example.sort_values("normalized-losses", 
                                      ascending = False, inplace = False, 
                                      na_position ='last')


# In[169]:


reading_csv_files_example.groupby('make')[
    ["horsepower","price"]].mean().sort_values(
    "horsepower",ascending=False,inplace=False)


# In[170]:


reading_csv_files_example.groupby('make')[
    ["horsepower","price"]].mean().sort_values(
    "price",ascending=False,inplace=False)


# ##  <div class="alert alert-block alert-danger"> 7 - Data Types </div>
# 
# 
# 

#  <div class="alert alert-block alert-danger"> 
#     
# What are the most common data types that you will see in pandas?
# 
#  1. int64 (integer)
#     
#  2. float64 (floating point number)
# 
#  3. object (string)
#     
#  4. datetime (datetime)
#     
#  5. bool (true or false)
# 
# We can convert a column of one type into another using the astype function. </div>
# 
# 

#  <div class="alert alert-block alert-danger"> 
#     
# In below example, we are able to find the data types of columns out with the help of " .dtypes " function.
# 
# 
# </div>
# 
# 

# In[171]:


reading_csv_files_example.dtypes


#  <div class="alert alert-block alert-danger"> 
#     
# Moreover, in the other  example, we are able to find the data types of the exact column out with the help of " .dtypes " function.
# 
# 
# </div>
# 
# 

# In[172]:


reading_csv_files_example['symboling'].dtypes


#  <div class="alert alert-block alert-danger"> 
#     
# Converting the Columns' Data Types
# 
# </div>
# 
# 

# <div class="alert alert-block alert-danger"> 
#     
# Astype Function:
#     
# This method is used to cast a pandas object to a specified dtype. astype() function also provides the capability to convert any suitable existing column to categorical type.
# 
# </div>

# In[173]:


reading_csv_files_example['symboling'].astype('float64')


# In[174]:


reading_csv_files_example['height'].astype('int64')


# <div class="alert alert-block alert-danger"> 
#     
# We good to combine the data types after the changing them by using " astype " function with the help of the below table.
# 
# </div>

# In[175]:


reading_csv_files_example.info()


# ## <div class="alert alert-success" role="alert"> 8 - Combining DataFrame 
#     
# </div>
# 
# 
# 
# 

# ### <div class="alert alert-success" role="alert"> 8.1 -  Concat   </div>

# <div class="alert alert-success" role="alert"> Concatenate pandas objects along a particular axis with optional set logic along the other axes.
# 
# Can also add a layer of hierarchical indexing on the concatenation axis, which may be useful if the labels are the same (or overlapping) on the passed axis number.
# 
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)    
#     
# </div>

# In[176]:


concat_example1 = {'Name': ['Rebekka','Katie'],'City': ['Toronto','Zurich']}

concat_example2 = {'Name': ['Carl','Gustav'],'City': ['New York','Basel']}


# In[177]:


df_concat1 = pd.DataFrame(concat_example1)
df_concat1


# In[178]:


df_concat2 = pd.DataFrame(concat_example2)
df_concat2


# <div class="alert alert-success" role="alert"> 
# 
# In below example, we have used " concate " method to concatenate two DataFrames for column-based with the help pf " axis = 0 ".
#     
# </div>

# In[179]:


pd.concat([df_concat1,df_concat2],axis=0,ignore_index=False)


# In[180]:


pd.concat([df_concat1,df_concat2],axis=0,ignore_index=True)


# <div class="alert alert-success" role="alert"> 
# 
# In below example, we have used " concate " method to concatenate two DataFrames for row-based with the help pf " axis = 1 ".
#     
# </div>

# In[181]:


pd.concat([df_concat1,df_concat2],axis=1,ignore_index=False)


# In[182]:


pd.concat([df_concat1,df_concat2],axis=1,ignore_index=True)


# <div class="alert alert-success" role="alert"> 
# 
# Creating Random Variables in DataFrame with " concat " method
# </div>

# In[183]:


pd.concat([pd.DataFrame([i], columns = ['A']) for i in range(3)], ignore_index = True)


# In[184]:


pd.concat( [pd.DataFrame([i], columns = ["A"]) for i in np.random.random(3)], ignore_index = True)


# <div class="alert alert-success" role="alert"> 
# 
# Concatenating 3 created variables with random method in numpy by using " Concat " method
#     
# </div>

# In[185]:


data_concat1 = np.random.random((4,4))
data_concat1_df = pd.DataFrame(data_concat1)

data_concat2 = np.random.randint(111,222,size=(4,4))
data_concat2_df2 = pd.DataFrame(data_concat2)

data_concat3 = np.random.randint(3,4,size=(4,4))
data_concat3_df3 = pd.DataFrame(data_concat3)

concat_example_concat = pd.concat([data_concat1_df,data_concat2_df2,data_concat3_df3],axis=0,ignore_index=True)
concat_example_concat


# ### <div class="alert alert-success" role="alert"> 8.2 - Merge  </div>
# 
# 
# 
# 

# <div class="alert alert-success" role="alert"> The merge() method updates the content of two DataFrame by merging them together, using the specified method(s).
# 
# [Reference](https://www.w3schools.com/python/pandas/ref_df_merge.asp)
#     
#  
# Merge DataFrame or named Series objects with a database-style join.
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
#     
# </div>
# 
# 
# 
# 
# 
# 

# In[186]:


merge_df1 = pd.DataFrame({'Users': ['foo', 'bar', 'baz', 'foo'],

                          'Value': [1, 2, 3, 5]})

 
merge_df2 = pd.DataFrame({'Users_2': ['foo', 'bar', 'baz', 'foo'],

                          'Value': [5, 6, 7, 8]})


# <div class="alert alert-success" role="alert"> 
#     
# 1. left_on : label or list, or array-like
#  Column or index level names to join on in the left DataFrame. Can also be an array or list of arrays of the length of the left DataFrame. These arrays are treated as if they are columns.
# 
#     
# 2. right_on : label or list, or array-like
#  Column or index level names to join on in the right DataFrame. Can also be an array or list of arrays of the length of the right DataFrame. These arrays are treated as if they are columns.
# 
#     
# 3. suffixes : list-like, default is (“_x”, “_y”)
#  A length-2 sequence where each element is optionally a string indicating the suffix to add to overlapping column names in left and right respectively. Pass a value of None instead of a string to indicate that the column name from left or right should be left as-is, with no suffix. At least one of the values must not be None.
# 
#     
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)    
#     
# </div>
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[187]:


merge_df1.merge(merge_df2, left_on='Users', right_on='Users_2')


# In[188]:


merge_df1.merge(merge_df2, left_on='Users', right_on='Users_2', suffixes=('of User', 'of Users2'))


# In[189]:


merge_df2.merge(merge_df1, left_on='Users_2', right_on='Users', suffixes=('of User_2', 'of Users'))


# <div class="alert alert-success" role="alert"> 
# how : {‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘inner’
# 
# Type of merge to be performed.
# 
#  1. left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
# 
#  2. right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
# 
#  3. outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
# 
#  4. inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
# 
#  5. cross: creates the cartesian product from both frames, preserves the order of the left keys.
#     
#     
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
#     
# </div>
# 
# 
# 
# 
# 
# 

# In[190]:


merge_df3 = pd.DataFrame({'Users': ['A','B'], 'Values1':[1,2], 'Location':['Pink','Floyd']})
merge_df4 = pd.DataFrame({'Users': ['A','B'], 'Values2':[33,44], 'Location':['The','Wall']})


# In[191]:


merge_df3.merge(merge_df4, how = 'inner', on = 'Users')


# In[192]:


merge_df4.merge(merge_df3, how = 'inner', on = 'Users')


# In[193]:


merge_df3.merge(merge_df4, how = 'left', on = 'Users')


# In[194]:


merge_df4.merge(merge_df3, how = 'right', on = 'Users')


# In[195]:


merge_df3.merge(merge_df4, how = 'cross')


# ### <div class="alert alert-success" role="alert"> 8.3 - Append     </div>

# <div class="alert alert-success" role="alert"> Append function is used to append rows of other dataframe to the end of the given dataframe, returning a new dataframe object. Columns not in the original dataframes are added as new columns and the new cells are populated with NaN value.  
# 
# [Reference](https://www.geeksforgeeks.org/python-pandas-dataframe-append/)
# 
# </div>

# In[196]:


df_append1 = pd.DataFrame([[1, 2, 99], [3, 4, 88]], columns=list('ABC'), index=['x', 'y'])

df_append1


# In[197]:


df_append2 = pd.DataFrame([[5, 6, 11], [7, 8, 22]], columns=list('ABC'), index=['x', 'y'])

df_append2


# In[198]:


df_append1.append(df_append2)


# In[199]:


df_append1.append(df_append2,ignore_index= True)


# In[200]:


df_append3 = pd.DataFrame(columns = ['A'])

for i in range(5):
    df_append3 = df_append3.append({'A': i}, ignore_index = True)
    
df_append3


# In[201]:


import numpy as np

df_append4 = pd.DataFrame(columns = ['A','B','X'])

for i in range(5):
    df_append4 = df_append4.append({'A': i,
                                    'B':np.random.rand(),
                                    'X': np.random.randint(140,150)}, 
                                    ignore_index = True)
    
df_append4


# ### <div class="alert alert-success" role="alert"> 8.4 - Join </div>
# 
# 
#  

# <div class="alert alert-success" role="alert"> 
#     
# Join columns of another DataFrame.
# 
# Join columns with other DataFrame either on index or on a key column. Efficiently join multiple DataFrame objects by index at once by passing a list.
# 
# 
# [Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)
# 
# </div>
# 
# 
#  

# In[202]:


join_df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'], 'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

join_df


# In[203]:


join_df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

join_df2


# In[204]:


join_df.join(join_df2,lsuffix = '_caller', rsuffix = '_other')


# In[205]:


join_df.set_index('key').join(join_df2.set_index('key'))


# In[206]:


join_df.join(join_df2.set_index('key'), on = 'key')


# In[207]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

