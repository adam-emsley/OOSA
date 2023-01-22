#!/usr/bin/env python
# coding: utf-8

# In[99]:


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
    
    - returns sorted array and unsorted array
    ---------------------------------------------------------------------------------
    """

    m, arr = minimum(sequence = sort) #minimum of our sequence and the sequence itself
    arr2 = arr.copy() #copy of our sequence for knowing length
    empty = [] #empty list in whichn we can append minima
    i = 0 #dummy index used as counter
    
    while i < len(arr2): #we loop through the length of our array
    
        count = len(arr[arr==m]) #if repeated numbers in list, we must append that number of times
        while count > 0:
            empty.append(m)
            count = count -1
        
        i = i+len(arr[arr==m]) #adding to dummy i how many minima we have of given number
        cut = arr[arr != m]    #we do not care about the minima we remove, so chop our array
        m, arr = minimum(sequence = np.array(cut)) #find minima of new chopped array, and carry on while loop

    return empty, arr2

