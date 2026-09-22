# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        left_stack = []
        right_stack = []

        def push_left(node):
            while node:
                left_stack.append(node)
                node = node.left

        def push_right(node):
            while node:
                right_stack.append(node)
                node = node.right

        push_left(root)
        push_right(root)

        while left_stack and right_stack:

            left = left_stack[-1]
            right = right_stack[-1]

            if left == right:
                break

            total = left.val + right.val

            if total == k:
                return True

            if total < k:
                node = left_stack.pop()
                push_left(node.right)

            else:
                node = right_stack.pop()
                push_right(node.left)

        return False
        