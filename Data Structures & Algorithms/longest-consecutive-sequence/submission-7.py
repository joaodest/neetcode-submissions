class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in seen: # se existe um anterior, o num atual pertence
                                    # a uma sequencia mas não é o primeiro termo
                length = 1
                while num + length in seen:
                    length += 1
                longest = max(length, longest)

        return longest

                


                

            
