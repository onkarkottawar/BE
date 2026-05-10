# Matrix Multiplication using Python

N = 4

# Initialize matrices
A = [[0 for _ in range(N)] for _ in range(N)]
B = [[0 for _ in range(N)] for _ in range(N)]
C = [[0 for _ in range(N)] for _ in range(N)]

# Fill matrices
for i in range(N):
    for j in range(N):
        A[i][j] = i + j
        B[i][j] = i * j

# Matrix Multiplication
for i in range(N):
    for j in range(N):
        sum = 0
        for k in range(N):
            sum += A[i][k] * B[k][j]

        C[i][j] = sum

# Print matrices
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nResult Matrix C:")
for row in C:
    print(row)