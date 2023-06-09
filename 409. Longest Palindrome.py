class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1

        flag = 0
        count = 0
        for i in d:
            if d[i] == 1:
                flag = 1
                continue
            if d[i] % 2 != 0:
                flag = 1
                count = count + d[i] - 1
            else:
                count = count + d[i]
        if flag == 1:
            count += 1
        return count
