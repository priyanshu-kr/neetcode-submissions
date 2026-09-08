class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freq_buckets = {}
        for element, count in freq.items():
            if count not in freq_buckets:
                freq_buckets[count] = []
            
            freq_buckets[count].append(element)

        result = []
        for freq in range(len(nums), 0, -1):
            if freq in freq_buckets:

                for element in freq_buckets[freq]:
                    result.append(element)

                    if len(result) == k:
                        return result