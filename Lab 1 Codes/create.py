#1. Using Array module
import array

my_array = array.array('i')                  #O(1)
print(my_array)
my_array1 = array.array('i', [1,2,3,4])      #O(N)
print(my_array1)

#2. Using numpy module
import numpy as np

np_array = np.array([], dtype=int)           #O(1)
print(np_array)
np_array1 = np.array([1,2,3,4])              #O(N)
print(np_array1)

#Summary
#Time Complexity : O(1)/O(N)
#Space Complexity : O(N)




