class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        m = 0
        l = len(nums3)
        print(l)
        if (l % 2 == 0):
            return (nums3[(l//2)-1]+nums3[(l//2)])/2
        else:
            return (nums3[l//2])
        return (m)
