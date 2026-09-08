class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        for n in s:
            dict_s[n] = dict_s.get(n, 0)+1
        
        dict_t = {}
        for m in t:
            dict_t[m] = dict_t.get(m, 0)+1
        
        return dict_s == dict_t