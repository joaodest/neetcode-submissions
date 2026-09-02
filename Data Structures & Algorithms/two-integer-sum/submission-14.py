import json
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = target - nums[i] -> diff = 4 
        # -> diff está no hashmap? Sim, então retorna hash[i], hash[diff]  
        
        mapa = {}
        for idx, num in enumerate(nums):
            if num not in mapa:
                mapa[num] = idx
            elif num in mapa:
                l = []
                mapa[num] = [mapa[num], idx]

        print(json.dumps(mapa, indent=2))
        for i in mapa:
            diff = target - i
            print(f"i: {i}\n diff: {diff}")
            if diff not in mapa: continue
            if i != diff:
                return [mapa[i], mapa[diff]]
            else:
                if isinstance(mapa[diff], list): return [n for n in mapa[diff]]
                continue