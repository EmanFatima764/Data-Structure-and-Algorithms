class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums_lo=[]
        for i in range(len(nums)):
            if i<1:
                nums.append(nums_lo)
            else:
                nums[i]=nums[i]+nums[i-1]
            nums_lo.append(nums[i])
        return nums_lo


        