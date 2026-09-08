import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary",inplace=True)
    employee.sort_values(by="salary",ascending=False,inplace=True)
    if len(employee)<=1:
        return pd.DataFrame([[None]],columns=["SecondHighestsalary"])
    salary=employee.iloc[1]["salary"]
    new_df=pd.DataFrame([[salary]],columns=["SecondHighestSalary"])
    return new_df

    