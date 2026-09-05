# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
         
        if left==right:
            return head

        dummy=ListNode(0)
        dummy.next = head 
        before=dummy

        for i in range(left-1):
            before = before.next

        tail=before.next

        previous=None
        current=tail

        for i in range(right - left + 1):

            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        # reconet

        before.next=previous
        tail.next=current

        return dummy.next



