#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing packages required:
import numpy as np

#defining functions needed:
def minimum(no=10, start=0, stop=1): 
    """ 
    
    ---------------------------------------------------------------------------------
    - function to find minimum of a random list of length 'no'
    
    - default list length is 10
    
    - random floats in range [start,stop] with default of [0,1] form list
    
    - returns minimum of the list (m), and the list itself (array)
    
    - example usage: m, array = minimum(no=100, start=0, stop=100)
    ---------------------------------------------------------------------------------
    """
    array = np.random.uniform(start, stop, size=(no,))
    
    m = array[0]
    
    for x in array:
        if x <= m:
            m = x
    
    return m, array

