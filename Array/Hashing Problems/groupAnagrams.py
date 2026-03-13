from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count freq
        # count len and char should be same
        freq={}
        for num in strs:      
            key=" ".join(sorted(num))   
            if key not in freq:
                freq[key]=[]
            freq[key].append(num)
        return list(freq.values())     

        # sorted array as hashmapkey
if __name__ =="__main__":
    sol=Solution()
    strs=["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))