class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t): return False
        for a in s:
            chars[a] = chars.get(a , 0) + 1
        
        for i in t:
            if( i in chars ):
                chars[i] = chars.get(i) - 1
        
        for a in chars:
            if chars[a] != 0: return False
        return True
