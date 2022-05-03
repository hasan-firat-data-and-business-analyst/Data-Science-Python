#!/usr/bin/env python
# coding: utf-8

# # Import Numpy Library and Creating the arrays

# In[44]:


import numpy as np


# In[45]:


array = np.array([1, 2, 3, 4, 5])

print(array)

print(type(array))


# In[46]:


# The second way to create the arrays

test = [11,22,33,44,55]
test


# In[47]:


print(type(test))


# In[48]:


test2 = np.array(test)
test2


# In[49]:


type(test2)


# # The array's dimension

# In[50]:


# 0-D Arrays or Scalar

zero_d = np.array(101)

print(zero_d) 
print(type(zero_d))


# In[51]:


# 1-D Arrays or Uni-dimensional

uni_dimensional_or_one_D_array = np.array([11, 23, 36, 14, 58])

print(uni_dimensional_or_one_D_array) 
print(type(uni_dimensional_or_one_D_array))


# In[52]:


# 2 – D Arrays

two_D = np.array([[1,2,3,4],[9,8,7,6]])
print(two_D)
print(type(two_D))


# In[53]:


# 3 – D Arrays

three_D = np.array([[[1,2,3,4],[11,22,33,44]], 
                    [[22,22,22,22],[44,44,44,44]],
                    
                   ])
print(three_D)
print(type(three_D))


# In[54]:


three_D = np.array([[[1,2,3,4],[11,22,33,44]], 
                    [[22,22,22,22],[44,44,44,44]],
                    [["m","e","t","a"],["d","a","t","a"]]
                   ])
print(three_D)
print(type(three_D))


# In[55]:


# How to find the number of dimensions ? 

print(zero_d.ndim)


# In[56]:


print(uni_dimensional_or_one_D_array.ndim)


# In[57]:


print(two_D.ndim)


# In[58]:


print(three_D.ndim)


# In[59]:


# Shape Function in NumPy

print(zero_d)
print("--"*10)
print(zero_d.shape)


# In[60]:


print(uni_dimensional_or_one_D_array)
print("--"*10)
print(uni_dimensional_or_one_D_array.shape)


# In[61]:


print(two_D)
print("--"*10)
print(two_D.shape)


# In[62]:


print(three_D)
print("--"*10)
print(three_D.shape)


# In[63]:


# More information in shape function

shape_1 = np.array([1, 2, 3, 4])

print(shape_1)
print(shape_1.ndim)
print('shape of array :', shape_1.shape)


# In[64]:


shape_2 = np.array([1, 2, 3, 4],ndmin=5)

print(shape_2)
print(shape_2.ndim)
print('shape of array :', shape_2.shape)


# In[65]:


shape_3 = np.array([[1, 2, 3, 4],[11,22,33,44]],ndmin=5)

print(shape_3)
print(shape_3.ndim)
print('shape of array :', shape_3.shape)


# In[66]:


# Reshape
# 1-D to 2-D

reshape_1 = np.array([1,2,3,4,5,6,7,8,9,10])
new_one = reshape_1.reshape(5,2)
new_two = reshape_1.reshape(2,5)


# In[67]:


print(new_one)


# In[68]:


print(new_two)


# In[69]:


# 1-D to 3-D

reshape_2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_1 = reshape_2.reshape(2,3,2)


# In[70]:


print(new_1)


# In[71]:


# Size function in NumPy

zero_d.size


# In[72]:


uni_dimensional_or_one_D_array.size


# In[73]:


two_D.size


# In[74]:


three_D.size


# In[75]:


# N – Dimensional Arrays

n_dim_examples = np.array([11,22,33,44],ndmin=5)
print(n_dim_examples)
print('number of dimensions :', n_dim_examples.ndim)


# # Indexing Arrays

# In[76]:


# Access Array Elements

indexing = np.array([1,2,3,"Paris","Berlin","1984","Kung Fu","Rapper","The","Wall"])


