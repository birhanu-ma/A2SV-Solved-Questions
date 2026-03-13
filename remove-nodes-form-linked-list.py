# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        prev = None
        curr = head 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
       
        temp.append(prev.val)
        prev_list = prev
        while prev_list and prev_list.next:
            if prev_list.next.val >= temp[-1]:
                temp.append(prev_list.next.val)
                prev_list = prev_list.next
            else:
                prev_list.next = prev_list.next.next

        prev_temp = None
        curr = prev 
        while curr:
            next_node = curr.next
            curr.next = prev_temp
            prev_temp = curr
            curr = next_node
        return prev_temp
       
       

            

            

        

        
