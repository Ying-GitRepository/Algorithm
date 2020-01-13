# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def merge(self, one, two):
    """
    input: ListNode one, ListNode two
    return: ListNode
    """
    # write your solution here
    # 1. sanity check can be skipped for this code
    # 2. create add a dummy node to the input linkedlist
    new_head = ListNode(0)
    curr_node = new_head
    while one is not None and two is not None:
      if one.val <= two.val:
        curr_node.next = one
        one = one.next
      else:
        curr_node.next = two
        two = two.next
      curr_node = curr_node.next
    if(one is not None):
      curr_node.next = one
    elif(two is not None):
      curr_node.next = two
    return new_head.next
