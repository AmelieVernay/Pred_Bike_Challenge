# ---------- requirements ----------
import pandas as pd
import datetime
from datetime import date
# import the class that loads and saves data
# (see load_data.py)
import load_data

# ---------- loading dataset ----------

df_totem = load_data.Load_totemdata().save_as_df()

# ---------- first cleaning ----------


def totem_first_cleaning(df_totem):
    '''
    Specific function for the df_totem dataframe
    -----
    Input:
        df_totem: the dataframe from <url>
    Output:
        df_totem left with relevent only renamed columns,
        i.e. "Today's total", with no NaN values, and an index
        column set to a datetime object
    '''
    # rename the columns
    df_totem.columns = ["Date", "Hour", "Big total",
                        "Today's total", "Unnamed", "Remark"]
    # only keep date-related and today's total columns
    df_totem.drop(['Big total', 'Unnamed', 'Remark'], inplace=True, axis=1)
    # merging date and hour in one column
    df_totem['Date'] = df_totem['Date'] + ' ' + df_totem['Hour']
    df_totem.drop(['Hour'], inplace=True, axis=1)
    # converting the 'Date' column into a datetime object
    df_totem['Date'] = pd.to_datetime(df_totem['Date'],
                                      format='%d/%m/%Y %H:%M:%S')
    df_totem.set_index('Date', inplace=True)
    # df_totem2 = df_totem2.sort_index() # just to be sure
    # drop eventual na values
    df_totem = df_totem.dropna(subset=["Today's total"])
    return df_totem


# ---------- time slicing ----------


def from_select_date(df, year, month, day):
    '''
    Keep values of df from a given day, drop the others
    -----
    Input:
        df: dataframe containing a 'Date' column
        year: int corresponding to...well it should be obvious
        month: int
        day: int
    Output:
        dataframe containing the values of df from the given day only
    '''
    df_temp = df.reset_index()
    df_temp = df_temp.loc[
        df_temp['Date'].dt.date >= datetime.date(year, month, day)]
    return df_temp


# keep only days for which we have a first entry before a given hour


def drop_hour_gap(df, hour):
    '''
    Drop days with too much missing informations
    -----
    Input:
        df: dataframe containing a 'Date' column of type datetime
        hour: integer. Only the days for which we have a first entry
        before "hour" AM will be kept.
        e.g. if hour=12, then any day for which there is no entry
        before 12 AM won't be kept in the dataframe
    Output:
        dataframe only containing days with "enough" values
    '''
    df.reset_index(inplace=True)
    unique = df['Date'].dt.date.unique()
    frames = []
    for i in range(len(unique)):
        i_day = df.loc[df['Date'].dt.date == unique[i]]
        i_day.reset_index(inplace=True)
        if (i_day['Date'][0].hour < hour):
            frames.append(i_day)
    dff = pd.concat(frames)
    # remove magically appeared columns...
    del dff['level_0']
    del dff['index']
    return dff


def resamp_interp(df):
    '''
    Resample and interpolate
    -----
    Input:
        dataframe containing a 'Date' column of type datetime
    Output:
        the dataframe resampled by minutes with NaN values filled
        using linear interpolation.
    Note:
        The for loop adds a zero value for the time 00:00 to
        00:59 each day. It could have been only for 00:00 but since
        no bike are passing on the totem at this time of the day,
        (or at least no one is there to note it!) well I
        found it more relevant to set this to zero for the
        coming interpolation purpose.
    '''
    # downsampling to the greatest common time basis: minute
    df_minutes = df.set_index('Date').resample('1min').mean()
    dftemp = df_minutes.copy()
    dftemp.reset_index(inplace=True)
    for i in range(len(dftemp)):
        if (dftemp['Date'][i].hour == 0):
            dftemp["Today's total"][i] = 0.0
    # (linear) interpolation to fill the NaN values
    df_minutes = dftemp.set_index('Date').interpolate()
    return df_minutes


def only_at(df, hour):
    '''
    Select only the rows corresponding to a given hour
    -----
    Input:
        df: dataframe with a datetime index 'Date'
        hour: int corresponding to the hour we want to
        keep for each day in the dataframe
    Output:
        dataframe with only 'hour' as hour for each day
    '''
    dftemp = df.copy()
    dftemp.reset_index(inplace=True)
    df_at_hour = dftemp.loc[
        (dftemp['Date'].dt.hour == hour) & (dftemp['Date'].dt.minute == 0)]
    return df_at_hour


def pick_week_days(df):
    '''
    Pick only the week days of a dataframe containing dates
    ------
    Input:
        df: dataframe with a datetime index 'Date'
    Output:
        dataframe df with only its week days
    '''
    # monday = 0, sunday = 6
    df_week = df.loc[df.index.dayofweek <= 4]
    return df_week
