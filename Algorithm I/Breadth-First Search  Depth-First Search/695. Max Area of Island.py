class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        a,b,area=len(grid),len(grid[0]),0
        def find_area(x,y):
            if 0<=x<a and 0<=y<b and grid[x][y]==1:
                grid[x][y]=0
                return 1+find_area(x-1,y)+find_area(x+1,y)+find_area(x,y-1)+find_area(x,y+1)
            else:
                return 0
        for x in range(a):
            for y in range(b):
                if (grid[x][y]==1):
                    area=max(area,find_area(x,y))
        return area
