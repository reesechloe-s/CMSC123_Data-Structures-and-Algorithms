import array

arr_1 = array.array('i', [1,2,3,4,5,6])      
arr_2 = array.array('d', [1.3,1.5,1.6])   

def accessElement(array, index):
    if index >= len(array):
        print("There is not any element in this index")    
    else:
        print(array[index])

accessElement(arr_1, 1)
accessElement(arr_2, 9)

#Summary
#Time Complexity : O(1)
#Space Complexity : O(1)
