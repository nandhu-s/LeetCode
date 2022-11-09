class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1, w, match = Counter(s1), len(s1), 0     
        for i in range(len(s2)):
            if s2[i] in cs1:
                if not cs1[s2[i]]:
                    match -= 1
                cs1[s2[i]] -= 1
                if not cs1[s2[i]]:
                    match += 1
            if i >= w and s2[i-w] in cs1:
                if not cs1[s2[i-w]]:
                    match -= 1
                cs1[s2[i-w]] += 1
                if not cs1[s2[i-w]]:
                    match += 1
            if match == len(cs1):
                return True
        return False
