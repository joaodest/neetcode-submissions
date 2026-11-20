class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # busca binaria modificada?
        # índice onde a soma da esquerda = soma da direita
        # cada lado individualmente
        
        # solução bruce force O(n²) -> Seja i cada índice do array nums:
        #   1. Para cada índice i, acumula-se os valores:
        #       lsum = nums[0..i]
        #       rsum = nums[i+1..n]
        #   2. compara-se a soma de cada particionamento
        #   3. se lsum == rsum, então retorne i
        
        N = len(nums)
        res = -1
        for i in range(N):
            rsum = 0
            lsum = 0
            for l_idx in range(0, i):
                lsum += nums[l_idx]

            for r_idx in range(i + 1, N):
                rsum += nums[r_idx]

            if lsum == rsum:
                return i

        return res




