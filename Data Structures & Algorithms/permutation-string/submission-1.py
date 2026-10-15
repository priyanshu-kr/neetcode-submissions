class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        matches =  0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        if matches == 26:
                return True
        
        def update_count(idx, delta):
            nonlocal matches

            if count1[idx] == count2[idx]:
                matches -= 1
            
            count2[idx] += delta

            if count1[idx] == count2[idx]:
                matches += 1

        L = 0
        for R in range(len(s1), len(s2)):
           
            idx1 = ord(s2[L]) - ord('a')
            update_count(idx1, -1)

            idx2 = ord(s2[R]) - ord('a')
            update_count(idx2, +1)

            L += 1

            if matches == 26:
                return True
        
        return matches == 26