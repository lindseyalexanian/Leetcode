"""Leetcode 22

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List

class Solution:

    def catalan(self, n):
        """find the catalan number for n"""
        # initialize catalan variables, let it start w/ 1
        cat_var = [1]

        # placeholder variable for the first number
        placeholder = 1

        # loop through all parentheses in n
        for i in range(1, n + 1):
            # use catalan formula
            placeholder *= (4 * i - 2) / (i + 1)
            # append to the list of catalan number results
            cat_var.append(int(placeholder))

        return cat_var

    def generateParenthesis(self, n: int) -> List[str]:
        """generate the combinations"""

        # initialize a list of strings to contains the results
        my_array = [['']]


        # loop from one to n + 1 (so as to include n)
        for i in range(1, n + 1):
            parentheses = []

            # only add items that fit the requirements of legal parentheses
            for item in range(i):
                parentheses.extend(["("+x+")" + y for x in my_array[item] for y in my_array[i-1-item]])

            # add new parentheses to the result array
            my_array.append(parentheses)

        # call the catalan function
        check_nums = self.catalan(n)

        # if catalan number is same as number of results (check work)
        if check_nums[n] == len(my_array[n]):

            return my_array[n]

# test it!
test_it = 3
answer = Solution().generateParenthesis(test_it)
print(answer)



