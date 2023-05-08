class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            st = "".join(sorted(s))
            if st not in d:
                d[st] = [s]
            else:
                d[st].append(s)
        final = []
        for value in d.values():
            final.append(value)
        return final
