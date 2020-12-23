def insertion_sort(arr):
    length = len(arr)
    for i in range(length):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    import time
    import random
    total_elements = 1000
    arr = random.sample(range(-50000, 50000), total_elements)

    start = time.time()
    sorted_arr = insertion_sort(arr)
    end = time.time()

    print("Total elements:", total_elements)
    print("Success?", sorted_arr == sorted(arr))
    print("Working time: %.2f sec" % (end-start))
