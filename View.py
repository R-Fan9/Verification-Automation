class View:

    __ui = None

    @staticmethod 
    def get_instance():
        if View.__ui is None:
            View()
        return View.__ui

    def __init__(self):
        if View.__ui is not None:
            raise Exception("This is a Singleton class")
        else:
            View.__ui = self

    def print_file_prompt(self):
        print("Please enter file directory: ")

    def print_sheet_prompt(self):
        print("Please enter the sheet name: ")

    def print_prefix_header(self):
        print("Please enter the name of prefix header: ")

    def print_header_prompt(self):
        print("Please enter the name of header: ")
    
    def print_mode_prompt(self):
        print("Please select mode single(s) or multi(m): ")
    
    def print_func_prompt(self):
        print("Please select func sum(s) or avg(a): ")

    def print_df(self, df):
        print(df)
