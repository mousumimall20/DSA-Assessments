import heapq

def kth_largest_smallest(arr, k):
    # Create a max-heap with the first K elements of the array
    max_heap = [-num for num in arr[:k]]
    heapq.heapify(max_heap)

    # Create a min-heap with the first K elements of the array
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    # Iterate over the remaining elements in the array
    for num in arr[k:]:
        # If the element is greater than the root of the max-heap, push it into the max-heap
        if -num > max_heap[0]:
            heapq.heappushpop(max_heap, -num)
        # If the element is smaller than the root of the min-heap, push it into the min-heap
        if num < min_heap[0]:
            heapq.heappushpop(min_heap, num)

    # The root of the max-heap is the Kth largest element
    kth_largest = -max_heap[0]

   
