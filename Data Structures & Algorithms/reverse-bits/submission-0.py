class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n:
            bits.append(str(n % 2))
            n = n >> 1

        while len(bits) < 32:
            bits.append("0")
        res = 0
        power = 0
        for char in bits[::-1]:
            res += int(char) * (2**power)
            power += 1
        return res

        
        