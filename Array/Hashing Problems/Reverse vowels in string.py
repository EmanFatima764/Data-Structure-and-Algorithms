class Solution:
    def reverseVowels(self, s: str) -> str:
        # convert string into list 
        string=list(s)
        # create  a set of vowels
        vowels=set("aeiouAEIOU")
        # Declare two pointers
        l=0
        r=len(s)-1 

        while l<r:
            # check value is vowel or not 
            while l<r and string[l] not in vowels:
                l+=1
            while l<r and string[r] not in vowels:
                r-=1
            # if vowel then swap
            string[l],string[r]=string[r],string[l]

            l+=1
            r-=1
        
        return "".join(string)
if __name__ == "__main__":
    sol=Solution()
    s="IceCreAm"
    print(sol.reverseVowels(s))

  
        