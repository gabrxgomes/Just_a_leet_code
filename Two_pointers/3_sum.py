class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: #This line compare the current number with the previous one, 
                                                #and if they are the same, it skips the current iteration of the loop. 
                                                #This is done to avoid processing duplicate numbers and 
                                                #generating duplicate triplets in the result.
                continue                    # pula duplicata de i

            left, right = i + 1, len(nums) - 1 #here the code discarts the current number and 
                                                #starts the two pointers from the next number (i + 1) and 
                                                #the end of the array (len(nums) - 1) [i..--->L........R<-----]

            while left < right:
                total = nums[i] + nums[left] + nums[right]#the result i expect is zero(0)

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]]) # append all right values can the sum results in zero(0)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1           # pula duplicata de left
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1          # pula duplicata de right
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result