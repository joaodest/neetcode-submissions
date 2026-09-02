class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        curr = 0
        max_v = arr[0]

        for n in arr:
            curr = max(curr, 0)
            curr += n
            max_v = max(max_v, curr)
        return max_v