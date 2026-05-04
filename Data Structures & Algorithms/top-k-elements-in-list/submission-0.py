from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=Counter(nums)
        sorted_dict=dict(sorted(s.items(), key=lambda item:item[1]))

        return list(sorted_dict.keys())[-k:]
