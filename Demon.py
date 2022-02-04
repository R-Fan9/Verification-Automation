from Checker import Checker
from View import View
from Controller import Controller
import pandas as pd

def main():

    df = pd.read_excel('AutosysMigration_dashboard2.xlsm', sheet_name='DEV')

    df = df[['Prefix', '2022-01-10']]

    print(df)


    # view = View.get_instance()
    # checker = Checker
    # controller = Controller.get_instance(view, checker)

    # controller.run_checker()
    
main()