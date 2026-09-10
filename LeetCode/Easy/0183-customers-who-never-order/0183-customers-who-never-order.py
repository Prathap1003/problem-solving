import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    values=orders['customerId']
    df=customers[~customers['id'].isin(values)]
    return pd.DataFrame({'Customers':df['name']})