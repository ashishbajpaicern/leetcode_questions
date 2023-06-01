class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = 0
        slow = 0
        fast = 1
        stack = [0]
        while fast != len(prices):
            if prices[slow] > prices[fast]:
                slow += 1
                continue
            elif prices[slow] == prices[fast]:
                fast += 1
            else:
                stack.append(prices[fast] - prices[slow])
                fast += 1
        return max(stack)
