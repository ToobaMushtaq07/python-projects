import pandas as pd
# Load the dataset
df = pd.read_csv("students.csv")
print(df.columns)
print(df)

# Display the original dataset
print("Original Dataset:")
print(df)

# Handle missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset after handling missing values:")
print(df)

# Filter rows (Marks greater than 80)
filtered_data = df[df["Marks"] > 80]

print("\nStudents with Marks greater than 80:")
print(filtered_data)

# Group by Department and calculate average marks
grouped_data = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(grouped_data)