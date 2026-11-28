# eader: "dict of key → sorted [time, value] list; get = binary search for latest time ≤ timestamp
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result

tm = TimeMap()
tm.set("foo", "bar", 1)
tm.set("foo", "bar2", 4)
print(tm.get("foo", 1))    # bar
print(tm.get("foo", 3))    # bar
print(tm.get("foo", 4))    # bar2
print(tm.get("foo", 5))    # bar2
print(tm.get("foo", 0))    # (empty)
print(tm.get("baz", 1))    # (empty)