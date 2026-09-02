from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        w1 = deque(word1)
        w2 = deque(word2)
        
        while w1 or w2:
            if w1:
                result.append(w1.popleft())
            if w2: 
                result.append(w2.popleft())
        return "".join(result)

                




