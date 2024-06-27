# 49 medium

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_dist = defaultdict(list)
        for s in strs:
            dist = [0] * 26;
            for char in s:
                dist[ord(char) - ord('a')] += 1
            letter_dist[tuple(dist)].append(s)

        return letter_dist.values()