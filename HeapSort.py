def heap_sort(arr, key=None):
    """
    Sorts the input list in ascending order using the heapsort algorithm.
    """
    if key is None:
        key = lambda x: x  # Default key function returns the element itself

    len_arr = len(arr)
    # Build a max heap
    for i in range(len_arr // 2 - 1, -1, -1):
        max_heapify(arr, len_arr, i, key)

    # Extract elements one by one
    for i in range(len_arr - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        max_heapify(arr, i, 0, key)

def max_heapify(arr, len_arr, i, key):
    largest = i
    l_child = 2 * i + 1
    r_child = 2 * i + 2

    if l_child < len_arr and key(arr[l_child]) > key(arr[largest]):
        largest = l_child

    if r_child < len_arr and key(arr[r_child]) > key(arr[largest]):
        largest = r_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, len_arr, largest, key)
