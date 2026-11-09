class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        interval = points[0]
        res = 1

        for i in range(1, len(points)):
            if not (interval[0] <= points[i][0] <= interval[1]):
                res += 1
                interval = points[i]
            else:
                interval = [points[i][0], min(interval[1], points[i][1])]
        return res

