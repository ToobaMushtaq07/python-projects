import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Print the  array
print("Original Array:")
print(numbers)

# Indexing
print("\nFirst Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("\nFirst 4 Elements:", numbers[:4])
print("Last 3 Elements:", numbers[-3:])
print("Elements from Index 2 to 5:", numbers[2:6])

# Basic Statistics (without loops)
print("\nStatistics")
print("Sum =", np.sum(numbers))
print("Mean =", np.mean(numbers))
print("Maximum =", np.max(numbers))
print("Minimum =", np.min(numbers))
print("Standard Deviation =", np.std(numbers))