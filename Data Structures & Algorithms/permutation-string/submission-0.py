class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        count2 = {}

        for i in s1:
            count1[i] = count1.get(i, 0) + 1

        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        if count1 == count2:
            return True
        
        L = 0
        for R in range(len(s1), len(s2)):
            count2[s2[L]] -= 1
 
            if count2[s2[L]] == 0:
                count2.pop(s2[L])

            L += 1

            count2[s2[R]] = count2.get(s2[R], 0) + 1

            if count1 == count2:
                return True
            
            pass
        
        return False