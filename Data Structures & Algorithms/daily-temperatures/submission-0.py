class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(len(temperatures) - 1, -1, -1):

            while(len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]):
                stack.pop()

            if(len(stack) > 0 and temperatures[i] < temperatures[stack[-1]]):
                ans[i] = stack[-1] - i


            #when stack is empty
            stack.append(i)
                
        return ans
