class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracking, curr = 0, 0
        while tracking < len(nums):
            if nums[tracking] != 0:
                nums[curr] = nums[tracking]
                tracking += 1
                curr += 1 
            else:
                tracking+=1
        
        while curr < tracking:
            nums[curr] = 0
            curr+=1
        
