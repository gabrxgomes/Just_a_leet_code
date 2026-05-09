class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()

        if len(s) == 0:
            return 0

        sign = 1
        index = 0
        result = 0

        if s[0] == "-":
            sign = -1
            index = 1
        elif s[0] == "+":
            index = 1

        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result = result * sign

        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result