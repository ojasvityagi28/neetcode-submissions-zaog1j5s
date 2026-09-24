class TimeMap:

    def __init__(self):
        self.timevaluestore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timevaluestore:
            self.timevaluestore[key] = []

        self.timevaluestore[key].append((value , timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timevaluestore:
            return ""
        
        values = self.timevaluestore[key]
        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r)//2

            time = values[mid][1]

            if time < timestamp:
                res = values[mid][0]
                l = mid + 1
            elif time > timestamp:
                r = mid - 1
            else:
                return values[mid][0]
        return res 




        
