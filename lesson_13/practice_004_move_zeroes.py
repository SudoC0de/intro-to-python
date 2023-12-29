# Given an array of integers, write a function to move all 0's
# to the end while maintaining the relative order of the other elements.
# Input: 0 4 0 3 12
# Output: 4 3 12 0 0

def move_zeros(arr):
    # Your code here
    count = 0

    for num in arr:
        count += 1

        if count == len(arr):
            break

        if num == 0:
            arr.remove(0)
            arr.append(0)

    return arr

custom_array = [4,0,3,0,12]
print(f"Array: {custom_array}")
print(f"Move Zeros Array: {move_zeros(custom_array)}")
