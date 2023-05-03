def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Move the left pointer to the right until we find a positive element
        while left <= right and arr[left] < 0:
            left += 1

        # Move the right pointer to the left until we find a negative element
        while left <= right and arr[right] >= 0:
            right -= 1

        # If we have not crossed the pointers, swap the elements
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr
