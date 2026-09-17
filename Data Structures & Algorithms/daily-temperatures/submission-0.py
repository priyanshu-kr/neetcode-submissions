class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            while len(stack) != 0 and temperatures[i] >= stack[-1][0]:
                stack.pop()

            if len(stack) != 0:
                answer[i] = stack[-1][1] - i

            stack.append((temperatures[i], i))
        
        return answer