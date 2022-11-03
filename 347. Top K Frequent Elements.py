class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        for i in range(k):
            max_key = max(d, key=d.get)
            ans.append(max_key)
            del d[max_key]
        return(ans)
