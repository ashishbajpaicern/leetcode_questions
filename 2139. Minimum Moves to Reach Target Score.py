class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        if maxDoubles == 0:
            return (target-1)
        while target >= 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target = target // 2
                    count += 1
                    maxDoubles -= 1
                    continue
            elif maxDoubles == 0:
                return count+target-1
            target -= 1
            count += 1
        return count-1
