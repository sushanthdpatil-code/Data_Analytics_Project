import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("D:\\Data_Analytics_project\\Datasets\\india_lpg_crisis.csv")

print("Complete Dataset")
print(data)
print("\nFirst 5 Records")
print(data.head())

print("\nLast 5 Records")
print(data.tail())

print("\nSummary Statistics")
print(data.describe())

df = data[['Year',
           'State',
           'Monthly_Demand_MT',
           'Supply_Received_MT',
           'Supply_Deficit_Percent',
           'Avg_Cylinder_Price_INR',
           'Households_Affected_Percent',
           'Black_Market_Index',
           'Crisis_Severity']]

print("\nSelected Columns")
print(df.head())

today = df[df['Year'] == 2026]

print("\nLPG Crisis Data - 2026")
print(today)
deficit = today.sort_values(by='Supply_Deficit_Percent', ascending=False)
top10_deficit = deficit.head(10)

print("\nTop 10 States by Supply Deficit")
print(top10_deficit)

plt.figure(figsize=(12,6))

sns.barplot(
    x='State',
    y='Supply_Deficit_Percent',
    data=top10_deficit,
    hue='State',
    legend=False,
    palette='viridis'
)

plt.xticks(rotation=45)
plt.title("Top 10 States by LPG Supply Deficit (2026)")
plt.xlabel("State")
plt.ylabel("Supply Deficit (%)")
plt.tight_layout()
plt.show()

affected = today.sort_values(by='Households_Affected_Percent', ascending=False)
top10_affected = affected.head(10)

print("\nTop 10 States by Households Affected")
print(top10_affected)

plt.figure(figsize=(12,6))

sns.barplot(
    x='State',
    y='Households_Affected_Percent',
    data=top10_affected,
    hue='State',
    legend=False,
    palette='Set2'
)

plt.xticks(rotation=45)
plt.title("Top 10 States by Households Affected (2026)")
plt.xlabel("State")
plt.ylabel("Households Affected (%)")
plt.tight_layout()
plt.show()