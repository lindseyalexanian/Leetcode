"""Leetcode 53: Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""

from typing import List

# note that I have some commented out print statements - I use them to check my work

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """This method finds and returns the maximum sum of an subarray within the input array.
        This implements dynamic programming through the use of Kadane's algorithm."""

        # initialize an array that will contain the max at each index
        max_sum_array = len(nums) * [0]

        # find the base case (abides by loop invariant trivially, b/c it's the first element)
        max_sum_array[0] = nums[0]

        # initialize a sum finder variable \
        # this keeps track of the current max sum at each index as we parse the array
        sum_finder = nums[0]

        # get length of the input array
        length_input = len(nums)

        # loop through the input array
        for i in range(1, length_input):

            # compare previous sum plus new number w/ new number on its own
            max_sum_array[i] = max(max_sum_array[i-1] + nums[i], nums[i])

            # if the current sum max is less than the max in the array
            if sum_finder < max_sum_array[i]:
                #print(sum_finder)

                # update max sum variable
                sum_finder = max_sum_array[i]

                #print(f"max sum is now: {sum_finder}")

            #print(max_sum_array)

        return sum_finder




# test cases
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5,4,-1,7,8]

# call class and method
answer = Solution().maxSubArray(nums3)
print(f"Answer: {answer}")