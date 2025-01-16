# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast =fast.next.next
        return slow

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        tail = head.next
        while tail:
            i += 1
            tail = tail.next
        j = 1
        while head:
            if j == int(i / 2) + 1:
                return head
            head = head.next
            j += 1
