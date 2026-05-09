class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip() #remove leading and trailing whitespace characters from the string, this is important because we need to ignore any whitespace characters at the beginning of the string, if we don't do this then we might get an error when we try to convert the string to an integer

        if len(s) == 0: #if the string is empty after removing whitespace characters, then we need to return 0 because there is no valid integer to convert
            return 0

        sign = -1 if s[0] == "-" else 1 #ternary operator to check if the first character is a negative sign, if it is then the sign is -1, otherwise it is 1
        index = 1 if s[0] in ("+", "-") else 0 #ternary operator to check if the first character is a positive or negative sign, if it is then the index is 1, otherwise it is 0
        result = 0

        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result = result * sign #apply the sign to the result

        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result