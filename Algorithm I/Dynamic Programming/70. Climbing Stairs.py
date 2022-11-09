class Solution:
    def climbStairs(self, n: int) -> int:
        ans=[0]*46
        ans[0],ans[1],ans[2]=1,1,2
        for i in range(3,n+1):
            ans[i]=ans[i-1]+ans[i-2]
        return ans[n]
