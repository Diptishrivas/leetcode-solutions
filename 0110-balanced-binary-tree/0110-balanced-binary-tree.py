# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def solve(node):
            if node is None:
                return 0
        
            left_depth=solve(node.left)
            right_depth=solve(node.right)

            if left_depth==-1 or right_depth==-1:
                return -1
 
        
            if abs(left_depth-right_depth)>1:
                return -1

            return max(left_depth,right_depth)+1
        
        return solve(root) != -1
        