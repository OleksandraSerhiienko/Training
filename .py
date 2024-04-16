import pandas as pd
def readfile(salaries):
    salaries = pd.read_csv("/Users/oleksandrasergienko/Training/Training/Employee_Salaries.csv")
    pyth_lst = salaries.values.tolist()
    return pyth_lst
