class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {0: 0}
        for i in wall:
            sum = 0
            for j in i[:-1]:
                sum = sum + j
                d[sum] = 1 + d.get(sum, 0)
        return len(wall) - max(d.values())
