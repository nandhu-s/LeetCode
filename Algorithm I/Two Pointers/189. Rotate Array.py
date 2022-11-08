class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        t=[0]*l
        for i in range(l):
            t[(i+k)%l]=nums[i]
        for i in range(l):
            nums[i]=t[i]        
