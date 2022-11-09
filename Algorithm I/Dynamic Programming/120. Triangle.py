class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans=[0]*(len(triangle)+1)
        for row in triangle[::-1]:
            for i, v in enumerate(row):
                ans[i]=v+ min(ans[i],ans[i+1])
        return ans[0]
