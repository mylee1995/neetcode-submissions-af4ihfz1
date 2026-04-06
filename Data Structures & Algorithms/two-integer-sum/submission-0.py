class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i, num in enumerate(nums):
            matching_number = target - num
            if matching_number in counter:
                return [counter[matching_number], i]
            else:
                counter[num] = i