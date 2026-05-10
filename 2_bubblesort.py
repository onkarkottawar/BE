import random
import time
from concurrent.futures import ThreadPoolExecutor

SIZE = 20   # keep small for printing


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
def bubble_sort_parallel(arr):
    n = len(arr)

    def compare_and_swap(start):
        for j in range(start, n - 1, 2):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Create thread pool only once
    with ThreadPoolExecutor(max_workers=2) as executor:

        for _ in range(n):

            # Even phase
            future1 = executor.submit(compare_and_swap, 0)

            # Odd phase
            future2 = executor.submit(compare_and_swap, 1)

            future1.result()
            future2.result()


# ============================
# Generate Random Array
# ============================
def generate_random(size):
    return [random.randint(0, 100) for _ in range(size)]


# ============================
# Main Function
# ============================
def main():

    arr = generate_random(SIZE)

    # Print Original Array
    print("Original Array:")
    print(arr)

    # -------- Sequential Bubble Sort --------
    temp1 = arr.copy()

    start = time.time()
    bubble_sort_seq(temp1)
    end = time.time()

    print("\nSequential Sorted Array:")
    print(temp1)

    print(f"Sequential Bubble Sort Time: {end - start:.6f} sec")

    # -------- Parallel Bubble Sort --------
    temp2 = arr.copy()

    start = time.time()
    bubble_sort_parallel(temp2)
    end = time.time()

    print("\nParallel Sorted Array:")
    print(temp2)

    print(f"Parallel Bubble Sort Time: {end - start:.6f} sec")


if __name__ == "__main__":
    main()
