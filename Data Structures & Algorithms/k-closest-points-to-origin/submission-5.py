class Solution:
    def distancia_euc(self, xi, yi):
        return math.sqrt(xi ** 2 + yi**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            points.sort(key=lambda x: x[0] ** 2 + x[1]**2)
            return points[:k]
                

            