class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        seen_s = {}
        seen = {}
        for c in s:
            if c not in seen_s.keys():
                seen_s[c] = 0
            else:
                seen_s[c] = seen_s[c] + 1

        
        for c in t:
            if c not in seen.keys():
                seen[c] = 0
            else:
                seen[c] = seen[c] + 1
        print(seen)
        print(seen_s)
        for i in seen:
            if i not in seen_s.keys(): return False
            if seen[i] != seen_s[i]: return False 
            
        
        return True
 