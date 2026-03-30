class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        i = 0
        window = set()
        maxLength = 0
        for j in range(len(s)):
            while(s[j] in window):
                window.remove(s[i])
                i = i + 1
            window.add(s[j])
            maxLength = max(maxLength, j - i + 1)
        return maxLength
            
            