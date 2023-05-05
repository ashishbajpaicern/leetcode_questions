class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        m = {}
        for i in ransomNote:
            r[i] = r.get(i, 0) + 1
        for i in magazine:
            m[i] = m.get(i, 0) + 1
        for i in r:
            if i not in m:
                return False
            elif r[i] > m[i]:
                return False
        return True
