import numpy as np

twoDArray = np.array([[11, 15, 10, 6], 
                      [10, 14, 11, 5], 
                      [12, 17, 12, 8], 
                      [15, 18, 14, 9] ])
print(twoDArray)

#New Row
newTwoDArray = np.insert(twoDArray, 2, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))

# #New Column
# newTwoDArray = np.insert(twoDArray, 1, [[11,22,33,44]], axis=1)
# print(newTwoDArray)
# print(len(newTwoDArray[0]))

#Append

# newerTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
# print(newerTwoDArray)

# new_col = np.array([[1], [2], [3], [4]])
# newerTwoDArray = np.append(twoDArray, new_col, axis=1)

#Summary
#Time Complexity : O(MN)
#Space Complexity : O(MN)