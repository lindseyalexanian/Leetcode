"""Leetcode 85"""


from typing import List
import pandas as pd


class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    """
    This function accepts a matrix and returns the area of the largest
    rectangle that can be made from the values contained in the matrix."

    :type matrix: List[List[str]]
    :rtype: int
    """

    # ensure that the input matches the input requirements
    try:

      # initialize a variable to contain largest rect area
      largest_rectangle_area = 0

      # convert the matrix to a df using pandas library
      my_matrix = pd.DataFrame(matrix)
      print(my_matrix)


      # find the number of columns in the df
      col_count = len(my_matrix.columns)

      # initialize height sum
      height_sum = [0 for _ in range(col_count)]

      # initialize a matrix w/ one row, containing all 0s
      empty_mat = [0 for _ in range(col_count)]

      # initialize a matrix w/ one row, containing all
      full_mat = [col_count for _ in range(col_count)]

      # loop through the whole matrix (the number of rows first)
      for i in range(len(matrix)):

        # initialize min possible count of ones
        min_count = 0

        # loop through the columns in each row, left to right
        for item in range(col_count):
          # check if this df cell contains a 1
          if my_matrix.iloc[i][item] == "1":

            # set the initialized matrix row to the max between min count and current item in new matrix
            empty_mat[item] = max(empty_mat[item], min_count)

            # add one to height
            height_sum[item] += 1

          else:
            # otherwise, set all to zero and reset column count
            full_mat[item] = col_count
            height_sum[item] = 0
            empty_mat[item] = 0

            # update the minimum count to 1 more
            min_count = item + 1

        # set the maximum count to the number of columns
        max_count = col_count

        # now go from the right, backward through the columns across row
        for item in reversed(range(col_count)):

          # if cell contains "1"
          if my_matrix.iloc[i][item] == "1":
            # get minimum
            full_mat[item] = min(full_mat[item], max_count)

            # find the current height for these circumstances
            current_height = height_sum[item]*(full_mat[item]-empty_mat[item])
            #print(current_height)

            # compare the current area to the largest stored area \
            # we drop the lower one, no need to store it anymore
            largest_rectangle_area = max(largest_rectangle_area, current_height)

          else:
            # otherwise, set to index
            max_count = item

      return largest_rectangle_area

    except TypeError:
      return 0



input = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
input2 = [["1"]]
input3 = 5

answer = Solution().maximalRectangle(input)
print(f"Answer is {answer}")

# explanation!
# we need to find the area of the largest rectangle up to each row
# once that is done, we find which row(s) contained the largest rectangle
# that largest rectangle is the largest rectangle in the matrix
# this works b/c every possible combination is considered by just looking at the rows
# time complexity is O(n^2), or O(length * width) of the matrix