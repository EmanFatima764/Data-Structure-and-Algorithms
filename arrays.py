class Solution:
    # with TLE error
    def isSorted(self, arr) -> bool:
        n=len(arr)
        if n<=1:
            return True
        if arr[n-1]<arr[n-2]:
            return False
        return self.isSorted(arr[:n-1])
      
    
        
      
        
    
        
     

        
              
    
        
     

        
            
