import random
import time
from concurrent.futures import ThreadPoolExecutor

SIZE = 10000

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

    for _ in range(n):

        # Even phase
        with ThreadPoolExecutor() as executor:
            executor.submit(compare_and_swap, 0).result()

        # Odd phase
        with ThreadPoolExecutor() as executor:
            executor.submit(compare_and_swap, 1).result()


# ============================
# Generate Random Array
# ============================
def generate_random(size):
    return [random.randint(0, 100000) for _ in range(size)]


# ============================
# Main Function
# ============================
def main():

    arr = generate_random(SIZE)

    # -------- Sequential Bubble Sort --------
    temp = arr.copy()

    start = time.time()
    bubble_sort_seq(temp)
    end = time.time()

    print(f"Sequential Bubble Sort Time: {end - start:.6f} sec")

    # -------- Parallel Bubble Sort --------
    temp = arr.copy()

    start = time.time()
    bubble_sort_parallel(temp)
    end = time.time()

    print(f"Parallel Bubble Sort Time: {end - start:.6f} sec")


if __name__ == "__main__":
    main()