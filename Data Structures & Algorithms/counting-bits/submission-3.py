class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for number in range(n + 1):
            bits = 0
            while number:
                bits += number % 2
                number = number//2
            res.append(bits)
        return res

    # def convertToBinary(self,n : int):
    #     res = []
    #     while n:
    #         res.append(str(n % 2))
    #         n = n//2
    #     return int("".join(res))
        