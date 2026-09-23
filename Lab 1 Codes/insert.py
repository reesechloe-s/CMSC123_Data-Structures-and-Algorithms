#1. Using Array module
import array

my_array1 = array.array('i', [1,2,3,4])     #O(N)
print(my_array1)

#Insert at beginning - index 0 
my_array1.insert(0,6)
print(my_array1)

#Insert at middle - index 2
my_array1.insert(2,7)
print(my_array1)

#Insert at end - index 6
my_array1.insert(6,99)
print(my_array1)

#Summary
#Time Complexity : O(1)/O(N)
#Space Complexity : O(1)


