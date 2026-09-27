class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        #iterate through str in strings and key:value
        #sorted word: other words

        if not strs:
            return [[""]]

        for word in strs:
            key = "".join(sorted(word))

            anagrams[key].append(word)
        return list(anagrams.values())        