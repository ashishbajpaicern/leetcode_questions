class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_contained = (r-l) * min(height[l], height[r])
        while l < r:
            max_contained = max(max_contained, (r-l) *
                                min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_contained
