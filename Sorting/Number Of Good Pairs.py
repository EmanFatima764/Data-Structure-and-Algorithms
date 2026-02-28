from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
         # count frequency of each number
        freq=Counter(nums)      # {1:3,2:1,3:2}
        count=0
        for k in freq:
            # pairs of each number
            count+=freq[k]*(freq[k]-1)//2   # 1: (0,3) , (0,4),(3,4),(2,5)
        return count
if __name__ =="__main__":
    sol=Solution()
    nums=[1,2,3,1,1,3]
    print(sol.numIdenticalPairs(nums))


        
