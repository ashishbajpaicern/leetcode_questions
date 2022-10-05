class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        m = 0
        check = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        print(d)
        for i in range(k):
            max_key = max(d, key=d.get)
            ans.append(max_key)
            del d[max_key]
        return(ans)
