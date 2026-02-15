# Definition for singly-linked list.
from typing import List,Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hare-Torotise Approach
        slow=head
        fast=head
        while  fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
if __name__ =="__main__":
    sol=Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    middle=sol.middleNode(head)
    print(f"The middle node value is  {middle.val}")



        