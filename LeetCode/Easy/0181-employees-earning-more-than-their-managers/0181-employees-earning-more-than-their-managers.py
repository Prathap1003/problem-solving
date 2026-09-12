import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager=employee[['id','salary']].rename(columns={'id':'manager_id','salary':'manager_salary'})
    merged=pd.merge(employee,manager,left_on='managerId',right_on='manager_id')
    return pd.DataFrame({'Employee':merged[merged['salary']>merged['manager_salary']]['name']})

    