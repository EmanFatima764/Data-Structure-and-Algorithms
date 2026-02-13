# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__ (self,val=0 , next=None):
        self.val=val
        self.next=nexta
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # Base case
            return head
        # Recursive call
        new_head=self.reverseList(head.next) 
        # give address of node to currentnode  
        head.next.next=head
        # give None to current.next to stop cycle
        head.next=None
        
        return new_head
if __name__ =="__main__":
    sol=Solution()
    head = [1,2,3,4,5]
    print(sol.reverseList(head))

        