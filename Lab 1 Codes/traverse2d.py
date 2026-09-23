import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

def traverseTDArray(array):
    for i in range(len(array)):             #O(M)
        for j in range(len(array[0])):      #O(N)
            print(array[i][j])              #O(1)
traverseTDArray(twoDArray)

#Summary
#Time Complexity : O(MN)
#Space Complexity : O(1)

