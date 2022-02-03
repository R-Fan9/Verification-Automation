
from matplotlib.pyplot import axis
import pandas as pd
import numpy as np

class checker:
    def join_df(df1, df2, key):
        df_join = df1.merge(df2, how="inner", on=key)
        return df_join
    
    def filter_unmatch(df, col1, col2):
        df_unmatch = df[df[col1] != df[col2]]
        return df_unmatch
    
    def sum_df_cols(df):
        df["Sum"] = df.sum(axis= 1, skipna= True)
        return df
    
    def avg_df_cols(df):
        df_sum = checker.sum_df_cols(df)
        Columns = len(df_sum.columns)
        i = 0
        for row in df_sum["Sum"]:
            avg = row / (Columns - 2)
            df_sum["Sum"].loc[[i]] = avg
            i += 1
        df_avg = df_sum.rename(columns= {"Sum":"Avg"})
        return df_avg

    def drop_cols(df, prefix_col, col_name):
        for col in df.columns:
            if col != col_name and col != prefix_col:
                df = df.drop([col], axis=1)
            else:
                continue
        return df
