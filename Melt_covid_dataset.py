import pandas as pd


# COVID dataset
covid_data_df = pd.read_csv("time_series_covid19_confirmed_global.csv")

print(covid_data_df.columns)
