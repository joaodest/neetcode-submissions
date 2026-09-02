class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            a = ord(s[i])
            b = ord(s[j])

            a ^= b
            b ^= a
            a ^= b

            s[i] = chr(a)
            s[j] = chr(b)

            i += 1
            j -= 1