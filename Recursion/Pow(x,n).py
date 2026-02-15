from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:          
            return 1
         # if n is negative make n positive then divide x^n by 1
        if n<0:       
            return 1 / self.myPow(x,-n)

         # to    improve effeciency divide power into half



        half = self.myPow(x , n//2)  
        # if n is even
        if n%2==0:
            return half*half
        # if n is odd
        else:
            return x*half*half
if __name__ =="__main__":
    sol=Solution()
    x=2
    n=-2
    print(sol.myPow(x,n))

        
        