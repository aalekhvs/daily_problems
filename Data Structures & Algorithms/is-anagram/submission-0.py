class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = {}

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        
        for char in t:
            if char not in s_freq or s_freq[char] <= 0:
                return False
            s_freq[char] -= 1
        return True