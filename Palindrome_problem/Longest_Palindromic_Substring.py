class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #the first think is use two pointers for the start and end of the string, then check if the characters 
        #are the same, if they are the same then move the pointers towards the center, if they are not the same 
        #then move the end pointer to the left and check again, if they are not the same then move the start pointer 
        #to the right and check again, if they are not the same then move both pointers towards the 
        #center and check again, if they are not the same then return the longest palindrome found so far


        longest = ""
        for i in range(len(s)):
            #odd length palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

            #even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]
                left -= 1
                right += 1

        return longest  