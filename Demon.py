from Checker import Checker
from View import View
from Controller import Controller
from datetime import datetime as dt
import pandas as pd

def main():
    '''
    view = View.get_instance()
    checker = Checker
    controller = Controller.get_instance(view, checker)

    controller.run_checker_auto()
    '''
    file_dir = "AutosysMigration_dashboard2.xlsm"
    sheet = "DRAFT-MOA"
    df = pd.read_excel(file_dir, sheet_name=sheet, header=0)
    print(df)

main()