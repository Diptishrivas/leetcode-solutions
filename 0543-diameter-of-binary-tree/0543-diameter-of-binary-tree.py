# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        diameter = [0]

        def solve(node):
            if node is None:
                return 0

            left_depth = solve(node.left)
            right_depth = solve(node.right)

            diameter[0] = max(diameter[0], left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        solve(root)

        return diameter[0]