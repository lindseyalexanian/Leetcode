"""Let T be an undirected binary tree with nn vertices.  Create an algorithm to compute the diameter of T.

Clearly explain how your algorithm works, why it guarantees the correct output, and determine the running
time of your algorithm."""

import time

# start time (for running time calculations)
start = time.time()

### note that this is partially based on my solution to leetcode 543!
# The TreeNode class comes from that

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Graph_Stuff():
    """Graph stuff!"""

    def __init__(self, root: TreeNode) -> int:
        self.root = root

    def diameter_binary_tree(self):
        """This function returns the diameter of the binary tree"""

        # if there's no root, return 0
        if not self.root:
            return 0

        # let's make the root dynamic! aka I'm just using the list portion of the TreeNode object
        dynamic_root = [self.root]

        # initialize a dictionary for the heights
        height = {None: 0}

        # initialize a variable to hold the current max distance
        my_maximum = 0

        # while the dynamic root list exists/is being parsed
        while dynamic_root:

            # pop the first node
            node = dynamic_root.pop()


            # if there's no node left, continue
            if not node:
                continue

            # get the height of the left-most node
            left_height = height.get(node.left, None)

            # get the height of the right-most node
            right_height = height.get(node.right, None)

            # as long as there exists height for the node in question...
            if left_height == None or right_height == None:
                # add the node to the dynamic root list (as well as its child-nodes)
                dynamic_root.append(node)
                dynamic_root.append(node.left)
                dynamic_root.append(node.right)
                continue

            # the node height is the max of the left and right branches (plus one b/c of indexing)
            height[node] = max(left_height, right_height) + 1

            # update maximum if necessary
            my_maximum = max(left_height + right_height, my_maximum)

        return my_maximum


def main():
    """Main function! Compiles the rest"""
    # make the tree!
    # this is specific to binary tree T from the homework
    root = TreeNode(1)  # a
    root.left = TreeNode(2)  # b
    root.right = TreeNode(3)  # c
    root.left.left = TreeNode(4)  # d
    root.left.right = TreeNode(5)  # e
    root.right.left = TreeNode(6)  # f
    root.right.right = TreeNode(7)  # g
    root.right.left.left = TreeNode(8)  # h
    root.right.left.right = TreeNode(9)  # i
    root.right.right.left = TreeNode(10)  # j
    root.right.right.right = TreeNode(11)  # k
    root.right.left.left.left = TreeNode(12)  # l
    root.right.left.left.right = TreeNode(13)  # m
    root.right.right.left.left = TreeNode(14)  # n
    root.right.right.left.right = TreeNode(15)  # o
    root.right.right.right.right = TreeNode(16)  # p
    root.right.left.left.right.left = TreeNode(17)  # q

    # call function for diameter of binary tree, store in variable
    diameter_T = Graph_Stuff(root).diameter_binary_tree()

    print(f'The diameter of binary tree T is: {diameter_T}')

if __name__ == '__main__':
    # call main function
    main()


# algorithm time complexity is O(n) -- linear


### RUNNING TIME

# end time
end = time.time()

# running time
running_time = end - start
print(f"Running time: {running_time} sec")