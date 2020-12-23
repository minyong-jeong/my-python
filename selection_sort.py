def selection_sort(arr):
    length = len(arr)
    for i in range(length-1):
        min_idx = i
        for j in range(i+1, length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    import time
    import random
    total_elements = 1000
    arr = random.sample(range(-50000, 50000), total_elements)

    start = time.time()
    sorted_arr = selection_sort(arr)
    end = time.time()

    print("Total elements:", total_elements)
    print("Success?", sorted_arr == sorted(arr))
    print("Working time: %.2f sec" % (end-start))
