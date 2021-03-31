import pandas as pd
import datetime
# import os

# import weather file
weather = pd.read_csv("weather.csv", index_col=0)


def today_weather(rain, wind, cloud):
    """
    Formatting today's given weather
    -----
    Input:
        rain: float corresponding to the amount of precipitation (mm/m^2)
        wind: float corresponding to the average wind speed (km/h)
        cloud: float corresponding to the percentage of sky coverage
    Output:
        dataframe containing the given weather if the
        day isn't already in the dataframe 'weather',
        a warning string otherwise
    """
    today = datetime.date.today()
    if weather['Date'].iloc[-1] != weather['Date'].iloc[-2]:
        df_today_weather = pd.DataFrame(
                                [[today, rain, wind, cloud]],
                                columns=['Date', 'rain', 'wind', 'cloud'])
        return df_today_weather
    else:
        print("today's weather has already been added!")


# Update weather with today's weather
weather = weather.append(today_weather(0., 3., 5.), ignore_index=True)

# print(weather)
# Save changes
weather.to_csv('weather.csv')
