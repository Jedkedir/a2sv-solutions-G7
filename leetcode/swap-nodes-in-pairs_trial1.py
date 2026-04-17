# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next:  return head
        prev,curr = head,head
        while curr and curr.next:
            curr = curr.next
            temp = curr.next
            curr.next = prev
            prev.next = temp
            curr,prev = temp,temp
        return head



