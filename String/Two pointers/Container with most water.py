from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_water=0


        while l<r:
          width=r-l 
          current_water=(min(height[l],height[r])* width)
          max_water=max(max_water , current_water)     # sorted array as hashmapkey
          if height[l]<height[r]:
             l+=1
          else:
             r-=1
        return max_water



if __name__ =="__main__":
    sol=Solution()
    height=[1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))