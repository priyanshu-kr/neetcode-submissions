from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for each_str in strs:
            
            freq = {each_char: 0 for each_char in ascii_lowercase}

            for char in each_str:
                freq[char] += 1
            
            signature = tuple(freq.values())

            if signature in groups:
                groups[signature].append(each_str)
            else:
                groups[signature] = [each_str]

        return list(groups.values())


