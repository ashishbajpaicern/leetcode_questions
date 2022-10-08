class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        col = list(colors)
        res = 0
        for i in range(1, len(col)):
            if col[i] == col[i - 1]:
                res += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return res
