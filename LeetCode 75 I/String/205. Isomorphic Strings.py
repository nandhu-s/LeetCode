class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1_st, map2_ts = {}, {}
        for ch1, ch2 in zip(s, t):
            if (ch1 in map1_st and map1_st[ch1] != ch2) or (ch2 in map2_ts and map2_ts[ch2] != ch1):
                return False
            map1_st[ch1] = ch2
            map2_ts[ch2] = ch1
        return True
