import utils as ut

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
        print("Please select func {} or {}: ".format(ut.COL_SUM, ut.COL_AVG))

    def print_file_names(self, f_names):
        print(' vs '.join(f_names))
    
    def print_df(self, df):
        print(df)

    def out_file(self, df, file_name, sheet_name):
        df.to_excel(file_name, sheet_name, index=False)
