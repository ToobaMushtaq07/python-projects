import numpy as np

sales = np.array([1200, 1500, 1800, 1700, 2000, 2100, 1900, 2200])

print("Original Array:")
print(sales)

# Indexing
print("\nSecond Element:", sales[1])
print("Last Element:", sales[-1])

# Slicing
print("\nFirst 5 Elements:", sales[:5])
print("Index 2 to 6:", sales[2:7])

# Basic Statistics
print("\nStatistics")
print("Sum =", np.sum(sales))
print("Mean =", np.mean(sales))
print("Maximum =", np.max(sales))
print("Minimum =", np.min(sales))