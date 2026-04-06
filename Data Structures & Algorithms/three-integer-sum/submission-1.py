class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        result = []
        dup_finder = set()

        for i in range(0, len(nums) - 2, 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                num_sum = nums[i] + nums[j] + nums[k]
                num_sum_str = str(nums[i]) + " " + str(nums[j]) + " " + str(nums[k])
                if num_sum == 0 and num_sum_str not in dup_finder:
                    result.append([nums[i], nums[j], nums[k]])
                    dup_finder.add(num_sum_str)
                    j+=1
                    k-=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif num_sum < 0:
                    j+=1
                else:
                    k-=1
                    
        return result