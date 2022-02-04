class Checker:
    COL_SUM = "Sum"
    COL_AVG = "AVG"

    def rename_col(df, old_name, new_name):
        df.rename(columns={old_name: new_name})
        return df

    def join_df(df1, df2, key, how="inner"):
        df_join = df1.merge(df2, how=how, on=key)
        return df_join
    
    def get_unmatch(df, col1, col2):
        df_unmatch = df[df[col1] != df[col2]]
        return df_unmatch
    
    def sum_df_cols(self, df):
        df[self.COL_SUM] = df.sum(axis=1, skipna=True)
        return df
    
    def avg_df_cols(self, df):
        df[self.COL_AVG] = (df.sum(axis= 1, skipna= True))/(len(df.columns) - 1)
        return df

    def nan_to_zero(df):
        df.fillna(0)
        return df

    def drop_cols(df, cols):
        for col in df.columns:
            if col not in cols:
                df = df.drop([col], axis=1)
        return df
    

