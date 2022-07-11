# below was my exact leetcode submission that ran in the shortest amount of time \
# and did not include the extra parameters and notes from the previous file



from typing import List
import numpy as np
import sys


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # define variables for the length of nums1 and nums2
        length_1 = len(nums1)
        length_2 = len(nums2)

        # flip variables if nums1 is longer
        if length_1 > length_2:
            nums1, nums2 = nums2, nums1
            # MUST flip lengths too
            length_1, length_2 = length_2, length_1

        # prepare left and right indices for binary split
        left_side = 0
        right_side = length_1

        while left_side <= right_side:
            # break into 2 partitions (for a binary split)
            # left breaks off @ midpoint
            part1 = (right_side + left_side) // 2
            # print(part1)
            # right is midpoint +1 to the end
            part2 = (1 + length_1 + length_2) // 2 - part1

            # set left max 1
            if part1 == 0:
                lmax1 = -sys.maxsize
            else:
                lmax1 = nums1[part1 - 1]

            # set left max 2
            if part2 == 0:
                lmax2 = -sys.maxsize
            else:
                lmax2 = nums2[part2 - 1]

            if part1 == length_1:
                rmin1 = sys.maxsize
            else:
                # print(part1)
                # print(nums1[part1])
                rmin1 = nums1[part1]

            if part2 == length_2:
                rmin2 = sys.maxsize
            else:
                rmin2 = nums2[part2]

            # find median now!
            if lmax1 <= rmin2 and lmax2 <= rmin1:
                # if length is even
                if (length_1 + length_2) % 2 == 0:
                    med_ans = (max(lmax1, lmax2) + min(rmin1, rmin2)) / 2
                    return med_ans
                # if length is odd
                else:
                    # get max of just left partition
                    med_ans = max(lmax1, lmax2)
                    return med_ans


            # if skewed left!
            elif lmax1 > rmin2:
                right_side = part1 - 1

            # if skewed right!
            else:
                left_side = part1 + 1

# my test cases!
x = [1, 3, 5]
y = [2, 7, 10]

a = [0, 0, 0, 0, 0]
b = [-1, 0, 0, 0, 0, 0, 1]

c = [1, 2]
d = [3, 4]

# class instance
z = Solution()

# find median
answer = z.findMedianSortedArrays(x, y)
print(answer)