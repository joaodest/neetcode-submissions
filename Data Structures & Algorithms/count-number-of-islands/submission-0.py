
d = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(row, col):
            # Para se estiver fora do grid ou for água
            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == "0"
            ):
                return

            # Marca como visitada
            grid[row][col] = "0"

            for dr, dc in d.values():
                dfs(row + dr, col + dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands