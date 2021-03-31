import pandas as pd
import datetime
import os

# initialize weather dataframe
initial_day1 = datetime.date(2021, 3, 4)
initial_day2 = datetime.date(2021, 3, 5)

weather = pd.DataFrame([[initial_day1, 0., 5., 36.], [initial_day2, 0., 5., 15.]], columns=['Date', 'rain', 'wind', 'cloud'])


path = 'D:\\Users\\Vamelie\\Desktop\\dvlpmt_log\\bike_challenge\\'
weather.to_csv(os.path.join(path, r'weather.csv'))

#print(weather)