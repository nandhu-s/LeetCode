class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        c=Counter(nums)
        for i in c:
            if c[i]==1:
                return(i)
        
