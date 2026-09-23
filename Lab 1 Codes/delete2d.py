import numpy as np

twoDArray = np.array([[11, 15, 10, 6], 
                      [10, 14, 11, 5],
                      [12, 17, 12, 8], 
                      [15, 18, 14, 9] ])
print(twoDArray)

newTDArray = np.delete(twoDArray, 1, axis=1)
newTDArray = np.delete(twoDArray, 2, axis=0)
print(newTDArray)

#Summary
#Time Complexity : O(MN)
#Space Complexity : O(1)






