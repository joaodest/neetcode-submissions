from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def neighbors(r, c):
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        # achar qualquer célula de terra para iniciar a BFS
        start_r, start_c = -1, -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    break
            if start_r != -1:
                break

        queue = deque([(start_r, start_c)])
        visited = set([(start_r, start_c)])
        perimeter = 0

        while queue:
            r, c = queue.popleft()

            # cada bloco começa com 4 lados
            cell_perimeter = 4

            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    cell_perimeter -= 1
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            perimeter += cell_perimeter

        return perimeter