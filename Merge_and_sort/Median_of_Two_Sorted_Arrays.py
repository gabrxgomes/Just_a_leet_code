class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #for this leetcode i need merge the two
        #arrays and take the middle number using slice? Maybe

        #merged = sorted(nums1 + nums2)

        #well the first thing is to define an variable for receiving the merged array, then containing (nums1 + nums2)
        
        
        merged = sorted(nums1 + nums2)
        mergedlen = len(merged)


        if mergedlen % 2 == 0:
            return (merged[mergedlen//2 - 1] + merged[mergedlen//2]) / 2.0
        else:
            return merged[mergedlen//2]


        


