class Solution:
    # Longest possilbe sequence is length of the nums
    # [0, 1, 2, 3, 5, 4]
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) in numSet:
                continue
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
        return longest