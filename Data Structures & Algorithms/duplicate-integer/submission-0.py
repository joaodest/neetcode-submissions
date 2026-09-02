class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        has_appeared = False
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                has_appeared = True
                break
        return has_appeared