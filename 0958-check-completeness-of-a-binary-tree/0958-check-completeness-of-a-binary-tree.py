# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        if root is None:
            return True

        q = deque([root])
        seen_none = False

        while q:
            node = q.popleft()

            if node is None:
                seen_none = True
                continue

            if seen_none:
                return False

            q.append(node.left)
            q.append(node.right)

        return True
        