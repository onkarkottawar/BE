import time
from concurrent.futures import ThreadPoolExecutor

# ============================
# Sequential Bubble Sort
# ============================
def bubble_sort_seq(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# ============================
# Parallel Bubble Sort
# ============================
def even_phase(arr, n):
    for j in range(0, n - 1, 2):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


def odd_phase(arr, n):
    for j in range(1, n - 1, 2):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_parallel(arr):
    n = len(arr)

    for i in range(n):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(even_phase, arr, n)
            executor.submit(odd_phase, arr, n)


# ============================
# Merge Function
# ============================
def merge(arr, l, m, r):

    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# ============================
# Sequential Merge Sort
# ============================
def merge_sort_seq(arr, l, r):

    if l < r:

        m = (l + r) // 2

        merge_sort_seq(arr, l, m)
        merge_sort_seq(arr, m + 1, r)

        merge(arr, l, m, r)


# ============================
# Parallel Merge Sort
# ============================
def merge_sort_parallel(arr, l, r, depth):

    if l < r:

        m = (l + r) // 2

        if depth <= 0:
            merge_sort_seq(arr, l, m)
            merge_sort_seq(arr, m + 1, r)

        else:
            with ThreadPoolExecutor(max_workers=2) as executor:

                executor.submit(
                    merge_sort_parallel,
                    arr,
                    l,
                    m,
                    depth - 1
                )

                executor.submit(
                    merge_sort_parallel,
                    arr,
                    m + 1,
                    r,
                    depth - 1
                )

        merge(arr, l, m, r)


# ============================
# Main
# ============================
def main():

    n = int(input("Enter number of elements: "))

    arr = []

    print("Enter elements one by one:")

    for i in range(n):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)

    # -------- Bubble Sort Sequential --------
    temp = arr.copy()

    start = time.time()

    bubble_sort_seq(temp)

    end = time.time()

    print("\nSequential Bubble Sort:")
    print("Sorted Array:", temp)
    print("Execution Time:", end - start, "sec")

    # -------- Bubble Sort Parallel --------
    temp = arr.copy()

    start = time.time()

    bubble_sort_parallel(temp)

    end = time.time()

    print("\nParallel Bubble Sort:")
    print("Sorted Array:", temp)
    print("Execution Time:", end - start, "sec")

    # -------- Merge Sort Sequential --------
    temp = arr.copy()

    start = time.time()

    merge_sort_seq(temp, 0, n - 1)

    end = time.time()

    print("\nSequential Merge Sort:")
    print("Sorted Array:", temp)
    print("Execution Time:", end - start, "sec")

    # -------- Merge Sort Parallel --------
    temp = arr.copy()

    start = time.time()

    merge_sort_parallel(temp, 0, n - 1, 4)

    end = time.time()

    print("\nParallel Merge Sort:")
    print("Sorted Array:", temp)
    print("Execution Time:", end - start, "sec")


if __name__ == "__main__":
    main()
