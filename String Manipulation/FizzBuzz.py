
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[""]*(n+1)    # string array of length n
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answer[i]="FizzBuzz"
            elif i% 3==0:
                 answer[i]="Fizz"
            elif i% 5==0:
                 answer[i]="Buzz"
            else:
                answer[i]=str(i)

        return answer[1:]   # exclude 0th index
if __name__ =="__main__":
    sol=Solution()
    n=3
    print(sol.fizzBuzz(n))


                

            

        