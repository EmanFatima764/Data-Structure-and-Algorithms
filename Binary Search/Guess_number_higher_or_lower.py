# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

PICKED_NUMBER = 6   # change this value to test
def guess(num: int) -> int:
    if num > PICKED_NUMBER:
        return -1
    elif num < PICKED_NUMBER:
        return 1
    else:
        return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        # Take two pointers
            l,r=1,n
            while l<=r:
                mid=(l+r)//2    # find mid
                res=guess(mid)   #  call guess 
                if res ==0:       # guessed successfully
                   return mid
                elif res==-1:     # guess is higher
                    r=mid-1
                else:              # guess is lower
                    l=mid+1
if __name__ =="__main__":
    n=12
    sol=Solution()
    print(sol.guessNumber(n))
    
            



        
