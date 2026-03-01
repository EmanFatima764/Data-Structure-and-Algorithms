class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort array

        nums.sort()
        # create a list
        res=[]
        # start from a fix number
        for i in range(0,len(nums)-2):
            # skip duplicate fixed number
            if i>0 and nums[i]==nums[i-1]:
                continue
            # declare two pointers
            left=i+1
            right=len(nums)-1
            # condition 
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                # if value is too small move left
                if total <0:
                    left+=1
                # if value is too big move big to right
                elif total >0:
                    right-=1
                # if sum is 0 then add into list 
                else :
                    res.append([nums[i],nums[left],nums[right]])
                    # skip duplicates
                    while left <right and nums[left]==nums[left+1]:
                       left +=1
                    while left <right and nums[right]==nums[right-1]:
                       right -=1
                    left+=1
                    right-=1
        return res
if __name__ == "__main__":
        sol=Solution()
        nums=[0,1,1]
        print(sol.threeSum(nums))


                 
                





        