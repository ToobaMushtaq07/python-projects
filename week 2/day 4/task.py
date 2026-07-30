import pandas as pd

# First dataset
data1 = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Ahmed"]
}

# Second dataset
data2 = {
    "ID": [1, 2, 3],
    "Marks": [85, 90, 78]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge the datasets
merged_data = pd.merge(df1, df2, on="ID")

# Display merged dataset
print("Merged Dataset:")
print(merged_data)

# Produce summary
print("\nSummary:")
print("Total Students:", len(merged_data))
print("Average Marks:", merged_data["Marks"].mean())
print("Highest Marks:", merged_data["Marks"].max())
print("Lowest Marks:", merged_data["Marks"].min())