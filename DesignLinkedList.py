class Solution(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None   

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
          return -1

        fakeHead = Solution()
        fakeHead.next = self
        for c in range(index):
          fakeHead = fakeHead.next 
          if not fakeHead:
            return -1
        return fakeHead.next.val

    def getNode(self, index):
        """
        search by index
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: the node type
        """
        if index < 0:
          return -1

        fakeHead = Solution()
        fakeHead.next = self
        for c in range(index):
          fakeHead = fakeHead.next 
          if not fakeHead:
            return -1
        return fakeHead.next

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_head = Solution()
        new_head.val = val
        new_head.next = self       
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        lastNode = Solution()
        lastNode.val = val
        cur = self
        while cur.next:          
          cur = cur.next
        cur.next = lastNode 

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        fakeHead = Solution()
        fakeHead.next = self
        insertPoint = fakeHead.getNode(index)
        if insertPoint is not None:         
          newNode = Solution()
          newNode.val = val
          insertPoint.next, newNode.next = newNode, insertPoint.next       
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        fakeHead = Solution( )
        fakeHead.next = self
       
        delPoint = fakeHead.getNode(index)
        if delPoint is None:
          return self

        if delPoint.next is not None:
          delPoint.next = delPoint.next.next
        
# Your Solution object will be instantiated and called as such:
# obj = Solution()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
