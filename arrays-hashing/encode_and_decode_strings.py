# ? medium

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        idx = 0
        while idx < len(s):
            n = idx
            while s[n] != "#":
                n += 1
            result.append(s[n+1 : n + int(s[idx:n]) + 1])
            idx = n + int(s[idx:n]) + 1
        return result

    arr = ["we","say",":","yes","!@#$%^&*()"]
    # print(encode(arr, arr))
    assert(decode("", encode(arr, arr)) == arr)
