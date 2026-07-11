class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0X7FFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a^b) & mask #mask is just 32 1 bits which we keep the no exactly same
            #but remove extra bits
            b = carry & mask
        return a if a <= max_int else ~(a ^ mask)
        