class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels=set("aeiou")
        i=len(s)-1         # start from end
        while i>=0 and s[i] in vowels:
            i-=1
        return s[:i+1]       # return string by skiping continuos vowel from last
if __name__=="__main__":
    sol=Solution()
    s="idea"
    print(sol.trimTrailingVowels(s))
        