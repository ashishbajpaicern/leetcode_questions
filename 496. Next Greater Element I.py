class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            flag = 0
            for j in range(index, len(nums2)):
                if nums1[i] < nums2[j]:
                    nums1[i] = nums2[j]
                    flag = 1
                    break
            if flag == 0:
                nums1[i] = -1
        return nums1
