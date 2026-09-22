import numpy as np

# 1. Create arrays
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.arange(12)   # array from 0 to 11
arr3 = np.linspace(0, 1, 5)  # 5 evenly spaced values between 0 and 1

print("Original arr1:", arr1)
print("Original arr2:", arr2)
print("Original arr3:", arr3)

# 2. Reshape arrays
reshaped1 = arr1.reshape(2, 3)   # 2 rows, 3 columns
reshaped2 = arr2.reshape(3, 4)   # 3 rows, 4 columns

print("\nReshaped arr1 (2x3):\n", reshaped1)
print("Reshaped arr2 (3x4):\n", reshaped2)

# 3. Flatten arrays
flat = reshaped1.flatten()
print("\nFlattened arr1:", flat)

# 4. Transpose arrays
transposed = reshaped2.T
print("\nTransposed arr2:\n", transposed)

# 5. Stacking arrays
stacked_v = np.vstack([arr1, arr1])   # vertical stack
stacked_h = np.hstack([arr1, arr1])   # horizontal stack

print("\nVertical stack:\n", stacked_v)
print("Horizontal stack:\n", stacked_h)

# 6. Splitting arrays
split_arr = np.split(arr2, 3)   # split into 3 equal parts
print("\nSplit arr2 into 3 parts:", split_arr)

# 7. Basic manipulations
added = arr1 + 10
multiplied = arr1 * 2
squared = arr1 ** 2

print("\nAdded 10:", added)
print("Multiplied by 2:", multiplied)
print("Squared:", squared)

# 8. Aggregate functions
print("\nSum:", arr1.sum())
print("Mean:", arr1.mean())
print("Max:", arr1.max())
print("Min:", arr1.min())

# 9. Boolean indexing
mask = arr1 > 3
print("\nMask (arr1 > 3):", mask)
print("Filtered values:", arr1[mask])

# 10. Advanced reshape with -1
auto_reshape = arr2.reshape(-1, 6)   # NumPy figures out rows automatically
print("\nAuto reshape (-1,6):\n", auto_reshape)
