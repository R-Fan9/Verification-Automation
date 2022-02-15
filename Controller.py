from email import header
import pandas as pd
import utils as ut
from datetime import datetime as dt

class Controller:
    __view = None
    __checker = None
    __controller = None

    __multi_file_num = 5
    __DUP_col_num = 4

    __idx_offset = 2

    @staticmethod
    def get_instance(view, checker):
        if Controller.__controller is None:
            Controller(view, checker)
        return Controller.__controller

    def __init__(self, view, checker):
        if Controller.__controller is not None:
            raise Exception("This is a Singleton class")
        else:
            self.__view = view
            self.__checker = checker
            Controller.__controller = self
            
    def read_file_input(self):
        file_dir = input()
        return file_dir

    def read_sheet_input(self):
        input_sheet = input()
        return input_sheet

    def read_prefix_header(self):
        prefix = input()
        return prefix

    def read_header_input(self):
        header = input()
        return header
    
    def read_mode_input(self):
        user_input = input()
        while user_input not in ["s", "m"]:
            print("Please enter 's' or 'm' ")
            user_input = input()

        return user_input
    
    def read_func_input(self):
        user_input = input()
        while user_input not in [ut.COL_SUM, ut.COL_AVG]:
            print("Please enter '{}' or '{}' ".format(ut.COL_SUM, ut.COL_AVG))
            user_input = input()

        return user_input

    def __compare_df(self, df1, df2, headers):
        df_unmatch = pd.DataFrame(columns=headers)
        for idx, row in df1.iterrows():
            unmatch_row = self.__compare_util(row, idx, df2, headers)
            if unmatch_row is not None:
                df_unmatch = pd.concat([df_unmatch, unmatch_row.to_frame().T], ignore_index=True)

        return df_unmatch

    def __compare_util(self, row, idx, df2, headers):
        unmatch_row = None

        pf1 = row[0]
        pf2 = df2.iloc[idx, 0]

        val1 = row[1]
        val2 = df2.iloc[idx, 1]

        #if the two prefixes on the same index are not the same
        if pf2 != pf1:
            unmatch_row = pd.Series(
                [
                    pf1,
                    self.__idx_to_str([idx]), 
                    self.__idx_to_str(self.__checker.find_val_idx(df2, ut.COL_PREFIX, pf1))
                ], 
                index=headers
                )
        # if the two values with the same prefix are not the same
        elif val2 != val1:
            unmatch_row = pd.Series([pf1, val1, val2], index=headers)

        return unmatch_row
    
    def single_file_mode(self, file1, file2, check_idx=False, check_diff=False):
        f1_dir = file1[0]
        f2_dir = file2[0]

        f1_pfx = file1[1]["prefix"]
        f2_pfx = file2[1]["prefix"]

        f1_hd = file1[1]["header"]
        f2_hd = file2[1]["header"]

        df1 = self.__get_df_col(file1[0],file1[1])
        self.__checker.rename_col(df1, f1_pfx, ut.COL_PREFIX)

        df2 = self.__get_df_col(file2[0], file2[1])
        self.__checker.rename_col(df2, f2_pfx, ut.COL_PREFIX)

        if len(df1.index) > len(df2.index):
            df1, df2 = df2, df1
            f1_pfx, f2_pfx = f2_pfx, f1_pfx
            f1_hd, f2_hd = f2_hd, f1_hd
            f1_dir, f2_dir = f2_dir, f1_dir

        file_name = f1_dir+' vs '+f2_dir
        sheet_name = f1_hd+' - '+f2_hd

        headers = [ut.COL_PREFIX, f1_hd, f2_hd]

        df_unmatch = pd.DataFrame(
            [[
                'SUM', 
                self.__checker.get_rows_sum(df1, f1_hd), 
                self.__checker.get_rows_sum(df2, f2_hd)
            ]], 
            columns=headers)
        
        if not check_idx:
            dfj = self.__checker.join_df(df1, df2, ut.COL_PREFIX)
            self.__checker.nan_to_zero(dfj)
            df_unmatch = pd.concat(
                [
                    df_unmatch,
                    self.__checker.get_unmatch(dfj, f1_hd, f2_hd),
                ], 
                ignore_index=True)
        else:
            df_unmatch = pd.concat(
                [
                    df_unmatch,
                    self.__compare_df(df1, df2, headers)
                ],
                ignore_index=True
            )

        self.__view.print_file_names([f1_dir, f2_dir])
        self.__view.print_df(df_unmatch)

        self.__view.out_file(df_unmatch, file_name, sheet_name)

        if(check_diff):
            dfd = self.__checker.diff_df(df1, df2, ut.COL_PREFIX)
            self.__view.out_file(dfd, file_name, sheet_name+'(diff)')

    def multi_file_mode(self, f_map, file2, func):
        f2_pfx = file2[1]["prefix"]
        f2_hd = file2[1]["header"]
  
        df2 = self.__get_df_col(file2[0], file2[1])
        self.__checker.rename_col(df2, f2_pfx, ut.COL_PREFIX)

        df_mult = self.__map_to_df(f_map)

        self.__aggregate_cols(df_mult,  func)

        self.__checker.keep_cols(df_mult, [ut.COL_PREFIX, func])

        dfj = self.__checker.join_df(df_mult, df2, ut.COL_PREFIX)
        self.__checker.nan_to_zero(dfj)

        df_unmatch = self.__checker.get_unmatch(dfj, func, f2_hd)
        self.__view.print_file_names(f_map.keys().append(file2[0]))
        self.__view.print_df(df_unmatch)

    def run_checker_auto(self):
        for check in ut.check_files.keys():
            if(check == ut.REPORT_MASTER or check == ut.MASTER_DASHBOARD or check == ut.REPORT_DASHBOARD_OUT or check == ut.DASHBOARD_SINGLE):
                for files in ut.check_files[check]:
                    f1 = files[0]
                    f2 = files[1]
                    self.single_file_mode(f1, f2)
            elif(check == ut.MASTER_DEV_UAT_PROD or check == ut.DASHBOARD_DRAFT):
                i = 0
                for files in ut.check_files[check]:
                    f1 = files[0]
                    f2 = files[1]

                    col_idx = i%self.__DUP_col_num
                    date = f2[1]["header"]

                    if col_idx == 0:
                        f2[1]["header"] = dt.strptime(date + " 00:00:00", "%Y-%m-%d %H:%M:%S")
                    else:
                        f2[1]['header'] = date + ' 00:00:00.{}'.format(col_idx)
                    self.single_file_mode(f1,f2)
                    i += 1

            elif(check == ut.MULTI_MASTER_DASHBOARD or check == ut.DASHBOARD_MULTI_SUM or check == ut.DASHBOARD_MULTI_AVG):
                func = ut.COL_SUM 
                if check == ut.DASHBOARD_MULTI_AVG:
                    func = ut.COL_AVG
                    
                for files in ut.check_files[check]:
                    f1 = files[0]
                    f_map = files[1]
                    self.multi_file_mode(f_map, f1, func)
            print()

    def run_checker_manual(self):
        self.__view.print_mode_prompt()
        mode = self.read_mode_input()
        if mode == "s":
            f1 = [None]*2
            f2 = [None]*2
            self.__populate_pair(f1)
            self.__populate_pair(f2)
            self.single_file_mode(f1, f2)

        elif mode == "m":
            f_map = {}
            i = 0
            while i < self.__multi_file_num:
                inputs = self.__get_input()
                file_dir = inputs[0]
                if file_dir not in f_map:
                    f_map[inputs[0]] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}
                    i += 1

            f1 = [None]*2
            self.__populate_pair(f1)
            self.multi_file_mode(f_map, f1)

    def __idx_to_str(self, idx_list):
        return 'idx: '+','.join([str(i+self.__idx_offset) for i in idx_list])

    def __map_to_df(self, f_map):
        df = pd.DataFrame(columns=[ut.COL_PREFIX])
        for f_dir in f_map.keys():            
            df_cur = self.__get_df_col(f_dir, f_map[f_dir])
            self.__checker.rename_col(df_cur, f_map[f_dir]['prefix'], ut.COL_PREFIX)
            df = self.__checker.join_df(df, df_cur, ut.COL_PREFIX, 'outer')

        return df

    def __aggregate_cols(self, df, func):
        if func == ut.COL_SUM:
            self.__checker.sum_df_cols(df)
        elif func == ut.COL_AVG:
           self.__checker.avg_df_cols(df)

    def __get_input(self):
        self.__view.print_file_prompt()
        file_dir = self.read_file_input()
        self.__view.print_sheet_prompt()
        sheet = self.read_sheet_input()
        self.__view.print_prefix_header()
        prefix = self.read_prefix_header()
        self.__view.print_header_prompt()
        header = self.read_header_input()
        return [file_dir, sheet, prefix, header]

    def __get_df_col(self, file_dir, info_map):
        sheet = info_map["sheet"]
        prefix = info_map["prefix"]
        column = info_map["header"]

        header = 1 if sheet in [ut.SHEET_MASTER, ut.SHEET_DASHBOARD] else 0

        df = pd.read_excel(file_dir, sheet_name=sheet, header=header, engine='openpyxl')
        return df[[prefix, column]]

    def __populate_pair(self, p):
        inputs = self.__get_input()
        p[0] = inputs[0]
        p[1] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}
