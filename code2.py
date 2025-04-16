import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
file_path = 'D:/INT375 Project/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69 (1) (1).csv'
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Parse datetime column
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print(df.columns)
df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')

# Convert numeric column
df['pollutant_avg'] = pd.to_numeric(df['pollutant_avg'], errors='coerce')

# Drop rows with missing essential values
df = df.dropna(subset=['last_update', 'pollutant_avg', 'latitude', 'longitude', 'pollutant_id'])

# Set Seaborn style
sns.set(style="whitegrid")

# ========== 1. Pie Chart: Distribution of Data Points by Pollutant ==========
pollutant_counts = df["pollutant_id"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(pollutant_counts.values, labels=pollutant_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Data Points by Pollutant Type")
plt.axis('equal')
plt.tight_layout()
plt.show()

# ========== 2. Bar Graph (Horizontal): Top 10 Most Polluted Cities ==========
top_cities = df.groupby("city")["pollutant_avg"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette="magma", legend=False)
plt.title("Top 10 Most Polluted Cities")
plt.xlabel("Avg Pollutant Level")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# ========== 3. Column Graph (Vertical Bar): Avg Pollutant by Type ==========
avg_pollutant = df.groupby("pollutant_id")["pollutant_avg"].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_pollutant.index, y=avg_pollutant.values, hue=avg_pollutant.index, palette="viridis", legend=False)
plt.title("Average Pollutant Level by Type")
plt.xlabel("Pollutant")
plt.ylabel("Average Level")
plt.tight_layout()
plt.show()

# ========== 4. Heatmap: Average Pollutant by State & Type ==========
heatmap_data = df.pivot_table(index='state', columns='pollutant_id', values='pollutant_avg', aggfunc='mean')
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlOrRd")
plt.title("Pollution Levels by State and Pollutant")
plt.xlabel("Pollutant ID")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# ========== 5. Scatter Plot: Pollution Distribution by Location ==========
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='pollutant_avg', size='pollutant_avg', palette='coolwarm', legend=False)
plt.title("Pollution by Location")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()


#6. Plot KDE (Density Plot) distribution of pollution levels (pollutant_avg) across all your data points.
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x="pollutant_avg", fill=True, color="purple", linewidth=2)
plt.title("Density Distribution of Pollution Levels")
plt.xlabel("Pollutant Average")
plt.ylabel("Density")
plt.grid(True)
plt.tight_layout()
plt.show()

