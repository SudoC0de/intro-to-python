def delete_duplicates(arr):
    # 'write_index' points to where the next unique element should be written.
    write_index = 1

    # Iterate over the list's length, starting from the second element because
    # the first element doesn't have a previous element to compare against.
    for index in range(1, len(arr)):
        # Compare the current element with its immediate previous element.
        if arr[index] != arr[index - 1]:
            # If they're different, it's not a duplicate.
            # Place the current element at the 'write_index' position.
            arr[write_index] = arr[index]
            # Then increment 'write_index' by 1 to prepare for the next unique element.
            write_index += 1

    # Once you have shifted all unique elements to the left,
    # fill the remaining positions in the list with zeroes.
    for i in range(write_index, len(arr)):
        arr[i] = 0

    # Return the modified list for visualization and the count of unique elements.
    return arr


input_list = [1, 2, 2, 3, 4, 4, 4, 5]
print(delete_duplicates(input_list))
