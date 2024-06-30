# 981 medium

class TimeMap:

    def __init__(self):
        self._entries = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._entries:
            self._entries[key].append((timestamp, value))
        else:
            self._entries[key] = [(timestamp, value)]
        # print(f'key:{key}, entries[key]:{self._entries[key]}')

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._entries:
            return ''
        storage = self._entries[key]
        left = 0
        right = len(storage) - 1
        value = ''
        while left <= right:
            half = (left + right) // 2
            if storage[half][0] <= timestamp:
                value = storage[half][1]
                left = half + 1
            else:
                right = half - 1
        return value
