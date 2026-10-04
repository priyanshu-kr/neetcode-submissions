class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1

        while L <= R:

            mid = (L + R) // 2

            if nums[mid] == target:
                return mid

            if nums[L] <= nums[mid]:          # left half is sorted
                if nums[L] <= target < nums[mid]:      # target is in left half
                    R = mid - 1
                else:
                    L = mid + 1

            else:                           # right half is sorted
                if nums[mid] < target <= nums[R]:      # target is in right half
                    L = mid + 1
                else:
                    R = mid - 1
            
        return -1