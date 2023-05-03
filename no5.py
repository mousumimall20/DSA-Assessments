def find_duplicates(arr):
    freq = {}  # dictionary to keep track of the frequency of each element
    duplicates = []  # list to store the duplicates

    # Count the frequency of each element in the array
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate over the array and add the duplicates to the list
    for num in arr:
        if freq[num] > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates
