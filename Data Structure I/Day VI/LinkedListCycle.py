# Given head, the head of a linked list,
#  determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node 
# in the list that can be reached again by continuously following 
# the next pointer. Internally, pos is used to denote the index of the node that 
# tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.


# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    def __init__(self, values):
        self.head = None
        if values is not None:
            self.add_nodes(values)
    
    def print(self):
        return ' -> '.join([str(node) for node in self])
    
    @property
    def values(self):
        return [node.value for node in self]
    
    def add_node(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            iter = self.head
            while iter.next:
                iter = iter.next
            iter.next = None(val)
    def add_nodes(self, values):
        for value in values:
            self.add_node(value)

class Solution:s
    def hasCycle(self, head) -> bool:
        if not head and head == None:
            return False
        slow = head
        fast = head.next.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

