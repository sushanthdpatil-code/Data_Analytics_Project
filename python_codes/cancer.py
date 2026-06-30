import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("D:\\Data_Analytics_project\\Datasets\\Cancer_Statewise_Dataset_500_Rows.xlsx")

print("Complete Dataset")
print(data)

print("\nFirst 5 Records")
print(data.head())

print("\nLast 5 Records")
print(data.tail())

df = data[['State',
           'Cancer_Type',
           'Cancer_Stage',
           'Diagnosed_Cases',
           'Cured_Cases',
           'Deaths',
           'Alive_Patients']]
df.columns = ['State',
              'Type',
              'Stage',
              'Diagnosed',
              'Cured',
              'Deaths',
              'Alive']
print("\nSelected Columns")
print(df.head())

state = df.groupby('State')['Diagnosed'].sum().reset_index()
print("\nState-wise Diagnosed Cases")
print(state)

plt.figure(figsize=(12,6))
sns.barplot(
    data=state,
    x='State',
    y='Diagnosed',
    hue='State',
    palette='viridis',
    legend=False
)
plt.title("State-wise Diagnosed Cancer Cases")
plt.xlabel("State")
plt.ylabel("Diagnosed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
stage = df.groupby(['State','Stage'])['Deaths'].sum().reset_index()
print("\nState-wise Deaths by Cancer Stage")
print(stage)

plt.figure(figsize=(14,6))
sns.barplot(
    data=stage,
    x='State',
    y='Deaths',
    hue='Stage',
    palette='Set2'
)
plt.title("State-wise Cancer Deaths by Stage")
plt.xlabel("State")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.legend(title="Cancer Stage", bbox_to_anchor=(1.02,1), loc='upper left')
plt.tight_layout()
plt.show()