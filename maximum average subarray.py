from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window
        window_sum=sum(nums[:k])   # sum of first subarray
        max_sum=window_sum
        for i in range(k,len(nums)):   # loop from 4 to 6
            window_sum =window_sum+nums[i] - nums[i-k] 
            max_sum=max(max_sum,window_sum)
            
        return max_sum/k           # avg max_sum

if __name__ =="__main__":
    sol=Solution()
    nums=[1,12,-5,-6,50,3]
    k=4
    print(sol.findMaxAverage(nums,k))    