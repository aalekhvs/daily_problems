class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            for i in range(min(len(word), len(prefix))):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            else:
                prefix = prefix[:len(word)]
        return prefix