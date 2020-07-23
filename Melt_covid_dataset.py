import pandas as pd


# COVID dataset
data = pd.read_csv("sources/time_series_covid19_confirmed_global.csv")

#Melt covid to have a proper structure
clean_data = pd.melt(data, id_vars=data.columns[1:4], value_vars = data.columns[4:],
    var_name='Date', value_name='confirmed_cases')

# Get columns of datetime format
clean_data['Datetime'] = pd.to_datetime(clean_data['Date'], format="%m/%d/%y")
clean_data['year'] = clean_data['Datetime'].dt.year
clean_data['month'] = clean_data['Datetime'].dt.month
clean_data['day'] = clean_data['Datetime'].dt.day


# print(clean_data.info())
# print(clean_data.head())

# Save dataframe on a csv file
clean_data.to_csv('sources/clean_covid_db', index=False)
