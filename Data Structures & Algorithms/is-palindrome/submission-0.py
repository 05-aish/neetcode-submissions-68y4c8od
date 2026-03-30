class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(cleanString) - 1
        while (i <= j):
            if (cleanString[i] == cleanString[j]):
                i = i + 1
                j = j - 1
            else:
                return False
        return True
        