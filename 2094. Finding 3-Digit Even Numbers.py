class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = {str(x) for x in range(100, 1000, 2)}
        ans = []
        for i in nums:
            for d in i:
                if i.count(d) > digits.count(int(d)):
                    break
            else:
                ans.append(i)
        return sorted(ans)
