class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st,en=0,len(s)-1
        while st<en:
            s[st],s[en]=s[en],s[st]
            st,en=st+1,en-1
