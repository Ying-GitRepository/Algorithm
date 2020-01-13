# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def reverse(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # write your solution here
    if not head:
      return None
    # traverse the linked list,until the last listNode,  
    # ListNode.next listNode to its previous listNode, 
    # move to the next listNode
    cur = head
    pre = None
    nex = head

    while cur:
      nex = cur.next
      cur.next = pre
      pre = cur
      cur = nex
 
    return pre
