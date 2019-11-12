import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns


def combine_by_title(df):
    title_alias = pd.read_csv('title.akas.csv')
    title_alias.groupby('title_id')
    combined_dataframe_title = pd.concat([df, title_alias], axis=0,
                                         join='outer')
    return combined_dataframe_title


def combine_by_id(df):
    title_alias = pd.read_csv('title.akas.csv')
    title_alias.groupby('title_id')
    combined_dataframe_id = pd.concat([df, title_alias], axis=0, join='outer')
    return combined_dataframe_id
