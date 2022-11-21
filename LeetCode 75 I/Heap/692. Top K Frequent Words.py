class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wdict=Counter(words)
        words=sorted(wdict.items(),key=lambda x:(-x[1],x[0]))
        ans=[]
        for i,j in words[:k]:
            ans.append(i)
        return (ans)
            
