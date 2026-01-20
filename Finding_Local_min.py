# Array to search
a = [5, 6, 7, 8, 9, 10, 4, 1, 2, 3]

def find_local_min(arr):
    """
    Finds a local minimum in the array.
    A local minimum is an element smaller than its neighbors.
    Returns the index of the local minimum.
    """
    n = len(arr)
    
    # Edge cases: first or last element
    if n == 0:
        return None
    if n == 1 or arr[0] < arr[1]:
        return 0
    if arr[-1] < arr[-2]:
        return n - 1
    
    # Binary search for local minimum
    low = 1
    high = n - 2  # avoid first and last elements
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid is local minimum
        if arr[mid - 1] > arr[mid] < arr[mid + 1]:
            return mid
        # If left neighbor is smaller, local min is on the left
        elif arr[mid - 1] < arr[mid]:
            high = mid - 1
        # If right neighbor is smaller, local min is on the right
        else:
            low = mid + 1
    
    return None  # If no local minimum found

# Find and print local minimum
index = find_local_min(a)
if index is not None:
    print("Local minimum found at index", index, "with value", a[index])
else:
    print("No local minimum found")
