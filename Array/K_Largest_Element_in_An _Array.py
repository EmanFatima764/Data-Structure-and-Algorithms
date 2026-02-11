from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for _ in range(k):   
            largest=float("-inf")    
            for num in nums:
                if num>largest:
                 largest=num
            nums.remove(largest)
        return largest
if __name__ =="__main__":
    sol=Solution()
    nums=[3,2,1,5,6,4]
    k=2
    print(sol.findKthLargest(nums,k))
