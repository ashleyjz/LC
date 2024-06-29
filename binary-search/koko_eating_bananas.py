# 875 medium

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k: int) -> int:
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / float(k))
            return time

        # speeds = [i for i in range(1, max(piles)+1)]
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            k = (left + right) // 2
            time = eat(k)
            # print(f'left:{left}, right:{right}, k:{k}, time:{time}')
            if time <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1
        return ans