import pandas as pd
import utils as ut

class Controller:
    __view = None
    __checker = None
    __controller = None

    __multi_file_num = 5
    __DUP_col_num = 4

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
    
    def single_file_mode(self, file1, file2):

        f1_pfx = file1[1]["prefix"]
        f2_pfx = file2[1]["prefix"]

        f1_hd = file1[1]["header"]
        f2_hd = file2[1]["header"]

        df1 = self.__get_df_col(file1[0],file1[1])
        self.__checker.rename_col(df1, f1_pfx, ut.COL_PREFIX)

        df2 = self.__get_df_col(file2[0], file2[1])
        self.__checker.rename_col(df2, f2_pfx, ut.COL_PREFIX)

        dfj = self.__checker.join_df(df1, df2, ut.COL_PREFIX)
        self.__checker.nan_to_zero(dfj)

        df_unmatch = self.__checker.get_unmatch(dfj, f1_hd, f2_hd)
        self.__view.print_file_names([file1[0], file2[0]])
        self.__view.print_df(df_unmatch)
        print()

    def multi_file_mode(self, f_map, file2):

        f2_pfx = file2[1]["prefix"]
        f2_hd = file2[1]["header"]
  
        df2 = self.__get_df_col(file2[0], file2[1])
        self.__checker.rename_col(df2, f2_pfx, ut.COL_PREFIX)

        df_mult = self.__map_to_df(f_map)

        self.__view.print_func_prompt()
        func = self.read_func_input()

        self.__aggregate_cols(df_mult,  func)

        self.__checker.keep_cols(df_mult, [ut.COL_PREFIX, func])

        dfj = self.__checker.join_df(df_mult, df2, ut.COL_PREFIX)
        self.__checker.nan_to_zero(dfj)

        df_unmatch = self.__checker.get_unmatch(dfj, func, f2_hd)
        self.__view.print_file_names(f_map.keys().append(file2[0]))
        self.__view.print_df(df_unmatch)
        print()

    def run_checker_auto(self):
        for check in ut.check_files.keys():
            if(check == 'rm' or check == 'md'):
                for files in ut.check_files[check]:
                    f1 = files[0]
                    f2 = files[1]
                    self.single_file_mode(f1, f2)
            elif(check == 'm_DUP'):
                i = 0
                for files in ut.check_files[check]:
                    f1 = files[0]
                    f2 = files[1]
                    f2[1]['header'] += ' 00:00:00.{}'.format(i%self.__DUP_col_num)
                    self.single_file_mode(f1,f2)
                    i += 1
            elif(check == 'mmd'):
                for files in ut.check_files[check]:
                    f1 = files[0]
                    f_map = files[1]
                    self.multi_file_mode(f_map, f1)

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

        df = pd.read_excel(file_dir, sheet_name=sheet, header=header)
        return df[[prefix, column]]

    def __populate_pair(self, p):
        inputs = self.__get_input()
        p[0] = inputs[0]
        p[1] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}
