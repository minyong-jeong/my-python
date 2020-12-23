def heapify(arr, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

def heap_sort(arr):
    length = len(arr)

    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, i, length)

    for i in range(length - 1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

if __name__ == "__main__":
    import time
    import random
    total_elements = 7
    arr = random.sample(range(0, 10), total_elements)

    start = time.time()
    sorted_arr = heap_sort(arr)
    end = time.time()

    print("Total elements:", total_elements)
    print("Success?", sorted_arr == sorted(arr))
    print("Working time: %.2f sec" % (end-start))
