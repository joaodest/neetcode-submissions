class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            # O limite superior garante que não ultrapassamos k nem o fim da lista
            limit = min(i + k + 1, n)
            for j in range(i + 1, limit):
                if nums[i] == nums[j]:
                    return True
        return False