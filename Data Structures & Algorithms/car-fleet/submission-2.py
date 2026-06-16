class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        prev_time = (target - pairs[0][0])/pairs[0][1]
        fleets = 1
        for i in range(len(pairs)):
            curr_time = (target - pairs[i][0])/pairs[i][1]
            if curr_time > prev_time:
                fleets +=1
                prev_time = curr_time
        return fleets
        