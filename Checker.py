import utils as ut
import pandas as pd

class Checker:

    @staticmethod
    def join_df(df1, df2, key, how="inner"):
        df_join = df1.merge(df2, how=how, on=key)
        return df_join
    
    @staticmethod
    def diff_df(df1, df2):
        df = pd.concat([df1,df2]).drop_duplicates(keep=False)
        return df
    
    @staticmethod
    def get_rows_sum(df):
        df.loc["Total"] = df.sum(numeric_only=True)
    
    @staticmethod
    def find_val_idx(df, header):
        index = []
        for i in df[header]:
            index.append(i)
        return index

    @staticmethod
    def get_unmatch(df, col1, col2):
        df_unmatch = df[df[col1] != df[col2]]
        return df_unmatch

    @staticmethod 
    def sum_df_cols(df):
        df[ut.COL_SUM] = df.sum(axis=1, skipna=True)

    @staticmethod
    def avg_df_cols(df):
        df[ut.COL_AVG] = df.mean(axis=1, skipna=True)

    @staticmethod
    def nan_to_zero(df):
        df.fillna(0, inplace = True)

    @staticmethod
    def rename_col(df, old_name, new_name):
        df.rename(columns={old_name: new_name}, inplace = True)

    @staticmethod
    def keep_cols(df, cols):
        for col in df.columns:
            if col not in cols:
                df.drop([col], inplace=True, axis=1)

