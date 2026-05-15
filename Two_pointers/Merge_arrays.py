class Solution(object):
    def merge(self, nums1, nums2):
        left, right = 0
        result = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                result.append(nums1[left])
                left += 1
            else:
                result.append(nums2[right])
                right += 1
        result.extend(nums1[left:])
        result.extend(nums2[right:])
        return result
    


"""
You're given two sorted arrays of integers merge then into a single sorted array.
For example, if you have arrays one as one, two, three and array two as two
,three, four, the result should be one, two, two, three, three, four.

"""