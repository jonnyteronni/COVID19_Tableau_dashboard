import requests
import pandas as pd
#1
token = '3a82a6faa2512305d6e739630513344f4b349405'

#2

city = 'lisbon'
url = 'https://api.waqi.info/feed/'+city+'/?token='+token

response = requests.get(url).json()
print(response)
# forks_df = pd.DataFrame(response)
# forks_df
