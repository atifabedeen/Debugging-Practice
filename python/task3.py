"""
This task is about reversing a doubly linked list.
This operation should correctly handle both the prev and next pointers.
Example:
1 <-> 2 <-> 3
Result: 3 <-> 2 <-> 1
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def reverse_doubly_linked_list(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = reverse_doubly_linked_list(head)
    print(head.value == 5) #True
    print(head.prev is None) #True
    print(head.next.value == 4) #True
    print(head.next.prev.value == 5) #True

