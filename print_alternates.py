class Solution:
    def getAlternates(self, arr):
        # Code Here
        # slicing
        result = []           # to not change original array
        for i in range(0, len(arr) , 2): # step by 2
            result.append(arr[i]) 
        return result    # to add element in array
       
