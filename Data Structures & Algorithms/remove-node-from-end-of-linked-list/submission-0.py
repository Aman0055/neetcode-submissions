# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      current_node = ListNode(0, head)
      last_node = current_node
      target = current_node

      for _ in range(n):
        last_node = last_node.next

      while last_node.next:
        last_node = last_node.next
        target = target.next

      target.next = target.next.next

      return current_node.next

