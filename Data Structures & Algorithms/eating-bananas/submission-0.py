class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        result = max(piles)

        while L <= R:
            k = (L + R) // 2
            hours = 0

            for p in piles:
                hours += (p + k - 1) // k

            if hours <= h:
                result = k
                R = k - 1
            else:
                L = k + 1

        return result