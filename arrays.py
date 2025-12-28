class Solution:
            # with TLE error
    def isSorted(self, arr) -> bool:
        n=len(arr)
        if n<=1:
            return True
        if arr[n-1]<arr[n-2]:
            return False
        return self.isSorted(arr[:n-1])
      # recursion
      class Solution:
    def isSorted(self, arr) -> bool:
        return self.check(arr,0)
    def check(self,arr,i):
        if i == len(arr)-1:
            return True
        if arr[i]>arr[i+1]:
            return False
        return self.check(arr,i+1)
        # iterative approach
    
        
      
        
    
        
     

        
              
    
        
     

        
            