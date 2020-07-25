import pandas as pd

data = pd.read_csv('../sources/Air_source/csv/covid19_totalDB_clean.csv',header=0, sep=',')

countries = ['IN']

filtered_data = data[data['Country']=='IN']

# print(filtered_data.head())
# print(filtered_data.columns)
# print(filtered_data.head(10))
filtered_data.to_csv('../sources/Air_source/csv/India_covid19_totalDB_clean.csv', index=False)
