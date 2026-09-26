class Solution:
    """
        diff = 2 - nums[L]
        mem[idx do array?]
    """  
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0

        mem = defaultdict(int)
        mem[0] = 1
        
        for num in nums:
            total += num
            target = total - k
            if target in mem.keys():
                res+=mem[target]
            mem[total] += 1
            
        return res




