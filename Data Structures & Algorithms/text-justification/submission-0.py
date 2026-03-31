class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                extra_width = maxWidth - length
                remainder = extra_width % max(1, (len(line) - 1))
                space = extra_width // max(1, len(line) - 1)
                for j in range(max(1, len(line) - 1)):
                    line[j] += space * " "
                    if remainder > 0:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0
        
        last_line = " ".join(line)
        res.append(last_line + " " * (maxWidth - len(last_line)))
        return res