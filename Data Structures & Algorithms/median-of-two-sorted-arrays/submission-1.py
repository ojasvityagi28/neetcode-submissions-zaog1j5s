class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i , j = 0 , 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j += 1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        l , r = 0 , len(merged)
        if len(merged) % 2 == 1:
            mid = (l + r)//2
            return merged[mid]
        else:
            mid = (l + r)//2
            median = (merged[mid] + merged[mid - 1])/2
            return median
        

        