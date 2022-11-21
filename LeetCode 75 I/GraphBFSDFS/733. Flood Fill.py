class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        in_color=image[sr][sc]
        def fill_color(x,y):
            if x<0 or y<0 or x>=len(image) or y>=len(image[0]) or image[x][y]==color or image[x][y]!=in_color:
                return
            image[x][y]=color
            fill_color(x-1,y)
            fill_color(x+1,y)
            fill_color(x,y-1)
            fill_color(x,y+1)
        fill_color(sr,sc)
        return image
