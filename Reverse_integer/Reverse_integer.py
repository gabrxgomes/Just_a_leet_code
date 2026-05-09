class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #the first think is to convert the integer to a string, then reverse the string and convert it back to an integer, 
        #if the integer is negative then we need to add a negative sign at the end of the reversed string, 
        #if the reversed integer is greater than 2^31 - 1 or less than -2^31 then we need to return 0

        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_str = str(x_abs)[::-1]
        reversed_int = sign * int(reversed_str)

        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int

