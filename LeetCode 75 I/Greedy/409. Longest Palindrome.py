class Solution:
    def longestPalindrome(self, s: str) -> int:
        c_dict = {}
        for i in s:
            if i not in c_dict:
                c_dict[i] = 1
            else:
                c_dict[i] += 1
        ans = odd = 0
        for i in c_dict:
            if c_dict[i]%2 == 0:
                ans += c_dict[i]
            else:
                ans += c_dict[i]-1
                odd=1
        return ans+odd
