class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()

        for i in range (0, len(nums)):
            
            windowStart = i - k + 1
            while dq and dq[0] < windowStart:
                dq.popleft()

            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result