from Checker import Checker
from View import View
from Controller import Controller

def main():
    view = View.get_instance()
    checker = Checker
    controller = Controller.get_instance(view, checker)

    controller.run_checker()
    
main()