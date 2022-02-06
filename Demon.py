from Checker import Checker
from View import View
from Controller import Controller
import pandas as pd

from datetime import datetime as dt



def main():
    # view = View.get_instance()
    # checker = Checker
    # controller = Controller.get_instance(view, checker)

    # controller.run_checker_auto()

    # file_dir = "AutosysMigration_dashboard2.xlsm"
    # sheet = " DEV "
    # df = pd.read_excel(file_dir, sheet_name=sheet)
    # print(df)

    inDate = '2021-11-15 00:00:00'
    d = dt.strptime(inDate, "%Y-%m-%d %H:%M:%S")

    print(type(d))
    print(d)





    
main()