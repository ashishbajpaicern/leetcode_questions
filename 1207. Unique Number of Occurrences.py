class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uni = []
        check = []
        for i in arr:
            if i not in uni:
                uni.append(i)
        for i in uni:
            a = arr.count(i)
            if a not in check:
                check.append(a)
            else:
                return False
        return True
