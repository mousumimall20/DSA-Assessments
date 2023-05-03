def count_pairs(arr, target):
    freq = {}  # dictionary to keep track of the frequencies of elements in the array
    count = 0  # variable to keep track of the number of pairs with the given sum

    # Count the frequency of each element in the array
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate over the array and check if there exists a pair with the given sum
    for num in arr:
        if target - num in freq:
            count += freq[target - num]
            # If target - num == num, decrement the count to avoid counting the same pair twice
            if target - num == num:
                count -= 1

    # Divide the count by 2 to avoid counting the same pair twice (i.e., (a, b) and (b, a))
    return count // 2
