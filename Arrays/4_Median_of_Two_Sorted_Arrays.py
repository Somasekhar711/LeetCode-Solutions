class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = [0] * (len(nums1) + len(nums2))
        median = 0

        i = 0
        j = 0
        k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i += 1
                k += 1
            else:
                arr[k] = nums2[j]
                j += 1
                k += 1

        if i >= len(nums1):
            while j < len(nums2):
                arr[k] = nums2[j]
                j += 1
                k += 1
        else:
            while i < len(nums1):
                arr[k] = nums1[i]
                i += 1
                k += 1

        total_size = len(nums1) + len(nums2)

        if total_size % 2 == 0:
            median = (float(arr[total_size // 2]) +
                      float(arr[(total_size // 2) - 1])) / 2
        else:
            median = float(arr[total_size // 2])

        return median