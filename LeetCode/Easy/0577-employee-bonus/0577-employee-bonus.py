import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    employee=employee.merge(bonus,on='empId',how='left')
    result=employee[(employee['bonus']<1000) | (employee['bonus'].isna())][['name','bonus']]
    return result