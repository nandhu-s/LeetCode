class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            poss_perm=self.permute(nums)
            for perm in poss_perm:
                perm.append(n)
            answer.extend(poss_perm)
            nums.append(n)
        return answer
