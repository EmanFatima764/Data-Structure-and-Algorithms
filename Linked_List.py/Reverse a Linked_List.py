# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__ (self,val=0 , next=None):
        self.val=val
        self.next=next
class Solution:
    def reverseList(self, head:[ListNode]) -> [ListNode]:
        temp=head
        stack=[]
        if head is None or head.next is None:  # Base case
            return head
        # Recursive call
        while temp is not None:
            stack.append(temp.val)
            temp=temp.val
        temp=head 
        while temp is not None:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return head

if __name__ =="__main__":
    sol=Solution()
    head = [1,2,3,4,5]
    print(sol.reverseList(head))

        