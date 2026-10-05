class Solution:
    def arrangeCoins(self, n: int) -> int:
        mask = 1 << 15
        rows = 0
        while mask > 0:
            rows |= mask
            coins = rows * (rows + 1) // 2
            if coins > n:
                rows ^= mask
            mask >>= 1
        return rows