# In[77]:


indexing[1]


# In[78]:


print(indexing[1])


# In[79]:


indexing[4]


# In[80]:


indexing[8:11]


# In[81]:


# Mathematical Operations

mat_op = np.array([0,1,2,3,4,5,6,7,8,9])
print(mat_op)


# In[82]:


print(mat_op[3] + mat_op[7])


# In[83]:


print(mat_op[9] / mat_op[9])


# In[84]:


print(mat_op[2] ** mat_op[7])


# In[85]:


print(indexing)


# In[86]:


print(indexing[0] / indexing[2])


# In[87]:


print(indexing[1] + indexing[1])


# In[88]:


print(indexing[2] + indexing[8] + indexing[9])


# In[89]:


indexing.dtype


# In[90]:


mat_op.dtype


# In[91]:


# 2-D Arrays

bullet = np.array([[0,1,2,3],[9,8,7,6]])


# In[92]:


bullet


# In[93]:


bullet[1,1]


# In[94]:


bullet[0,2]


# In[95]:


print(bullet[0,3])
print(bullet[1,0])


# In[96]:


bullet[0,3] + bullet[1,0]


# In[97]:


# 3-D Arrays

wrld = np.array([[[0,0,0],[1,1,1]],[[2,2,2],[3,3,3]]])
wrld


# In[98]:


wrld[1,1,1]


# In[99]:


wrld[1,1]


# In[100]:


wrld[1]


# In[101]:


wrld[1,1,1] ** wrld[1]


# In[102]:


wrld[1] ** wrld[1,1,1]


# In[103]:


wrld[1,1,1] ** wrld[1,1]


# In[104]:


wrld[1,1] + wrld[0,1,1] + wrld[0,1,1]


# In[105]:


germany = np.array([[[0,0,0],[1,1,1]],[[2,2,2],[3,3,3]]])
print(germany)
print(germany.ndim)


# In[106]:


swiss =  np.array([[0,0,0],[1,1,1]])
print(swiss)
print(swiss.ndim)


# In[107]:


canada = np.array([101,182,103])
print(canada)
print(canada.ndim)


# In[108]:


germany + swiss + canada


# In[109]:


germany ** swiss ** canada


# In[110]:


# Negative Indexing

ft = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print('The last element from 2nd', ft[1,-1])
print('The second element from 2nd', ft[1,1])


# In[111]:


print(ft[1,-1])
print(ft[1,-2])
print(ft[1,-3])
print(ft[1,-4])
print(ft[1,-5])
print('-*'*5)
print(ft[1,0])
print(ft[1,1])
print(ft[1,2])
print(ft[1,3])
print(ft[1,4])


# # Slicing Arrays

# In[112]:


slc = np.array([0,1,2,3,4,5,6,7,8,9])
slc


# In[113]:


slc[:4]


# In[114]:


slc[4:]


# In[115]:


# Negative Slicing

negative_slc = np.array([0,11,22,33,44,55,66,77,88,99])
negative_slc


# In[116]:


negative_slc[-1]


# In[117]:


negative_slc[-6:-1]


# In[118]:


# STEP

slc


# In[119]:


slc[1:5:2]


# In[120]:


slc[1:8:3]


# In[121]:


slc


# In[122]:


slc[::1]


# In[123]:


slc[::2]


# In[124]:


slc[::3]


# In[125]:


slc[::4]


# In[126]:


slc[::5]


# In[127]:


slc[::6]


# In[128]:


slc[::7]


# In[129]:


slc[::8]


# In[130]:


slc[::9]


# In[131]:


#Slicing multi-dimension

germany


# In[132]:


germany[0,1,0:1]


# In[133]:


germany[0,1,1:3]


# In[134]:


germany[0,1:3]


# In[135]:


df_negative_slicing = np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(df_negative_slicing)


# In[136]:


df_negative_slicing[0,3:4]


# In[137]:


df_negative_slicing[0:2,3]


