class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg = msg + str(len(s)) + "#" + s
        return msg


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        l=""
        while i < len(s):
            while s[i] != "#":
                l += s[i]
                i += 1
            res.append(s[i + 1: i + int(l) + 1])
            i = i + int(l) + 1
            l = ""
        return res