class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        fsum, bsum = 0, sum(nums)
        for index, num in enumerate(nums):
            fsum += num
            if fsum == bsum:
                return index
            bsum -= num
        return -1
