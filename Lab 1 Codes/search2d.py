import numpy as np

twoDArray = np.array([[11, 15, 10, 6], 
                      [10, 14, 11, 5], 
                      [12, 17, 12, 8], 
                      [15, 18, 14, 9] ])
print(twoDArray)

def searchTDArray(array, value):
    for i in range(len(array)):                                             #O(M)
        for j in range(len(array[0])):                                      #O(N)
            if array[i][j] == value:                                        #O(1)
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element not found'

print(searchTDArray(twoDArray, 14))

#Summary
#Time Complexity : O(MN)
#Space Complexity : O(1)