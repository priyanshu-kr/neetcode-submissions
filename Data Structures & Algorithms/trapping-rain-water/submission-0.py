class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        L = 0
        R = len(height) - 1

        left_max = 0
        right_max = 0

        while L < R:
            if height[L] <= height[R]:
                left_max = max(left_max, height[L])
                water += left_max - height[L]
                L += 1

            else:
                right_max = max(right_max, height[R])
                water += right_max - height[R]
                R -= 1

        return water