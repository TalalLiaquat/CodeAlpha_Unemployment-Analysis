import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Unemployment_Rate_upto_2020.csv')

print(df.head())
print(df.info())
print(df.describe())

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

print(df.isna().sum())
df = df.dropna(subset=['Unemployment_Rate'])

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Unemployment_Rate'])
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.show()

df['Year'] = df['Date'].dt.year
yearly = df.groupby('Year')['Unemployment_Rate'].mean().reset_index()
print(yearly)

plt.figure(figsize=(10,5))
plt.bar(yearly['Year'].astype(str), yearly['Unemployment_Rate'])
plt.title('Average Unemployment Rate by Year')
plt.xlabel('Year')
plt.ylabel('Avg Unemployment Rate (%)')
plt.show()

pre_2019 = df[df['Year'] == 2019]['Unemployment_Rate'].mean()
year_2020 = df[df['Year'] == 2020]['Unemployment_Rate'].mean()
pct_change = (year_2020 - pre_2019) / pre_2019 * 100
print("2019 avg:", pre_2019)
print("2020 avg:", year_2020)
print("Change (%):", pct_change)

df['Month'] = df['Date'].dt.month
plt.figure(figsize=(10,5))
plt.boxplot([df[df['Month']==m]['Unemployment_Rate'] for m in range(1,13)], labels=list(range(1,13)))
plt.title('Unemployment Rate by Month')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.show()

df.to_csv('cleaned_unemployment.csv', index=False)
