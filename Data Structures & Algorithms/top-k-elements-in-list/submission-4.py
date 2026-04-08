class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[:k]
 