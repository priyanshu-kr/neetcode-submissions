class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1
        
        window = {}
        have = 0
        need_count = len(need)
        
        L = 0
        min_len = float('inf')
        min_start = 0

        for R in range(0, len(s)):
            window[s[R]] = window.get(s[R], 0) + 1

            if s[R] in need and window[s[R]] == need[s[R]]:
                have += 1
            
            while have == need_count:
                current_len = R - L + 1

                if current_len < min_len:
                    min_len = current_len
                    min_start = L
                
                char = s[L]

                if char in need and window[char] == need[char]:
                    have -= 1
                
                window[char] -= 1
                L += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_start : min_start + min_len]  