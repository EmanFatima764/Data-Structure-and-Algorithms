from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using dictionary
        n=len(nums)    
        freq={}
        for i in range(0,n+1):  # keys from 0 to n in dictionary
            freq[i]=0           
        for num in nums:        # assign 1 to keys that exist in nums 
            freq[num]=1
        for k,v in freq.items():    # iterate through dictionary
            if v==0:                  
                return k              # return key which is not present in nums
if __name__ == "__main__":
    sol=Solution()
    nums=[3,0,1]
    print(sol.missingNumber(nums))

        
         
        
        