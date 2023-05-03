class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum_nodes(head):
    # Create a hashmap to store the cumulative sum up to the current node
    cum_sum = {}
    cum_sum[0] = dummy = Node(0)
    dummy.next = head
    curr = head
    cum = 0
    # Traverse the linked list
    while curr:
        cum += curr.data
        # If the cumulative sum up to the current node is already present in the hashmap
        # Delete all nodes between the current node and the node with the same cumulative sum
        if cum in cum_sum:
            prev = cum_sum[cum]
            node = prev.next
            while node != curr:
                cum += node.data
                del cum_sum[cum]
                node = node.next
            prev.next = curr.next
        else:
            cum_sum[cum] = curr
        curr = curr.next
    return dummy.next
