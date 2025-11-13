# https://neetcode.io/problems/string-encode-and-decode?list=blind75

class Solution:

    def encode(self, strs: List[str]) -> str:

        # input: ["neet","code","love","you"]
        # output: "4#neet4#code4#love3#you"

        res = []
        for s in strs:
            n = len(s)
            res.append(f"{n}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        # input: "4#neet4#code4#love3#you"
        # output: ["neet","code","love","you"]

        n = len(s)
        i = 0
        res = []

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + length + 1
            res.append(s[j+1:i])
        
        return res
