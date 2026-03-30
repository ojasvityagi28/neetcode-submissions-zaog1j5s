class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if target < matrix[mid][0] :
                r = mid -1
            elif target > matrix[mid][len(matrix[mid])-1]:
                l = mid +1
            else:
                low = 0
                high = len(matrix[mid])-1
                while low <= high:
                    middle = (low+high)//2
                    if matrix[mid][middle]==target:
                        return True
                    elif target < matrix[mid][middle]:
                        high = middle - 1
                    else:
                        low = middle + 1
                return False
        return False

        