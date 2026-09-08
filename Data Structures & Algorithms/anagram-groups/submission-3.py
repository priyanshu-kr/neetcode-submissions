from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for each_str in strs:
            freq = [0] * 26

            for char in each_str:
                index = ord(char) - ord('a')
                freq[index] += 1
            
            signature = tuple(freq)

            if signature in groups:
                groups[signature].append(each_str)
            else:
                groups[signature] = [each_str]

        return list(groups.values())