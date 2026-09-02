
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        majority = len(nums) // 2
        count = 0
        for num in nums:
            v = hm.get(num, 0) + 1
            hm[num] = v

            if v > majority:
                count = num
        return count