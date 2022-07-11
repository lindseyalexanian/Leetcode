"""My solution to leetcode #1584"""

import math

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # initialize the output variable
        output = 0

        # initialize a counter for the current vertex
        counter = 0

        # initialize an array to contain the distances
        distance_array = []

        # loop through all of the points
        for i in range(len(points)):

            # find the manhattan distance between each of the pairs of points (in order)
            two_point_dist = manhattan_distance(points[0], points[i])
            print(two_point_dist)

            # append to the distance array
            distance_array.append(two_point_dist)

        # initialize a list of passed nodes (set to false)
        passed_nodes = len(points)*[False]
        print(distance_array)
        # set first item in this list to true, b/c we just visited it
        passed_nodes[0] = True

        # loop through rest of points
        for _ in range(len(points) - 1):

            # initialize minimum weight as infinity
            weight_minimum = math.inf

            # loop
            for i in range(len(points)):
                print(f"dist array {distance_array[i]}")
                # if the min weight is greater than the current dist array and we haven't passed the node yet
                if weight_minimum > distance_array[i] and passed_nodes[i] == False:
                    # add min weight to the distance array
                    weight_minimum = distance_array[i]
                    print(f"weight min {weight_minimum}")

                    # update counter
                    counter = i

            # update the output to include the minimum weight
            output += weight_minimum

            # mark off node as passed
            passed_nodes[counter] = True

            # find distance for any points we haven't passed yet
            for i in range(len(points)):
                if passed_nodes[i] == False:
                    # minimum between current val and the manhattan dist
                    distance_array[i] = min(distance_array[i], manhattan_distance(points[counter], points[i]))

        return output


def manhattan_distance(x, y):
    """This function returns the manhattan dist. between 2 points"""
    # solve for the absolute dist. between the two points (just slope - rise over run)
    absolute_distance = abs(x[0] - y[0]) + abs(x[1] - y[1])

    # return the answer
    return absolute_distance

my_points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
solved = Solution().minCostConnectPoints(my_points)
print(f"The minimum weight is {solved}")


