class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        islands, visited = 0, set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                qr, qc = q.popleft()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    r, c = qr + dr, qc + dc
                    if r in range(row) and  c in range(col) and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands
