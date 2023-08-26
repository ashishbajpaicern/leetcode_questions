class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = set(groupSizes)
        res = []
        for i in g:
            ins = []
            for j in range(len(groupSizes)):
                if i == groupSizes[j]:
                    ins.append(j)
                if len(ins) == i:
                    res.append(ins)
                    ins = []
            if ins != []:
                res.append(ins)
        return res

    """
    class Solution:
    # Time: O(n)
    # Space: O(n)
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res, dic = [], {}
        for idx, group in enumerate(groupSizes):
            if group not in dic:
                dic[group] = [idx]
            else:
                dic[group].append(idx)
            
            if len(dic[group]) == group:
                res.append(dic[group])
                del dic[group]
        return res
    """
