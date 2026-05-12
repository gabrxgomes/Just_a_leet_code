class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # in this case, my input is a integer value, and my output value is a
        # string value.

        #the worst solution is iterate in all values more 2 times
        #the complexity in this moment if i isnt see the constraints
        #is a O(n), lets see the constraints.


        #the constraint is a O(1) solution.

        #for solve this problem i need to receive a integer imput
        #2 - i need to count the integer for undestanding the decimal value
        #3 - i need to append a new list the roman numbers based in the decimal value
        #4 - i need to convert the list type in string type

        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
            (10,  "X"),  (9,  "IX"), (5,  "V"),  (4,  "IV"),
            (1,   "I")
        ] # this is a dictionary of tuples

        result = []
        for value, symbol in values:
            while num >= value: # for K, V in values:
                result.append(symbol) # append the symbol in the result list
                num -= value # decrease the num value by the value of the symbol, and swap the value
                            #for the simbol
        return "".join(result) #append the list in a string type, and return the result







