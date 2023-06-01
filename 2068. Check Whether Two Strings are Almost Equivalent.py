class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        map1 = {}
        map2 = {}
        for i in word1:
            map1[i] = map1.get(i, 0) + 1
        for i in word2:
            map2[i] = map2.get(i, 0) + 1
        for i in word1:
            if abs(map1[i] - map2.get(i, 0)) > 3:
                return False
        for i in word2:
            if abs(map2[i] - map1.get(i, 0)) > 3:
                return False
        return True
