class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            
            if i == n:
                current_height = 0
            else:
                current_height = heights[i]

            while stack and current_height < heights[stack[-1]]:
                popped_index = stack.pop()
                rectangle_height = heights[popped_index]
                
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                area = rectangle_height * width
                max_area = max(area, max_area)
            
            if i < n:
                stack.append(i)

        return max_area