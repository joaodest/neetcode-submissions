class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # output = 
        output = []
        l = len(nums) - 1
        for i in range(len(nums)):
            aux = 1
            for j in range(len(nums)):
                if i == j: continue
                else:
                    aux *= nums[j]
            output.append(aux)
        return output
