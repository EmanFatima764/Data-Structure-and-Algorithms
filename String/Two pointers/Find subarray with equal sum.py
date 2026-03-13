from typing import List
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        #Create a set to store sums.
        hash_set=set()
        sum=0
        for i in range(1,len(nums)):
            sum=nums[i]+nums[i-1]
        # If the sum already exists in the set → return true.
            if sum in hash_set:
                return True
        # Otherwise add it to the se

            else:
                hash_set.add(sum)
        return False
if __name__ =="__main__":
    sol=Solution()
    nums=[4,2,4]
    print(sol.findSubarrays(nums))   

        