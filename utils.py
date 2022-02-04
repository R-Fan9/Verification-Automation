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
file_dic_Report = ''
file_dic_Master = ''
file_dic_Master_pre = ''
file_dic_Dashboard = ''
Input_date = ''

# inputs (multi)
file_dic_Master_1 = ''
file_dic_Master_2 = ''
file_dic_Master_3 = ''
file_dic_Master_4 = ''
file_dic_Master_5 = ''

report_master = [[[file_dic_Report, {"sheet":SHEET_REPORT[0], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[0], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[1], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[1], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[2], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[2], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[3], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[3], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[4], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[4], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[5], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}]],

                 [[file_dic_Report, {"sheet":SHEET_REPORT[5], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}]]]

master_DEV_UAT_PROD = [[[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}],

                       [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}], 
                       [file_dic_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]]]

master_dashboard = [[[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[0]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[2]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[4]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[0]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[2]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[4]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[0]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[1]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[2]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[3]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[4]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[5]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[6]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[7]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[8]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[9]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[10]}]],

                    [[file_dic_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[11]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[12]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[13]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[14]}],

                    [file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[15]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[16]}]],

                    [[file_dic_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}], 
                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[17]}]]]

multi_master_dashboard = [[file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[1]}],
                    {file_dic_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dic_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dic_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dic_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dic_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}},

                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[3]}],
                    {file_dic_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dic_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dic_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dic_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dic_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}},

                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[5]}],
                    {file_dic_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dic_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dic_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dic_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dic_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}},

                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[1]}],
                    {file_dic_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dic_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dic_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dic_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dic_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}},

                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[3]}],
                    {file_dic_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dic_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dic_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dic_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dic_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}},

                    [file_dic_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[5]}],
                    {file_dic_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dic_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dic_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dic_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dic_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}}]

check_files = {'rm': report_master, 'm_DUP': master_DEV_UAT_PROD, 'md': master_dashboard, 'mmd':multi_master_dashboard}