class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_len = 0

        for x in nums_set:
            if x-1 in nums_set:
                continue
        
            current_len = 1
            current = x

            while current+1 in nums_set:
                current_len += 1
                current +=1
        
            longest_len = max(longest_len, current_len)

        return longest_len