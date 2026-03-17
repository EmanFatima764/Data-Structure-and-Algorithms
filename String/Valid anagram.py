from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram means same character with same frequency
        # if one string can be formed by rearranging other
        # check lengths
        if len(s)!=len(t):
            return False
        # check freq
        hash_map={}
        # count character in s
        for ch in s:
            if ch in hash_map:
                hash_map[ch]+=1
            else:
                hash_map[ch]=1
        # Reduce character by 1
        for char in t:
            if char not in hash_map:
                return False
            hash_map[char]-=1
        # if t contain character more time than s
            if hash_map[char]<0:
               return False
        return True
if __name__ =="__main__":
    sol=Solution()
    s="anagram"
    t="nagaram"
    print(sol.isAnagram(s,t))
        
        