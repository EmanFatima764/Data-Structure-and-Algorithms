from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n      # new array
        pos=0          # even index
        neg=1          # odd index
        for num in nums:
            if num>0:        
                result[pos]=num      # add pos num
                pos+=2
            else:
                result[neg]=num       # add neg num
                neg+=2
        return result
if __name__ =="__main__":
    sol=Solution()
    nums=[3,1,-2,-5,2,-4]
    print(sol.rearrangeArray(nums))

        