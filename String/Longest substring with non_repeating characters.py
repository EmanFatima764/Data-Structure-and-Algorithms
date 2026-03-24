from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        l,r=0,0
        n=len(s)
        maxi=0
        # stores last index of chracters
        my_dict={}
        while r<n:
            if s[r] in my_dict:
                l=max(l,my_dict[s[r]]+1)
             # Update last index 
            my_dict[s[r]] = r
            # update max length 
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi
if __name__ =="__main__":
    sol=Solution()
    s="abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
        

        