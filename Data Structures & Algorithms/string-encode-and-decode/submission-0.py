from typing import List

### Length-Prefix Solution:

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find position of delimiter '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1  # Move past '#'
            res.append(s[i : i + length])
            i += length  # Jump past the extracted string

        return res