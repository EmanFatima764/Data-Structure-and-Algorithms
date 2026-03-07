from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes Algorithm
        n=len(nums)
        maxim=float("-inf")   # in case of negative numbers
        total=0
        for i in range(0,n):
            total+=nums[i]
            maxim=max(maxim,total)
            if total<0:        # skip negative number
                total=0
        return maxim
if __name__ =="__main__":
    sol=Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))




        