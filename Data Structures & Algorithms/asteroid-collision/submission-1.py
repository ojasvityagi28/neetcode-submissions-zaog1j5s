class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        n = len(asteroids)
        survivors = []

        for r in range(n):
            destroyed = False
            while survivors and (asteroids[r] < 0 and survivors[-1] > 0):
                s = abs(survivors[-1])
                a = abs(asteroids[r])

                if s == a:
                    survivors.pop()
                    destroyed = True
                    break
                elif s < a:
                    survivors.pop()
                else:
                    destroyed = True
                    break
            if not destroyed:
                survivors.append(asteroids[r])
        return survivors

                    
        