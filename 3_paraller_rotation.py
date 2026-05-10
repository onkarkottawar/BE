# Parallel Min, Max, Sum, Average using Python

from multiprocessing import Pool


# Find Minimum
def minimum(arr):
    return min(arr)


# Find Maximum
def maximum(arr):
    return max(arr)


# Find Sum
def summation(arr):
    return sum(arr)


# Find Average
def average(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5]

    print("Array:", arr)

    print("Minimum value is:", minimum(arr))
    print("Maximum value is:", maximum(arr))
    print("Summation is:", summation(arr))
    print("Average is:", average(arr))