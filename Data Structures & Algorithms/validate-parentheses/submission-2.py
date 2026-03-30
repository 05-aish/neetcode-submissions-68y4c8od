class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '[' : ']',
            '(' : ')',
            '{' : '}',
        }
        stack = []

        for i in s:
            if (i in '[({'):
                stack.append(i)
            elif (i in '])}'):
                if (len(stack) == 0 or hmap[stack[-1]] != i):
                    return False
                stack.pop()

        return len(stack) == 0
