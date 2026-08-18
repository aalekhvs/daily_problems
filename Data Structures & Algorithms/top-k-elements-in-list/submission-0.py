class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in freq_map.items():
            buckets[value].append(key)
        
        res = []
        
        for bucket in reversed(buckets):
            for num in bucket:
                if k > 0:
                    res.append(num)
                    k -= 1
                if k == 0:
                    return res
