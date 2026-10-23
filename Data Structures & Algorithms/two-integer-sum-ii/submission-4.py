class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l < r:
            sumii = numbers[l] + numbers[r]
            if target < sumii:
                r -=1
            elif target > sumii:
                l +=1
            else:
                return [l+1,r+1]
    
        