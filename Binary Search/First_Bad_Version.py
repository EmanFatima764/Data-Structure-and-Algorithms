# The isBadVersion API is aLeftready defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version):
    return version>=4
class Solution:
    def firstBadVersion(self, n: int) -> int:

        left=1
        right=n
        
        while left<right:
            mid=left+(right-left)//2
            if isBadVersion(mid):  # first bad version is at mid or before
                right=mid
            else:
                left=mid+1      # first bad version is after mid
        return left
if __name__ =="__main__":
    sol=Solution()
    n=5
    print("First Bad Version:",sol.firstBadVersion(n))

