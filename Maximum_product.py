from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=0     # maximum product
        n=len(nums)
        for i in range(n):   # loop
            for j in range(i+1,n):
                product=((nums[i]-1)*(nums[j]-1))   
                max_product=max(max_product,product)  # update max_product
        return max_product
if __name__ =="__main__":
    sol=Solution()
    nums=[3,4,5,2]
    print(sol.maxProduct(nums))



        