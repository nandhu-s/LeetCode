class Solution:
    def rob(self, nums: List[int]) -> int:
        plan1, plan2 = 0, 0
        for money in nums:
           rob_plan = max(plan1 + money, plan2)
           plan1 = plan2
           plan2 = rob_plan
        return plan2
