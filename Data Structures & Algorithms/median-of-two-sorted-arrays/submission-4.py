class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2
        if len(nums2) < len(nums1):
            A , B = B , A
        l = 0
        r = len(A) - 1
        total = len(A) + len(B)
        half = total//2

        while True:
            i = ( l + r )//2
            j = half - (i + 1) - 1

            ALeft = A[i] if i >= 0 else float('-inf')
            ARight = A[i + 1] if i + 1 < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j + 1] if j + 1 < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight))/2
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1
        


        
        