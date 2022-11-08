class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        srt,end=0,len(nums)-1
        while(srt<=end):
            m=(srt+end)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                end=m-1
            else:
                srt=m+1
        return srt
