class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        L = 0
        R = 0
        characters = set()

        for R in range(len(s)):
            
            while s[R] in characters:
                characters.remove(s[L])
                L += 1

            characters.add(s[R])            
           
            max_length = max(R-L+1, max_length)

        return max_length