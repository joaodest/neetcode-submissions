class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 1, 2, 3, 3, 5, 6
        mmin = float('inf')
        N = len(nums)
        lo, hi = 0, k - 1
        while hi < N:
            mmin = min(nums[hi] - nums[lo], mmin)
            hi+=1
            lo += 1

        return mmin