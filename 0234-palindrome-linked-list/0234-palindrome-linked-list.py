# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        newnode = self.reverse(slow)

        first = head
        second = newnode

        while second is not None:

            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
 
    def reverse(self, head):

        previous = None
        current = head

        while current is not None:

            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        return previous