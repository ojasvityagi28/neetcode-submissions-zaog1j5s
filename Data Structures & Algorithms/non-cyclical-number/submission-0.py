class Solution:
    def isHappy(self, n: int) -> bool:
        happyset = set()
        sumOfDigits = 0
        while sumOfDigits != 1:
            sumOfDigits = 0
            for digit in str(n):
                sumOfDigits += int(digit)**2
 
            if sumOfDigits in happyset:
                return False
            else:
                n = sumOfDigits
            happyset.add(sumOfDigits)
        return True
        


        