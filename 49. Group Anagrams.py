"""
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
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord("a")] += 1
            d[tuple(count)].append(i)
        print(d)
        return d.values()
