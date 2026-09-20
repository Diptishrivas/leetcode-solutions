# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        
        def solve(node):
            if node is None:
                return (None,0)
            left_node,left_depth=solve(node.left)
            right_node,right_depth=solve(node.right)

            if left_depth>right_depth:
                return (left_node,left_depth+1)
            if right_depth>left_depth:
                return(right_node,right_depth+1)

            return (node,left_depth+1)
        ans,depth=solve(root)

        return ans



        
        