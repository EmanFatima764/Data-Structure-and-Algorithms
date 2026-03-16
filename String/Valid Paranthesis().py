from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}
        for char in s:
            if char in mapping.values():
                # ['{','(','[']
                stack.append(char)
            else:
                if not stack or stack[-1] !=mapping[char]:
                    return False
                stack.pop()
        return not stack

if __name__ =="__main__":
    sol=Solution()
    s="()[]{}"
    print(sol.isValid(s))
