class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            req_n = target - n
            if req_n in seen:
                return [seen[req_n], i]
            else:
                seen[n] = i