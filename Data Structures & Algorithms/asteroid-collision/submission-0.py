class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        survivors = []
        n = len(asteroids)

        for i in range(n):
                destroyed = False
                while survivors and (asteroids[i] < 0 and survivors[-1] > 0):

                    if abs(survivors[-1]) == abs(asteroids[i]):
                        survivors.pop()
                        destroyed = True
                        break
                    elif abs(survivors[-1]) > abs(asteroids[i]):
                        destroyed = True
                        break
                    else:
                        survivors.pop()

                if not destroyed:
                    survivors.append(asteroids[i])
        return survivors
                    
        