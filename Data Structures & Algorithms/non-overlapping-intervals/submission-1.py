class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key = lambda x:x[1])
        tbr = 0
        prev_interval = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] < prev_interval[1]:
                tbr += 1
            else:
                prev_interval = intervals[i] #the last valid ie not removed interval
        return tbr



        