# Vector Addition using Python

n = 1024

# Initialize vectors
A = []
B = []
C = []

for i in range(n):
    A.append(i)
    B.append(i * 2)

# Vector Addition
for i in range(n):
    C.append(A[i] + B[i])

# Print first 10 results
print("First 10 Results:")

for i in range(10):
    print(f"{A[i]} + {B[i]} = {C[i]}")