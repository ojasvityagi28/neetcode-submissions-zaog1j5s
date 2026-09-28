class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2

        if len(nums2) < len(nums1):
            A , B = nums2 , nums1
        
        l = 0
        r = len(A) - 1

        total = (len(nums1) + len(nums2))
        half = total // 2

        while True:
            i = (l + r)//2

            j = half - (i + 1) - 1

            a_left = A[i] if i >= 0 else float('-inf')
            a_right = A[i + 1] if (i + 1) < len(A) else float('inf')
            b_left = B[j] if j >= 0 else float('-inf')
            b_right = B[j + 1] if (j + 1) < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right))/2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1
        
        