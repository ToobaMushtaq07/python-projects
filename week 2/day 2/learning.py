#students marks
import numpy as np

# Create a NumPy array
marks = np.array([78, 85, 92, 67, 88, 95, 73, 81])

print("Original Array:")
print(marks)

# Indexing
print("\nFirst Element:", marks[0])
print("Last Element:", marks[-1])

# Slicing
print("\nFirst 4 Elements:", marks[:4])
print("Last 3 Elements:", marks[-3:])

# Basic Statistics
print("\nStatistics")
print("Sum =", np.sum(marks))
print("Mean =", np.mean(marks))
print("Maximum =", np.max(marks))
print("Minimum =", np.min(marks))
print("Standard Deviation =", np.std(marks))


#monthly sales
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