# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        
        result=[]

        def fun(node):
            if node is None:
                return
            
            fun(node.left)
            fun(node.right)
            result.append(node.val)
        
        fun(root)

        return result


        