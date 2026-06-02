class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        while i < j:
            num_sum = numbers[i] + numbers[j]
            if num_sum == target:
                return [i+1, j+1]
            if num_sum > target:
                j-=1
            else:
                i+=1
        raise RuntimeError("Unexpected case")
        