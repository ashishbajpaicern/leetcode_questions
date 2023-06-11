class Solution:
    def countAsterisks(self, s: str) -> int:
        flag = 0
        count = 0
        for i in s:
            if i == "|":
                if flag == 0:
                    flag = 1
                else:
                    flag = 0
            if i == "*":
                if flag == 1:
                    continue
                else:
                    count += 1
        return count
