# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        odd_head=head
        even_head=odd_head.next
        curr_odd=odd_head
        curr_even=even_head

        while curr_even and curr_even.next:
            curr_odd.next=curr_even.next
            curr_odd=curr_odd.next
            curr_even.next=curr_odd.next
            curr_even=curr_even.next


        curr_odd.next=even_head
        return odd_head
        