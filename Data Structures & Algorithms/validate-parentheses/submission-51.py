class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for incoming_char in s:
            if incoming_char in "([{":
                stack.append(incoming_char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top == "(" and incoming_char != ")") \
                    or (top == "[" and incoming_char != "]") \
                    or (top == "{" and incoming_char != "}"):
                    return False

        return not stack


        