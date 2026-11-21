import numpy as np


#2(a)
total_a1 = 0
for i in range(1,5):
    total_a1 += (2*i-1)
print(total_a1)

print(sum(2*i-1 for i in range(1,5)))

i = np.arange(1,5)
print(np.sum(2*i-1))

# ---------- 2(b): prod_{k=1}^{3} (k + 1) ----------
total_b = 1                    # why 1 and not 0? (think: what's x * 0?)
for k in range(1,4):
    total_b *= k + 1


numpy_b = np.prod(np.arange(1, 4) + 1)
print("2(b):", total_b, numpy_b)

# ---------- 2(c): sum_{j=1}^{3} a_{2j} x_j ----------
A = np.array([[1, 2, 0], [3, -1, 4]])
x = np.array([2, 1, 1])
total_c = 0
for j in range(3):
    total_c += A[1,j] * x[j]
numpy_c = A[1] @ x             # row 2 of the book = A[1]; @ = multiply-and-sum
print("2(c):", total_c, numpy_c)