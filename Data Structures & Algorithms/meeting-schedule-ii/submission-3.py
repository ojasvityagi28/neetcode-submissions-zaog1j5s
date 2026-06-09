"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        i = 0
        j = 0
        res = 0
        while i < len(start):
            if start[i] < end[j]:# meeting started before another began
                rooms +=1
                i+=1
            else: #meeting has ended 
                rooms -=1
                j+=1
            res = max(res, rooms)
        return res
            

            

            
                




        