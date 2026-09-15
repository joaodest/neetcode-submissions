class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tam = len(nums)
        L, curr_sum = 0, 0
        ans = float('inf')
        for R in range(tam):
            curr_sum += nums[R]
            while curr_sum >= target:
                ans = min(ans, R-L+1)
                curr_sum -= nums[L] 
                L += 1
        if ans == float('inf'): ans = 0
        return ans
            