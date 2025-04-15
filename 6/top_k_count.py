from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        max_freq = max(count.values()) if count else 0
        
        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []

        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
        
