import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


def removing_na_values(df, column_name):
    df[df[column_name]].remove_na()
    return df

def money_values_to_integer(df, column_name):
    series_string = df[column_name].to_string(index=False,header=False)
    string_to_convert = series_string.replace('$', '')
    string_to_convert = string_to_convert.replace(',', '')
    list_to_convert = string_to_convert.split()
    cleaned_series = pd.Series(list_to_convert)
    money_as_int = pd.to_numeric(cleaned_series)
    df[column_name] = money_as_int
    return df

def clean_director_columns(df):
    df.reset_index(inplace=True)
    df.worldwide_gross.astype('int64')
    df.rename(columns={'primary_name': 'Director','worldwide_gross': 'Average Worldwide Box Office',
                       'profitability': 'Average Profit per Movie', 'num_of_movies': 'Number of Movies'}, inplace=True)
    return df

def clean_actor_columns(df):
    df.reset_index(inplace=True)
    df.worldwide_gross.astype('int64')
    df.rename(columns={'primary_name': 'Actor','worldwide_gross': 'Average Worldwide Box Office',
                       'profitability': 'Average Profit per Movie', 'num_of_movies': 'Number of Movies'}, inplace=True)
    return df

def drop_by_less_than_equal_to(df, column_name, value):
    to_remove = df.loc[df[column_name] <= value]
    df.drop(index=to_remove.index, inplace=True)
    return df

def drop_by_not_equal(df, column_name, value):
    to_remove = df.loc[df[column_name] != value]
    df.drop(index=to_remove.index, inplace=True)
    return df