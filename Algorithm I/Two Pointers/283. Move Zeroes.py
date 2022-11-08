class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans=[0]*len(nums)
        i=0
        for t in nums:
            if t!=0:
                ans[i]=t
                i+=1
        for i in range(len(nums)):
            nums[i]=ans[i]
        nums=ans
