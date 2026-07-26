class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(f"{len(word)}#{word}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            res.append(word)
            i += length
        return res
        
