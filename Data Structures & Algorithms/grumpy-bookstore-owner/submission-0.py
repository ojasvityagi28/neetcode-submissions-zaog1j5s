class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        l = 0
        res = 0
        custs = 0
        base = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        for r in range(len(customers)):
            if grumpy[r] == 1:
                custs += customers[r]

            while minutes < r - l + 1:
                custs -= customers[l] if grumpy[l] == 1 else 0
                l += 1

            res = max(custs, res)

        return res + base