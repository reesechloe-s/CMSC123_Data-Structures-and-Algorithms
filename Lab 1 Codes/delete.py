import array

arr_1 = array.array('i', [1,2,3,4,5,6])      

arr_1.remove(1)         #O(N)
print(arr_1)

arr_1.remove(3)         #O(N)
print(arr_1)

arr_1.remove(6)         #O(1)
print(arr_1)

#Summary
#Time Complexity : O(1)/O(N)
#Space Complexity : O(1)

