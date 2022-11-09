class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s=s.lower()
        length, ans = len(s), []
        def find(i, res=''):
            if i<length:
                find(i+1,res+s[i])
                if s[i].islower():
                    find(i+1,res+s[i].upper())
            else:
                ans.append(res)
        find(0,'')
        return ans
