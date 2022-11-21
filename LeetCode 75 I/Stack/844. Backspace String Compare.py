class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in s:
            if i == '#' and s_stack:
                s_stack.pop()
                continue
            if i != '#': s_stack.append(i)
        for i in t:
            if i == '#' and t_stack:
                t_stack.pop()
                continue
            if i != '#': t_stack.append(i)
        return s_stack == t_stack
