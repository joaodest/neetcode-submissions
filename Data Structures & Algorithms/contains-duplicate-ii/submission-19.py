class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            limit = i + k + 1
            for j in range(i + 1, min(n, limit)): 
                if nums[i] == nums[j]:
                    return True
        return False