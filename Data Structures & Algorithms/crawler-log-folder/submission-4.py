from enum import StrEnum
import re
class Ops(StrEnum):
    UP = "../"
    STAY = "./"
    
    

class Solution:
    
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            if log == Ops.STAY:
                continue
            elif log == Ops.UP:
                if stack:
                    stack.pop()
            else:
                stack.append(log)
            
        print(stack)
        return len(stack)