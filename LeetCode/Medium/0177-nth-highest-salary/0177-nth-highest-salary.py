import pandas as pd

def nth_highest_salary(emp: pd.DataFrame, N: int) -> pd.DataFrame:
    emp.drop_duplicates("salary",keep="first",inplace=True)
    emp.sort_values(by="salary",ascending=False,inplace=True)
    if len(emp)<N or N<=0:
        return pd.DataFrame([[None]],columns=[f"getNthHighestSalary({N})"])
    salary=emp.iloc[N-1]["salary"]
    new_df=pd.DataFrame([[salary]],columns=[f"getNthHighestSalary({N})"])
    return new_df
    