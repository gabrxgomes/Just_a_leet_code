class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            real_length = right - left + 1
            if real_length > result:
                result = real_length
        return result

#*Given a string s, find the length of the longest substring without repeating characters.
