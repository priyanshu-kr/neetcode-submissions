class Solution:
    def maxArea(self, height: list[int]) -> int:
        L = 0
        R = len(height) - 1
        result = 0
        
        while L < R:
            current_area = (R - L) * min(height[L], height[R])
            result = max(result, current_area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return result