import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


def removing_na_values(df, column_name):
    df[df[column_name]].remove_na()
    return df

def money_values_to_integer(df, column_name):
    series = df[column_name]
    series_string = series.to_string(index=False,header=False)
    string_to_convert = series_string.replace('$', '')
    string_to_convert = string_to_convert.replace(',', '')
    list_to_convert = string_to_convert.split()
    cleaned_series = pd.Series(list_to_convert)
    money_as_int = pd.to_numeric(cleaned_series)
    df[column_name] = money_as_int
    return df
