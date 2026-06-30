import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("D:\\Data_Analytics_project\\Datasets\\StatewiseTestingDetails.csv")

print("Complete Dataset")
print(data)
x = data.head()
print("\nFirst 5 Records")
print(x)
y = data.tail()
print("\nLast 5 Records")
print(y)

df = data[['Date', 'State', 'TotalSamples', 'Negative', 'Positive']]
df.columns = ['Dt', 'St', 'Total', 'Neg', 'Pos']

print("\nSelected Columns")
print(df.head())

today = df[df['Dt'] == '2021-08-10']

print("\nCOVID Data on 2021-08-10")
print(today)

total = today.sort_values(by='Total', ascending=False)
top10_total = total.head(10)

print("\nTop 10 States by Total Samples")
print(top10_total)

plt.figure(figsize=(12,6))
sns.barplot(
    x='St',
    y='Total',
    data=top10_total,
    hue='St',
    legend=False
)
plt.title("Top 10 States by Total Samples (2021-08-10)")
plt.xlabel("State")
plt.ylabel("Total Samples")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

positive = today.sort_values(by='Pos', ascending=False)
top10_positive = positive.head(10)

print("\nTop 10 States by Positive Cases")
print(top10_positive)

plt.figure(figsize=(12,6))
sns.barplot(
    x='St',
    y='Pos',
    data=top10_positive,
    hue='St',
    legend=False
)
plt.title("Top 10 States by Positive Cases (2021-08-10)")
plt.xlabel("State")
plt.ylabel("Positive Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()