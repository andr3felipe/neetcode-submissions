class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in cache:
                return [cache[diff], index]
            cache[number] = index
        
        return []