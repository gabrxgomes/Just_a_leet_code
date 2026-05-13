class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        the steps i can think for solve this problem is:
        1 - iterate string input
        2 - compare the indexes of all items in list of strings
        3 - the brute force solution for this is O (n log n)
        because this idea is iterate isoladly in all strings at once.
        4 - The best solution is O(n2), because i dont know how many letters 
        exist in all strings in the list, and, i dont know how many strings
        exists in strs variable.... based in this situation, is for within for,
        the frist for loop is for the strings in the list, the second for loop
        is for the letters in all strings.
        5 - after the code iterate in all strings, us compare all indexes in all
        strings, if the indexes match with the letter, i storage then in a string
        variable.
        """


        if not strs:
            return ""

        result = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return result
            result += char

        return result

        