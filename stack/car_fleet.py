# 853 medium

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        fleets = []
        for (pos, spd) in cars:
            arrive = (target - pos) / spd
            if not (len(fleets) > 0 and arrive <= fleets[-1]):
                fleets.append(arrive)
        return len(fleets)
