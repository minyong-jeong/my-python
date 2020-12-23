def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

if __name__ == "__main__":
    import time
    import random
    total_elements = 1000
    arr = random.sample(range(-50000, 50000), total_elements)

    start = time.time()
    sorted_arr = bubble_sort(arr)
    end = time.time()

    print("Total elements:", total_elements)
    print("Success?", sorted_arr == sorted(arr))
    print("Working time: %.2f sec" % (end-start))
