from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count frequency of each char
        hash_map={}
        for i in range(len(s)):
            hash_map[s[i]]= hash_map.get(s[i],0)+1
        
        # find first non repeating char
        for j in range(len(s)):
            if hash_map[s[j]]==1:
                return j 
            return -1
            
if __name__ =="__main__":
    sol=Solution()
    s="leetcode"
    print(sol.firstUniqChar(s))




        