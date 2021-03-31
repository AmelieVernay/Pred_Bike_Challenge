from download import download
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv'
path_target = "./Data/SaisiesTotem.csv"


class Load_totemdata:
    def __init__(self, url=url, target_name=path_target):
        download(url, target_name, replace=True)
        # above, set replace to True to always get the updated version

    @staticmethod
    def save_as_df():
        df = pd.read_csv(path_target)
        return df
