class Solution(object):
    def uniquePairs(self, nums, target):
        left, right = 0, len(nums) - 1
        result = []

        while left < right:
            if nums[left] + nums[right] == target:
                result.append((nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return result