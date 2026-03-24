from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # sliding window
        seen=set()  # add seen elements
        repeated=set()  # repeated sequence
        w_size=10
        for i in range(0,len(s)-w_size+1):
            seq=s[i:i+w_size]
            if seq not in seen:
                seen.add(seq)
            else:
                repeated.add(seq)
        return list(repeated)
if __name__ =="__main__":
    sol=Solution()
    s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(sol.findRepeatedDnaSequences(s))