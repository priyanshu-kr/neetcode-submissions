class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        L = 0
        R = m * n - 1

        while L <= R:
            mid = (L + R) // 2
            r = mid // n
            c = mid % n
            value = matrix[r][c]

            if value == target:
                return True
            elif value < target:
                L = mid + 1
            else:
                R = mid - 1

        return False