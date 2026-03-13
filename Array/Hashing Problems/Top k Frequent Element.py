from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        # count frequency 
        n=len(nums)
        for i in range(n):
            if nums[i]  in frequency:
                frequency[nums[i]] +=1
            else:
                frequency[nums[i]]=1
        # sort elemnets by frequency
        sorted_nums=sorted(frequency,key=frequency.get, reverse=True)
        # sorted(frequency) sorts ditionary by number   [1,2,3]
         # but we wnt to sort based on frequency        [3,2,1]
         # it sorts in ascending order so reverse = TRue
         #[1,2,3]
        return sorted_nums[:k]


               
if __name__ =="__main__":    
    sol=Solution()
    nums=[1,1,1,2,2,3]
    k=2
    print(sol.topKFrequent(nums,k))
