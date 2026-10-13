class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        max_frequency = 0
        result = 0

        for R in range(len(s)):

            count[s[R]] = count.get(s[R], 0) + 1

            max_frequency = max(max_frequency, count[s[R]])

            while (R - L + 1) - max_frequency > k:
                count[s[L]] -= 1
                L += 1
            
            result = max(result, R - L + 1)
        
        return result