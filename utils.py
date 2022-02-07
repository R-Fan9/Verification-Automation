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
SHEET_DEV = " DEV "
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
file_dir_Report = 'Report.xlsx'
file_dir_Master = 'MasterAfterUpdates_1.17.xlsx'
file_dir_Master_pre = ''
file_dir_Dashboard = 'AutosysMigration_dashboard2.xlsm'
Input_date = '2022-2-7'

# inputs (multi)
file_dir_Master_1 = ''
file_dir_Master_2 = ''
file_dir_Master_3 = ''
file_dir_Master_4 = ''
file_dir_Master_5 = ''

report_master = [[[file_dir_Report, {"sheet":SHEET_REPORT[0], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[0], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[1], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[1], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[2], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[2], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[3], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[3], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[4], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[4], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[5], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[0]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}]],

                 [[file_dir_Report, {"sheet":SHEET_REPORT[5], "prefix":REPORT_PREFIX, "header":REPORT_HEADER[1]}], 
                 [file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}]]]

master_DEV_UAT_PROD = [[[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_DEV, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_UAT, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]],

                       [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}], 
                       [file_dir_Dashboard, {"sheet":SHEET_PROD, "prefix":PREFIX_D_U_P, "header":Input_date}]]]

master_dashboard = [[[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[0]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[2]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[4]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[0]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[2]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[4]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[0]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[0]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[2]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[1]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[4]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[2]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[6]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[3]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[8]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[4]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[10]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[5]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[6]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[7]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[8]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[9]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[10]}]],

                    [[file_dir_Master, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[11]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[12]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[13]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[14]}],

                    [file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[15]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[16]}]],

                    [[file_dir_Master_pre, {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}], 
                    [file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_PRE_CUR[17]}]]]

multi_master_dashboard = [[[file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[1]}],
                    {file_dir_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dir_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dir_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dir_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]},
                    file_dir_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[1]}}],

                    [[file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[3]}],
                    {file_dir_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dir_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dir_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dir_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]},
                    file_dir_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[3]}}],

                    [[file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_11[5]}],
                    {file_dir_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dir_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dir_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dir_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]},
                    file_dir_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[5]}}],

                    [[file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[1]}],
                    {file_dir_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dir_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dir_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dir_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]},
                    file_dir_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[7]}}],

                    [[file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[3]}],
                    {file_dir_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dir_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dir_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dir_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]},
                    file_dir_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[9]}}],

                    [[file_dir_Dashboard, {"sheet":SHEET_DASHBOARD, "prefix":DASHBOARD_PREFIX, "header":DASHBOARD_HEADER_36[5]}],
                    {file_dir_Master_1: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dir_Master_2: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dir_Master_3: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dir_Master_4: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]},
                    file_dir_Master_5: {"sheet":SHEET_MASTER, "prefix":MASTER_PREFIX, "header":MASTER_HEADER[11]}}]]


# MOA
# utilis for MOA update

# Report
SHEET_REPORT_MOA = "report"
REPORT_PREFIX_MOA = "Client-App"
REPORT_HEADER_MOA = ["TotalJobsDefined", "TotalJobsRun", "TotalJobAlarms", "TotalJobsChanges"]

# Dashboard_out
SHEET_OUT = 'dashboard'
OUT_PREFIX = "Prefix"
OUT_HEADER = ["Jobs Defined", "Jobs Run", "Job Alarms", "TotalJobsChanges"]

# DRAFT
SHEET_DRAFT = "DRAFT-MOA"
DRAFT_PREFIX = "Prefix"

# Dashboard
SHEET_DASHBOARD_MOA = 'DRAFT-MOA Dashboard'
DASHBOARD_PREFIX_MOA = "Prefix"
DASHBOARD_HEADER_MOA_SINGLE = ["Jobs Defined", "Job Change", "Def_Previous", "Run_Current", "Prev_alarm", "Current_alarm", "Prev_Change"]

DASHBOARD_HEADER_MOA_MULTI_SUM = ["Jobs Run", "Job Alarms"]
DASHBOARD_HEADER_MOA_MULTI_AVG = ["Run_Previous", "Job Run avg"]


# inputs (single)
file_dir_Report_MOA = 'report.xlsx'
file_dir_OUT = 'dashboard_OUT.xlsx'
file_dir_OUT_pre = 'dashboard_OUT_pre.xlsx'
file_dir_Dashboard_MOA = 'AutosysMigration_dashboard2.xlsm'
Input_date_MOA = '2022-2-7'

