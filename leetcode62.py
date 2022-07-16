"""Leetcode 62

There is a robot on an m x n grid. The robot is initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109."""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Counts the number of unique paths across a 2D matrix"""

        # initialize a m*n matrix
        my_paths = list(n*[0] for _ in range(m))

        # view empty matrix (as a matrix, print by row)
        for item in my_paths:
            print(item)

        # write variables for rows and columns range
        rows = range(m)
        columns = range(n)

        # loop through the rows
        for i in rows:
            # add one to first column (first item in each row)
            my_paths[i][0] = 1

        # loo[ through columns next
        for j in columns:
            # add one to first item in each column (the whole first row)
            my_paths[0][j] = 1

        # now loop through the entire matrix, rows and columns, except for the first row & col
        for a in range(1, m):

            for b in range(1, n):

                # add, if there is a valid path
                # we add the number whenever a path is crossed, number at final cell is the answer
                my_paths[a][b] = my_paths[a - 1][b] + my_paths[a][b - 1]

                # check as you go!
                for item in my_paths:
                    print(item)

        # return the answer, which is in the last cell of the matrix
        return my_paths[-1][-1]

x = 3
y = 7

answer = Solution().uniquePaths(x,y)
print(answer)

# the print statements increase the run time considerably, so I commented them out when I ran it on leetcode, but \
# I find them helpful when checking my work