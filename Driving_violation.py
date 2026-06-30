import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("D:\\Data_Analytics_project\\Datasets\\Indian_Traffic_Violations.csv")

print("Complete Dataset")
print(data)
print("\nFirst 5 Records")
print(data.head())
print("\nLast 5 Records")
print(data.tail())

print("\nSummary Statistics")
print(data.describe())

df = data[['Violation_Type',
           'Fine_Amount',
           'Location',
           'Registration_State',
           'License_Type']]

df.columns = ['Viol', 'Fine', 'Loc', 'State', 'License']

print("\nSelected Columns")
print(df.head())

state = df.groupby('State').size().reset_index(name='Total_Violations')

print("\nState-wise Traffic Violations")
print(state)

plt.figure(figsize=(12,6))
sns.barplot(
    data=state,
    x='State',
    y='Total_Violations',
    hue='State',
    palette='viridis',
    legend=False
)
plt.title("State-wise Traffic Violations")
plt.xlabel("Registration State")
plt.ylabel("Number of Violations")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
reason = df.groupby(['State', 'Viol']).size().reset_index(name='Total')
print("\nState-wise Violation Types")
print(reason)

plt.figure(figsize=(16,6))
sns.barplot(
    data=reason,
    x='State',
    y='Total',
    hue='Viol',
    palette='Set2'
)
plt.title("State-wise Violation Types")
plt.xlabel("Registration State")
plt.ylabel("Number of Violations")
plt.xticks(rotation=45)
plt.legend(
    title="Violation Type",
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)
plt.tight_layout()
plt.show()