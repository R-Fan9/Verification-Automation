
import pandas as pd



'''
f_map = {}

for i in range(0, 5):
    ##inputs = get_input()
    inputs = ["C:\\Users\\12269\\Desktop\\Coding\Work\\1,17\\Report.xlsx", "A1D", "AppPrefix", "Define"]
    f_map[inputs[0]] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}




inputs = ["C:\\Users\\12269\\Desktop\\Coding\Work\\1,17\\Report.xlsx", "A1D", "AppPrefix", "Define"]
##print(inputs[0])
p = {}
p[0] = inputs[0]
p[1] = {"sheet":inputs[1], "prefix":inputs[2], "header":inputs[3]}
print(p)

j = 0
for i in range(0, 5):
    print(j)
    j += 2

'''
COL_PREFIX = 'prefix'
COL_SUM = 'sum'
COL_AVG = 'avg'

# Report
SHEET_REPORT = ["A1D","A1U","A1P","C1D","C1U","C1P"]
REPORT_PREFIX = "AppPrefix"
REPORT_HEADER = ["TotalJobsDefined", "TotalJobsRun"]

# Master
SHEET_MASTER = 'WeeklyReport'
MASTER_PREFIX = "Prefix"
MASTER_HEADER = ["A1D DEF", "A1D RUN", "A1U DEF", "A1U RUN", "A1P DEF", "A1P RUN",
                 "C1D DEF", "C1D RUN", "C1U DEF", "C1U RUN", "C1P DEF", "C1P RUN"]

# DEF, UAT, PROD
SHEET_DEV = "DEV"
SHEET_UAT = "UAT"
SHEET_PROD = "PROD"
PREFIX_D_U_P = "Prefix"

# Dashboard
SHEET_DASHBOARD = 'AutoSysDashboard'
DASHBOARD_PREFIX = "Prefix"
DASHBOARD_HEADER_11 = ["TotalJobsDefined (DEV - R11.0)", "TotalJobsRun (DEV - R11.0)",
                       "TotalJobsDefined (UAT - R11.0)", "TotalJobsRun (UAT - R11.0)",
                       "TotalJobsDefined (PROD - R11.0)", "TotalJobsRun  (PROD - R11.0)"]

DASHBOARD_HEADER_36 = ["TotalJobs Defined (DEV - R11.3.6)", "TotalJobsRun (DEV - R11.3.6)",
                       "TotalJobsDefined (UAT - R11.3.6)", "TotalJobsRun (UAT - R11.3.6)",
                       "TotalJobsDefined (PROD - R11.3.6)", "TotalJobsRun (PROD - R11.3.6)"]

DASHBOARD_PRE_CUR = ["A1D", "A1U", "A1P", "C1D", "C1U", "C1P",
                     "A1D Runs", "A1U Runs", "A1P Runs", "C1D Runs", "C1U Runs", "C1P Runs",
                     "A1D RUN_PAST", "A1U RUN_PAST", "A1P RUN_PAST", "C1D RUN_PAST", "C1U RUN_PAST", "C1P RUN_PAST"]


# inputs (single)
file_dic_Dashboard = "board"

# inputs (multi)
file_dic_Master_1 = 1
file_dic_Master_2 = 2
file_dic_Master_3 = 3
file_dic_Master_4 = 4
file_dic_Master_5 = 5

master_dashboard = [[file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[1]}],
                    [[file_dic_Master_1, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}],
                    [file_dic_Master_2, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}],
                    [file_dic_Master_3, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}],
                    [file_dic_Master_4, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}],
                    [file_dic_Master_5, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}]],
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[3]}],
                    [[file_dic_Master_1, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}],
                    [file_dic_Master_2, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}],
                    [file_dic_Master_3, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}],
                    [file_dic_Master_4, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}],
                    [file_dic_Master_5, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}]],
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[5]}],
                    [[file_dic_Master_1, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}],
                    [file_dic_Master_2, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}],
                    [file_dic_Master_3, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}],
                    [file_dic_Master_4, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}],
                    [file_dic_Master_5, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}]],
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[1]}],
                    [[file_dic_Master_1, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}],
                    [file_dic_Master_2, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}],
                    [file_dic_Master_3, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}],
                    [file_dic_Master_4, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}],
                    [file_dic_Master_5, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}]],
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[3]}],
                    [[file_dic_Master_1, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}],
                    [file_dic_Master_2, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}],
                    [file_dic_Master_3, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}],
                    [file_dic_Master_4, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}],
                    [file_dic_Master_5, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}]],
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[5]}],
                    [[file_dic_Master_1, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}],
                    [file_dic_Master_2, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}],
                    [file_dic_Master_3, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}],
                    [file_dic_Master_4, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}],
                    [file_dic_Master_5, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}]]]


print(master_dashboard[1][0][1]["sheet"])