class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # busca binaria modificada?
        # índice onde a soma da esquerda = soma da direita
        # cada lado individualmente
        
        # solução bruce force O(n²) -> 
        #   1. acumula a soma dos valores de nums[0..n]
        #   2. para cada índice, computa-se:
        #       lsum = nums[0..i]
        #       rsum = nums[i+1..n]
        #   3. busca-se 
        
        N = len(nums)
        res = -1
        for i in range(N):
            rsum = 0
            lsum = 0
            for l_idx in range(i):
                lsum += nums[l_idx]

            for r_idx in range(i + 1, N):
                rsum += nums[r_idx]

            if lsum == rsum:
                return i

        return res




