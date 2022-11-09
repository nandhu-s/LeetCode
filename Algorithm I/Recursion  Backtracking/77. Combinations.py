class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def find_ans(start, current_combination):
            if len(current_combination)==k:
                answer.append(current_combination.copy())
                return
            for i in range(start, n+1):
                current_combination.append(i)
                find_ans(i+1, current_combination)
                current_combination.pop()
        find_ans(1, [])
        return answer
