# 347 medium

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        freqs = [[] for i in range(len(nums)+1)]

        for num, ct in counts.items():
            if ct != 0:
                freqs[ct].append(num)

        ans = []
        for i in range(len(freqs) - 1, 0, -1):
            if len(freqs[i]) != 0:
                for f in freqs[i]:
                    ans.append(f)
            if len(ans) >= k:
                break
        return ans