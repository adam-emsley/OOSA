#!/usr/bin/env python
# coding: utf-8

# In[17]:


#importing packages required:
import numpy as np

#defining functions needed:
def minimum(sequence=[], no=10, start=0, stop=1): 
    """ 
    
    ---------------------------------------------------------------------------------
    - function to find minimum of a random list of length 'no', or user given sequence
    - user sequence input must be a numpy array
    
    - default random float list length is 10 
    
    - random floats in range [start,stop] with default of [0,1] form list
    
    - returns minimum of the list (m), and the list itself (array)
    
    - example usage: m, array = minimum(no=100, start=0, stop=100)
    ---------------------------------------------------------------------------------
    """
    
    if len(sequence) == 0:
        array = np.random.uniform(start, stop, size=(no,)) #random floats
    else:
        array = sequence
        
    m = array[0] #first element of array
    
    for x in array:
        if x <= m:
            m = x 
    
    return m, array


#using minimum function to sort our list:
def sorting(sort=[]):
    """ 
    
    ---------------------------------------------------------------------------------
    - function to sort a list of numbers 'sort'
    
    - by default, sorts a list of 10 random floats from 0 to 1
    
    - user input must be an array
    
    - returns sorted array
    ---------------------------------------------------------------------------------
    """
    
    m, arr = minimum(sequence = sort)
    arr2 = arr.copy()
    empty = np.array([0]*len(arr))
    i = 0
    
    while i < len(arr2):
        
        if len(arr[arr==m]) == 1:
            empty[i] = m
        else:
            empty[i:i+len(arr[arr==m])] = m
        
        i = i+len(arr[arr==m])
        cut = arr[arr != m]
        m, arr = minimum(sequence = cut)
        

    return empty