# In[138]:


df_negative_slicing[0,2:-2]


# In[139]:


df_negative_slicing[-2,0:2]


# In[140]:


new1 = np.array([[0,11,22,33,44],[55,66,77,88,99]])
new1


# In[141]:


new1[0:2,0:2]


# In[142]:


new1[0:2,3:4]


# In[143]:


# Checking the Data Type of an Array

data_type = np.array([0,1,2,3,4,5,6,7,8,9])

print(data_type)
print("**"*8)
print(data_type.dtype)


# In[144]:


data_2_type = np.array(["Chor","Mozart","Zurich"])

print(data_2_type)
print("**"*8)
print(data_2_type.dtype)


# In[145]:


# Creating Arrays With a Defined Data Type

defined_arrays = np.array([1,2,3,4,5],dtype = 'S')

print(defined_arrays)
print(defined_arrays.dtype)


# In[146]:


defined_arrays1 = np.array([1,2,3,4,5],dtype = 'i4')

print(defined_arrays1)
print(defined_arrays1.dtype)


# In[147]:


defined_arrays2 = np.array([1,2,3,4,5],dtype = 'i2')

print(defined_arrays2)
print(defined_arrays2.dtype)


# In[148]:


defined_arrays3 = np.array([1,2,3,4,5],dtype = 'i8')

print(defined_arrays3)
print(defined_arrays.dtype)


# In[149]:


defined_arrays4 = np.array([1,2,3,4,5],dtype = 'i')

print(defined_arrays4)
print(defined_arrays4.dtype)


# In[150]:


defined_arrays6 = np.array([1.1, 2.10, 3.12, 4.4, 5])

print(defined_arrays6)
print(defined_arrays6.dtype)
print("*-*"*8)
new_def_type = defined_arrays6.astype('i')
print(new_def_type)
print(new_def_type.dtype)


# # Copy 

# In[151]:


test_1 = np.array([1,2,3,4,5,6])
copy_test = test_1.copy()
test_1[1] = 22

print(test_1)
print(copy_test)


# # View

# In[152]:


test_2 = np.array([1,2,3,4])
view_test = test_2.view()
test_2[3] = 777

print(test_2)
print(view_test)


# In[153]:


# Status of data in arrays

testing = np.array([1,2,3,4])

x = testing.copy()
y = testing.view()

print(x.base)
print("**"*8)
print(y.base)


# # Joining

# In[154]:


join_1 = np.array([1,2,3,4])
join_2 = np.array(["a","b","c","d"])


# In[155]:


join_new = np.concatenate((join_1,join_2))
join_new


# In[156]:


join1 = np.array([[1,2,3],[4,5,6]])
join2 = np.array([[11,22,33],[44,55,66]])


# In[157]:


join1_new = np.concatenate((join1,join2))
join1_new


# In[158]:


# Joining with “ Stack “ function

m1 = np.array([1,2,3])
m2 = np.array([4,5,6])

mm = np.stack((m1,m2), axis = 0)
print(mm)


# In[159]:


n1 = np.array([1,2,3])
n2 = np.array([4,5,6])

nn = np.stack((n1,n2), axis = 1)
print(nn)


# In[160]:


arr1 = np.array([[1,2,3],[11,22,33]])
arr2 = np.array([[4,5,6],[77,88,99]])

arr = np.stack((arr1, arr2 ), axis = 1)

print(arr)


# In[161]:


arr11 = np.array([[1,2,3],[11,22,33]])
arr22 = np.array([[4,5,6],[77,88,99]])

arr_2 = np.stack((arr11, arr22 ), axis = 1)

print(arr_2)


# # Splitting

# In[162]:


splltng = np.array([0,1,2,3,4,5,6,7,8,9])
print(splltng)


# In[163]:


splltng_1 = np.array_split(splltng, 5)
print(splltng_1)


# In[164]:


splltng_2 = np.array_split(splltng, 2)
print(splltng_2)


