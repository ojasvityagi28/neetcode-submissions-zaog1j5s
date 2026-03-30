class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # hours = math.ceil(piles[0]/speed) +....+piles[i]/speed
        # if h < hours:
        #     increase speed
        # if h > hours:
        #     decrease speed
        # else:
        #     k = min(k,res)
        #     decrease speed
        low = 1
        high = max(piles)
        k= float('inf')
        while low <= high:
            speed = (low + high)//2
            hours = 0# hours should be reset everytime a new speed is decided
            for a in piles:
                hours += math.ceil(a/speed)
            if h < hours:
                low = speed+1
            elif h > hours:
                high = speed - 1
                k = min(speed, k)
            else:
                k = speed
                high = speed - 1
        return k


        