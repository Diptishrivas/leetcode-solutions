# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
       
        curr = head
        count = 0

        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        prev = None
        curr = head

        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)

        return prev
