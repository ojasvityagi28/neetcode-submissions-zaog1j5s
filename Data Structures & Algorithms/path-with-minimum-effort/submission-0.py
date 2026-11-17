class Solution:
    def minimumEffortPath(self ,heights):
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_reach(limit):
            visited = set()
            stack = [(0, 0)]
            visited.add((0, 0))

            while stack:
                r, c = stack.pop()
                if r == rows - 1 and c == cols - 1:
                    return True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if (nr, nc) in visited:
                        continue
                    if abs(heights[nr][nc] - heights[r][c]) > limit:
                        continue  # this jump is too big, skip it
                    visited.add((nr, nc))
                    stack.append((nr, nc))

            return False

        low = 0
        high = 10**6
        result = high

        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                result = mid       # mid works, save it
                high = mid - 1     # then look for something smaller
            else:
                low = mid + 1      # mid is too small
        return result