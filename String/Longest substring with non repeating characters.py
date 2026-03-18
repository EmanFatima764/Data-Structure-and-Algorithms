from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to detect repeated charcters use set(not dict (because no index needed))
        n=len(s)
        # to count length
        maxi=0
        # to check substring length
        for i in range(0,n):
            # dict reset afer every longest substring in j loop
            my_set=set()
            for j in range(i,n):
                if s[j] not in my_set:
                    maxi=max(maxi,j-i+1)
                    my_set.add(s[j])
                else:
                    break
        return maxi



if __name__ =="__main__":
    sol=Solution()
    s="abcabcbb"
    print(sol.lengthOfLongestSubstring(s))