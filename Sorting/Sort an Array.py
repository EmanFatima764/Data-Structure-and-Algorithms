from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            swapped=False
            for j in range(0,n-i-1):
                # compare adjacent elements
                if nums[j]>nums[j+1]:
                    # swap if element are in wrong order
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    swapped=True
                    # in case array is already sorted
            if  not swapped:
                    break
        return nums
if __name__ =="__main__":
    sol=Solution()
    nums=[5,2,3,1]
    print(sol.sortArray(nums))
            
                
             