"""Leetcode 131

"""


from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        :type s: str
        :rtype: List[List[str]]
        """

        # initialize list for palindrome possibilities
        pal_sets = []

        count = []

        # call the dfs function, which finds these arrangements
        self.dfs(s, pal_sets, count)

        # return the palindromes
        return pal_sets


    def palindrome(self, s: str):
        """This function checks if a particular a particular
        string is a palindrome and returns a boolean"""

        # get palindrome boolean
        pal_bool = (s == s[::-1])

        return pal_bool

    def dfs(self, s, answers, initialized_list):
        """This function runs a depth first search to check for palindromes and make the arragnements
        if a palindrome is possible"""

        # must account for if the input is an empty string
        if not s:
            # append the empty list to the answers
            answers.append(initialized_list)

            # return the empty string, as this is the only possibility if input is empty
            return [[""]]

        # now, loop through the entire string
        for i in range(1, len(s) + 1):

            # only consider if could be a palindrome
            if self.palindrome(s[:i]) == True:

                # call function, add to list of answers
                self.dfs(s[i:], answers, initialized_list + [s[:i]])


        print(initialized_list)


# test it!
input = "aab"
input2 = "pippa"
input3 = ""
answer = Solution().partition(input)
print(answer)


