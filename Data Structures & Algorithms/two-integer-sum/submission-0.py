class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        # for i, num in enumerate(nums):
        #     index_map[num] = i
        
        # for i, num in enumerate(nums):
        #     if target - num in index_map and index_map[target - num] != i:
        #         return [i, index_map[target - num]]

        for i, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target - num], i]
            index_map[num] = i
        return []
        