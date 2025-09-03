import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Project': ['Bridge A', 'Road B', 'Building C', 'Bridge D', 'Road E'],
    'Material Cost': [150000, 120000, 250000, 180000, 110000],
    'Labor Cost': [80000, 70000, 130000, 90000, 65000],
    'Equipment Cost': [50000, 40000, 70000, 60000, 35000],
    'Total Area (sq.m)': [1000, 800, 1500, 1100, 700]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate Total Cost
df['Total Cost'] = df['Material Cost'] + df['Labor Cost'] + df['Equipment Cost']

# Cost per sq.m
df['Cost per sq.m'] = df['Total Cost'] / df['Total Area (sq.m)']

# Display the DataFrame
print("Construction Cost Data:\n", df)

# Plotting
plt.figure(figsize=(10,6))
sns.barplot(x='Project', y='Total Cost', data=df, palette='viridis')
plt.title('Total Construction Cost by Project')
plt.ylabel('Total Cost (BDT)')
plt.xlabel('Project')
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df[['Material Cost', 'Labor Cost', 'Equipment Cost', 'Total Cost', 'Cost per sq.m']].corr(), annot=True, cmap='coolwarm')
plt.title('Cost Component Correlation Heatmap')
plt.tight_layout()
plt.show()