# In[165]:


splltng_3 = np.array_split(splltng, 4)
print(splltng_3)


# In[166]:


splltng_4 = np.array_split(splltng, 11)
print(splltng_4)


# # Searching

# In[167]:


where_test = np.array([1,2,3,7,5,7,7,8,910,7,17,7])

test_result = np.where(where_test == 7)

print(test_result)


# In[168]:


where_test_2 = np.array([1, 2, 3, "Berlin", "Paris", "Berling"])
test_result_2 = np.where(where_test_2 == "Berlin")

print(test_result_2)


# In[169]:


where_test_3 = np.array([1,2,3,4,11,22,33,44])
test_result_3 = np.where(where_test_3 %2 == 0)

print(test_result_3)


# In[170]:


where_test_4 = np.array([1,2,3,4,11,22,33,44])
test_result_4 = np.where(where_test_4 %3 == 1)

print(test_result_4)


# In[171]:


# Search Sorted and Search from right side

search_sorted_test1 = np.array([0,1,2,3,4,5,6,7,8,7])
search_sorted_test_result = np.searchsorted(search_sorted_test1, 7)
print(search_sorted_test_result)


# In[172]:


search_sorted_test2 = np.array([0,1,2,3,4,5,6,7,8,7])
search_sorted_test_result2 = np.searchsorted(search_sorted_test1, 7, side= 'right')
print(search_sorted_test_result2)


# # Find

# In[173]:


example = np.array(["Hello World from the Earth"])

find_example = np.char.find(example,"World", start = 0, end = None)
find_example


# In[174]:


find_example1 = np.char.find(example,"from", start = 0, end = None)
find_example1


# In[175]:


find_example2 = np.char.find(example,"the", start = 0, end = None)
find_example2


# # Sort

# In[176]:


sorting_example = np.array([54,1,78,3,2,11,129,13,4,5,67,9,98,6,87])
print(np.sort(sorting_example))


# In[177]:


sorting_example_words = np.array(["Zurich","Berlin", "Paris","Toronto","Los Angeles","London"])
print(np.sort(sorting_example_words))


# In[178]:


sorting_example_words_2 = np.array([True, False, False, True, True, False])
print(np.sort(sorting_example_words_2))


# In[179]:


sorting_example_3_D = np.array([[3,2,1],[33,22,11],[66,55,44]])
print(sorting_example_3_D)
print('*-* \n' * 2)
print(np.sort(sorting_example_3_D))


# # Filtering

# In[180]:


filtering_example = np.array([11,22,33,66,77,88])
filtering_check_valve = [True, False, True, False, True, False]

get_a_result = filtering_example[filtering_check_valve]

print(get_a_result)


# In[181]:


filtering_example2 = np.array([11,22,33,66,77,"Toronto"])
filtering_check_valve2 = [True, False, True, False, True, True]

get_a_result2 = filtering_example2[filtering_check_valve2]

print(get_a_result2)


# In[182]:


# Creating filter with a condition

filtering_example3 = np.array([0,1,2,3,4,5,6,7,8,9])
filtering_check_valve3 = filtering_example3 > 6

get_a_result3 = filtering_example3[filtering_check_valve3]

print(filtering_check_valve3)
print(get_a_result3)


# In[183]:


filtering_example4 = np.array([0,1,2,3,4,5,6,7,8,9])
filtering_check_valve4 = filtering_example4 %2 == 0

get_a_result4 = filtering_example4[filtering_check_valve4]

print(filtering_check_valve4)
print(get_a_result4)


# In[184]:


filtering_example5 = np.array([0,1,2,3,4,5,6,7,8,9])
filtering_check_valve5 = filtering_example5 %3 == 1

get_a_result5 = filtering_example5[filtering_check_valve5]

print(filtering_check_valve5)
print(get_a_result5)


# In[185]:


filtering_example6 = np.array([0,1,2,3,4,5,6,7,8,9])

