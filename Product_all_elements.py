def replace_with_product(arr):
    total_product = 1
    zero_count = 0
    
    # Count zeros and calculate product of non-zero elements
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num

    for i in range(len(arr)):
        if zero_count > 1:
            # More than one zero → all results are zero
            arr[i] = 0
        elif zero_count == 1:
            # Only one zero → only that position gets product
            arr[i] = total_product if arr[i] == 0 else 0
        else:
            # No zero → normal division
            arr[i] = total_product // arr[i]


# Example
a = [1, 2, 0, 4]
print("Before:", a)
replace_with_product(a)
print("After: ", a)

# Before: [1, 2, 3, 4]
# After:  [24, 12, 8, 6]
