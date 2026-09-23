import array

arr_1 = array.array('i', [1,2,3,4,5,6])      
arr_2 = array.array('d', [1.3,1.5,1.6])   

def traverseArray(array):
    for i in array:                 #O(N)
        print(i)                    #O(1)

traverseArray(arr_1)
traverseArray(arr_2)

#Summary
#Time Complexity : O(N)
#Space Complexity : O(1)

