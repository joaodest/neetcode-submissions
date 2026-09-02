class Solution:

    def isValid(self, s: str) -> bool:
        def is_open_char(c: str) -> bool:
            return c in ("[", "(", "{")
        def is_close_char(c: str) -> bool:
            return c in ("]", ")", "}")
        def pair(c1, c2):
            if c1 == '{'and c2 == '}': 
                return True
            elif c1 == '[' and c2 == ']':
                return True
            elif c1 == '('and c2 == ')':
                return True
            return False

        stack = []
        for incoming_char in s:
            if is_open_char(incoming_char):
                stack.append(incoming_char)
            if is_close_char(incoming_char):
                if not stack: 
                    return False
                stack_item = stack.pop()
                if not pair(stack_item, incoming_char):
                    return False
           
        return not stack


        