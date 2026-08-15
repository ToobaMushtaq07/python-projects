import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample numeric dataset
data = {
    "Math": [80, 85, 90, 75, 95],
    "Science": [78, 88, 92, 70, 96],
    "English": [85, 80, 88, 82, 90],
    "Computer": [90, 92, 95, 85, 98]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df.corr()

# Create heatmap
sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()