from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_new=[]
        for i in range(len(nums)):
            if i<1:
                nums.append(nums_new)
            else:
                nums[i]=nums[i]+nums[i-1]
            nums_new.append(nums[i])
        return nums_new
if __name__ =="__main__":
   sol=Solution()
   nums=[1,2,3,4,5]
   print(sol.runningSum(nums))


        