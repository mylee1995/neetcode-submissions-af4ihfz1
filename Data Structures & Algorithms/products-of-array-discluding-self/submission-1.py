class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # abcd -> 1 a ab abc
        # abcd -> dcb dc d 1
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        for i in range(0, len(nums), 1):
            if i == 0:
                continue
            
            forward[i] = forward[i-1] * nums[i-1]
        
        for i in range(len(nums) -1 , -1, -1):
            if i == len(nums)- 1:
                continue
            backward[i] = backward[i+1] * nums[i+1]

        print(forward)
        print(backward)

        result = [1] * len(nums)
        for i in range(0, len(nums), 1):
            result[i] = forward[i] * backward[i]

        return result

            