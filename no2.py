class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k_group(head, k):
    # Reverse a linked list between two nodes
    def reverse_between(prev, next):
        curr = prev.next
        tail = curr
        while curr != next:
            temp = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = temp
        return tail

    # Create a dummy node and connect it to the head of the linked list
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    count = 0
    # Traverse the linked list in groups of size k
    while curr:
        count += 1
        if count % k == 0:
            prev = reverse_between(prev, curr.next)
            curr = prev.next
        else:
            curr = curr.next
    return dummy.next
