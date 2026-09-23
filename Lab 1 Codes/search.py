import array

arr_1 = array.array('i', [1,2,3,4,5,6])      
arr_2 = array.array('d', [1.3,1.5,1.6])

def linear_search(array, value):
    for i in array:
        if i == value:
            return True
    return "The element does not exist in this array"

print(linear_search(arr_1, 8))
print(linear_search(arr_1, 3))
print(linear_search(arr_2, 1.300))
print(linear_search(arr_2, 3))

#Summary
#Time Complexity : O(N)
#Space Complexity : O(1)