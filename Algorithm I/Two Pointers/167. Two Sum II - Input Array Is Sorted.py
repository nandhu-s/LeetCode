class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,v in enumerate(numbers):
            if target-v in d:
                return d[target-v],i+1
            d[v]= i+1
