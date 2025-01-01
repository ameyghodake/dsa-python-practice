# array nums [], positive_int target
# Minimal length of subarray sum >= target
# If no subarray then return 0 instead


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        start = 0 
        current_sum = 0
        min_length = float('inf')

        for end in range(n):
            current_sum = current_sum + nums[end]

            while current_sum >= target:
                min_length = min(min_length, end-start+1)
                current_sum = current_sum - nums[start]
                start = start+1
        return min_length


target = 51
nums = [1, 4, 45, 6, 0, 19]
obj = Solution()
print(obj.minSubArrayLen(target, nums))