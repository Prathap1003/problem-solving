import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    new_df=orders.groupby('customer_number')['order_number'].count().reset_index()
    print(new_df)
    return new_df.loc[[new_df['order_number'].idxmax()],['customer_number']]