filtering_check_valve61 = filtering_example6 %2 == 0
filtering_check_valve62 = filtering_example6 %3 == 0
filtering_check_valve6 = filtering_check_valve61 + filtering_check_valve62

get_a_result6 = filtering_example6[filtering_check_valve6]

print(filtering_check_valve6)
print(get_a_result6)


# # Zeros

# In[186]:


np.zeros(5)


# In[187]:


np.zeros(5, dtype=int)


# In[188]:


np.zeros((2,4),dtype = float)


# In[189]:


np.zeros((2,4),dtype = int)


# In[190]:


x = (2,5)
np.zeros(x)


# # Ones

# In[191]:


np.ones(6)


# In[192]:


np.ones(5,dtype=int)


# In[193]:


np.ones((2,4),dtype = float)


# In[194]:


np.ones((2,4), dtype = int)


# In[195]:


y =(4,6)
np.ones(y,dtype=float)


# # Arange

# In[196]:


arange_example = np.arange(1,10,4,dtype= int)
print(arange_example)


# In[197]:


arange_example2 = np.arange(1,10,4,dtype = float)
print(arange_example2)


# In[198]:


arange_example3 = np.arange(10)
print(arange_example3)


# In[199]:


arange_example4 = np.arange(6, dtype = float)
print(arange_example4)


# In[200]:


arange_example5 = np.arange(1,10,0.5, dtype = float)
print(arange_example5)


# # Linspace

# In[201]:


linspace_example = np.linspace(2.0, 3.0, num=5)
print(linspace_example)


# In[202]:


linspace_example_2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
print(linspace_example_2)


# In[203]:


linspace_example_3 = np.linspace(2.0, 3.0, num=5, retstep=True)
print(linspace_example_3)


# # Arange vs. Linspace

# In[204]:


arange_vs_example = np.arange(1,10,2)
print(arange_vs_example)


# In[205]:


linspace_vs_example = np.linspace(1,10,2)
print(linspace_vs_example)


# # Random

# In[206]:


# Random Sample

faa = np.random.rand(3,3)
faa


# In[207]:


import random
random_example = random.random()

print(random_example)


# In[208]:


# Generate Random Floats

random_example_2 = random.randint(1,10)
print(random_example_2)


# In[209]:


# Generate Random Integers

random_example_3 = random.randint(1,250)
print(random_example_3)


# In[210]:


# Generate Random Numbers within Range

random_example_4 = random.randrange(1,600)
print(random_example_4)


# In[211]:


# Select Random Elements

random_example_5 = random.choice("Data Analytic for Business Decision Making")
print(random_example_5)


# In[212]:


random_example_6 = random.choice([11,22,33,44,55,66,77,88,99])
print(random_example_6)


# In[213]:


random_example_7 = random.choice([11,22,33,44,55,66,77,88,99,"Berlin","Paris","Zurich"])
print(random_example_7)


# In[214]:


# Shuffle Elements Randomly

number = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
random_example_6 = random.shuffle(number)

print(number)


# # Full

# In[215]:


full_example_1 = np.full([3, 3], 77, dtype = int)
print(full_example_1)


# In[216]:


full_example_2 = np.full([3, 2], 11, dtype = float)
print(full_example_2)


# In[217]:


full_example_3 = np.full([3, 3], 11.19)
print(full_example_3)


# In[218]:


full_example_4 = np.full((3, 2), [1, 2])
print(full_example_4)


# In[219]:


full_example_5 = np.full((1, 2), [1, 2])
print(full_example_5)


# In[220]:


full_example_6 = np.full((4,2), [1, 2])
print(full_example_6)


# # Empty

# In[221]:


empty_example = np.empty([2,2])
print(empty_example)


# In[222]:


empty_example_2 = np.empty([2, 2], dtype=int)
print(empty_example_2)


# In[223]:


empty_example_3 = np.empty([2, 2], dtype=float)
print(empty_example_3)

