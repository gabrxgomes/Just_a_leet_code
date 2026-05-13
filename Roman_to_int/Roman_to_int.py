class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        """
        for solve this problem, the things i can do is:
            1 - create the list of tuples for simbol-value
            2 - define the empty list []
            3 - extract the len for s input
        """

        values = {
            "I": 1,  "V": 5,   "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        } # what this is a dicts? for this problem us need to acess the value of the simbol, 
            #and for this reason i need to create a dicts for access the value of the simbol in O(1) time complexity

        result = 0
        
        for i in range(len(s)):
            curr = values[s[i]]
            next_ = values[s[i+1]] if i+1 < len(s) else 0

            if curr < next_:
                result -= curr   # caso subtrativo: IV, IX, XL...
            else:
                result += curr   # caso normal
        return result