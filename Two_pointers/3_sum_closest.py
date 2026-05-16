class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # the correct value is +1 or -1 the value of the target
        # i have to buil the follow logic --> if sum of i + left or i + left + right.. equals target + 1
        # or target - 1, print result.

        #the first action i have to do is declare the default values for left and righ,
        #after this i have to declare an empty list named result = []

        #[-1,2,1,-4]


        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest




