class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output = {}
        for i, l1 in enumerate(list1):
            if l1 in list2:
                output[l1] = i + list2.index(l1)
        return [i for i, j in output.items() if j == min(output.values())]
