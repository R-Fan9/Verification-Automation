from time import strptime
from Checker import Checker
from View import View
from Controller import Controller
import pandas as pd
from datetime import datetime as dt

def main():
    
    view = View.get_instance()
    checker = Checker
    controller = Controller.get_instance(view, checker)

    controller.run_checker_auto()
    '''
    file_dir = "AutosysMigration_dashboard2.xlsm"
    sheet = "AutoSysDashboard"
    df = pd.read_excel(file_dir, sheet_name=sheet, header=1)
    col = df.columns[24]
    print(col)
    '''
    
main()