# inputs (multi) from current week (1) to the sixth week(6)
file_dir_Draft_1 = 'dashboard_OUT_1'
file_dir_Draft_2 = 'dashboard_OUT_2'
file_dir_Draft_3 = 'dashboard_OUT_3'
file_dir_Draft_4 = 'dashboard_OUT_4'
file_dir_Draft_5 = 'dashboard_OUT_5'
file_dir_Draft_6 = 'dashboard_OUT_6'


Report_Dashboard_OUT = [[[file_dir_Report_MOA, {"sheet":SHEET_REPORT_MOA, "prefix":REPORT_PREFIX_MOA, "header":REPORT_HEADER_MOA[0]}], 
                       [file_dir_OUT, {"sheet":SHEET_DRAFT, "prefix":OUT_PREFIX, "header":OUT_HEADER[0]}]],

                       [[file_dir_Report_MOA, {"sheet":SHEET_REPORT_MOA, "prefix":REPORT_PREFIX_MOA, "header":REPORT_HEADER_MOA[1]}], 
                       [file_dir_OUT, {"sheet":SHEET_DRAFT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]}]],

                       [[file_dir_Report_MOA, {"sheet":SHEET_REPORT_MOA, "prefix":REPORT_PREFIX_MOA, "header":REPORT_HEADER_MOA[2]}], 
                       [file_dir_OUT, {"sheet":SHEET_DRAFT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]}]],

                       [[file_dir_Report_MOA, {"sheet":SHEET_REPORT_MOA, "prefix":REPORT_PREFIX_MOA, "header":REPORT_HEADER_MOA[3]}], 
                       [file_dir_OUT, {"sheet":SHEET_DRAFT, "prefix":OUT_PREFIX, "header":OUT_HEADER[3]}]]]


Dashboard_Draft = [[[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[0]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DRAFT, "prefix":DRAFT_PREFIX, "header":Input_date_MOA}]],

                    [[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DRAFT, "prefix":DRAFT_PREFIX, "header":Input_date_MOA}]],

                    [[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DRAFT, "prefix":DRAFT_PREFIX, "header":Input_date_MOA}]],

                    [[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[3]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DRAFT, "prefix":DRAFT_PREFIX, "header":Input_date_MOA}]]]


Dashboard_single = [[[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[0]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[0]}]],

                    [[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[3]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[1]}]],

                    [[file_dir_OUT_pre, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[0]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[2]}]],

                    [[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[3]}]],
                    
                    [[file_dir_OUT_pre, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[4]}]],
                    
                    [[file_dir_OUT, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[5]}]],
                    
                    [[file_dir_OUT_pre, {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[3]}], 
                    [file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_SINGLE[6]}]]]


Dashboard_multi_sum = [[[file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_MULTI_SUM[0]}],
                    {file_dir_Draft_2: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_3: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_4: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_5: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_6: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]}}],

                    [[file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_MULTI_SUM[1]}],
                    {file_dir_Draft_2: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]},
                    file_dir_Draft_3: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]},
                    file_dir_Draft_4: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]},
                    file_dir_Draft_5: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]},
                    file_dir_Draft_6: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[2]}}]]


Dashboard_multi_avg = [[[file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_MULTI_AVG[0]}],
                    {file_dir_Draft_2: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_3: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_4: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_5: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_6: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]}}],

                    [[file_dir_Dashboard_MOA, {"sheet":SHEET_DASHBOARD_MOA, "prefix":DASHBOARD_PREFIX_MOA, "header":DASHBOARD_HEADER_MOA_MULTI_AVG[1]}],
                    {file_dir_Draft_1: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_2: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_3: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_4: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]},
                    file_dir_Draft_5: {"sheet":SHEET_OUT, "prefix":OUT_PREFIX, "header":OUT_HEADER[1]}}]]


REPORT_MASTER = 'rm'
MASTER_DEV_UAT_PROD = 'mDUP'
MASTER_DASHBOARD = 'md'
MULTI_MASTER_DASHBOARD = 'mmd'

REPORT_DASHBOARD_OUT = 'rdo'
DASHBOARD_DRAFT = 'dd'
DASHBOARD_SINGLE = 'ds'
DASHBOARD_MULTI_SUM = 'dms'
DASHBOARD_MULTI_AVG = 'dma'

check_files = {
    REPORT_MASTER: report_master, 
    MASTER_DEV_UAT_PROD: master_DEV_UAT_PROD, 
    MASTER_DASHBOARD: master_dashboard, 
    MULTI_MASTER_DASHBOARD: multi_master_dashboard,
    REPORT_DASHBOARD_OUT: Report_Dashboard_OUT,
    DASHBOARD_DRAFT: Dashboard_Draft,
    DASHBOARD_SINGLE: Dashboard_single,
    DASHBOARD_MULTI_SUM: Dashboard_multi_sum,
    DASHBOARD_MULTI_AVG: Dashboard_multi_avg
    }