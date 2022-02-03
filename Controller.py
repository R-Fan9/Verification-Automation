
import numpy as np
import pandas as pd

from Checker import checker
from View import view

class controller:

    def read_file_input():
        input_file = input()
        return input_file

    def read_sheet_input():
        input_sheet = input()
        return input_sheet

    def read_prefix_header():
        prefix = input()
        return prefix

    def read_header_input():
        header = input()
        return header
    
    def read_mode_input():
        view.print_mode_prompt()
        while True:
            user_input = input()
            if user_input == "single" or user_input == "multi":
                break
            else:
                print("Pick single or multi mode ")
                continue

        return user_input
    
    def read_func_input():
        view.print_func_prompt()
        while True:
            user_input = input()
            if user_input == "sum" or user_input == "avg":
                break
            else:
                print("Pick sum or avg ")
                continue

        return user_input
    
    def single_file_mode(file1, file2):
        df1 = get_df_col(file1[0],file2[1])
        df2 = get_df_col(file2[0], file2[1])
        dfj = checker.join_df(df1, df2, file1[1]["prefix"]) #TroubleShooting
        df_unmatches = checker.filter_unmatch(dfj, file1[1]["header"], file2[2]["header"])
        view.print_df(df_unmatches)
        

    def multi_file_mode(f_map, file2):
        f_arr = [None]*5
        j = 0
        for i in range(0, 5):
            f_arr[i] = get_df_col(f_map[j], f_map[j+1])
            j += 2
        
        df_mult = f_arr[0]
        for i in range(0, 4):
            df_mult = checker.join_df(df_mult, f_arr[i+1])

        view.print_func_prompt()
        input_func = controller.read_func_input()
        df2 = get_df_col(file2[0], file2[1])

        if input_func == "sum":
            df_sum = checker.sum_df_cols(df_mult)
            df_sum = checker.drop_cols(df_mult, f_map[1]["prefix"], "Sum")
            df_join = checker.join_df(df_sum, df2, f_map[1]["prefix"])
            df_numatches = checker.filter_unmatch(df_join, "Sum", file2[1]["header"])

        if input_func == "avg":
            df_avg = checker.avg_df_cols(df_mult)
            df_avg = checker.drop_cols(df_mult, f_map[1]["prefix"], "Avg")
            df_join = checker.join_df(df_avg, df2, f_map[1]["prefix"])
            df_numatches = checker.filter_unmatch(df_join, "Avg", file2[1]["header"])
        
        view.print_df(df_numatches)
    
    def run_checker():
        mode = controller.read_mode_input()
        if mode == "single":
            f1 = [None]*2
            f2 = [None]*2
            populate_pair(f1)
            populate_pair(f2)
            controller.single_file_mode(f1, f2)

        if mode == "multi":
            f_map = {}
            f1 = [None]*2
            populate_pair(f1)
            for i in range(0, 5):
                inputs = get_input()
                f_map[inputs[0]] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}
            controller.multi_file_mode(f_map, f1)
            


def get_input():
    view.print_file_prompt()
    file_dir = controller.read_file_input()
    view.print_sheet_prompt()
    sheet = controller.read_sheet_input()
    view.print_prefix_header()
    prefix = controller.read_prefix_header()
    view.print_header_prompt()
    header = controller.read_header_input()
    out = [file_dir, sheet, prefix, header]
    return out

def get_df_col(file_dir, info_map):
    sheet = info_map["sheet"]
    prefix = info_map["prefix"]
    column = info_map["header"]
    if sheet == "WeeklyReport" or sheet == "AutoSysDashboard":
        df = pd.read_excel(file_dir, sheet_name=sheet, header=1)
    else:
        df = pd.read_excel(file_dir, sheet_name=sheet)
    df = df[[prefix, column]]
    return df

def populate_pair(p):
    inputs = get_input()
    p[0] = inputs[0]
    p[1] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}
    return p



path1 = 'C:\\Users\\12269\\Desktop\\Coding\Work\\1,17\\Report.xlsx'
sheet1 = "A1D"
path2 = "C:\\Users\\12269\\Desktop\\Coding\\Work\\1,17\\MasterAfterUpdates_1.17.xlsx"
sheet2 = "WeeklyReport"
key1 = "TotalJobsDefined"

out = get_df_col([path2, sheet2, "Prefix", "A1D DEF"])
print(out)
##controller.run_checker()

'''
a = controller.read_file_input(path1, sheet1)

##df = Checker.sum_df_cols(a, "AppPrefix")
df = checker.avg_df_cols(a)
df1 = checker.drop_cols(df, "AppPrefix", "Avg")


##print(a)

##print(controller.single_file_mode(path1, sheet1, "AppPrefix", "TotalJobsDefined", path2, sheet2, "Prefix", "A1D DEF", key1))
dk = controller.read_header_input(path1, sheet1, "AppPrefix", "TotalJobsDefined")

'''