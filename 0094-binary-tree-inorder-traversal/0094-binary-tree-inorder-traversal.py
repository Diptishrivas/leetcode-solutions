# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        
        result=[]

        def fun(node):
            if node is None:
                return
        
            fun(node.left)
            result.append(node.val)
            fun(node.right)

        fun(root)

        return result




        