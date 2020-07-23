import pandas as pd

# COVID dataset
data = pd.read_csv("sources/Air_source/waqi-covid19-airqualitydata-2020.csv")


# Get columns of datetime format
# clean_data['Datetime'] = pd.to_datetime(clean_data['Date'], format="%m/%d/%y")
# clean_data['year'] = clean_data['Datetime'].dt.year
# clean_data['month'] = clean_data['Datetime'].dt.month
# clean_data['day'] = clean_data['Datetime'].dt.day

print(data.head())

# print(clean_data.info())
# print(clean_data.head())

# Save dataframe on a csv file
# clean_data.to_csv('sources/clean_covid_db', index=False)
