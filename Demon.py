from Checker import Checker
from View import View
from Controller import Controller
from datetime import datetime as dt

def main():
    view = View.get_instance()
    checker = Checker
    controller = Controller.get_instance(view, checker)

    controller.run_checker_auto()

main()