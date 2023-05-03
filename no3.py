class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_alternate(head1, head2):
    # Traverse the first linked list and keep a pointer to the next node to be merged
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        next1 = curr1.next
        # Insert the next node to be merged from the first linked list after the current node in the second linked list
        curr1.next = curr2.next
        curr2.next = curr1
        curr1 = next1
        curr2 = curr2.next.next
    return head2
