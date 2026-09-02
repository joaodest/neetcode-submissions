class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i = 0
        n = len(s) - 1 
        while i <= n:
            if s[i] != s[n]:
                return False
            i+=1
            n-=1
        return True