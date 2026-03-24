from typing import list
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        if len(p)>len(s):
            return res
        pcount=Counter(p)
        window=Counter()
        left=0
        for right in range(len(s)):
            window[s[right]]+=1
            if right-left+1>len(p):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            if window == pcount:
                res.append(left)

        return res
if __name__ =="__main__":
    sol=Solution()
    s="cbaebabacd"
    p="abc"
    print(sol.findAnagrams(s,p))
