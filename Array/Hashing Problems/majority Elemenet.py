from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        # count frequency
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
            # check freq of eacch number if it is greater than half of array
            if freq[nums[i]] > n//2:
                return nums[i]
        
if __name__ =="__main__":    
    sol=Solution()
    nums=[2,2,1,1,1,2,2]
    print(sol.majorityElement(nums))