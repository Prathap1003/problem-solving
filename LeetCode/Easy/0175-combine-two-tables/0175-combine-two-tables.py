import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged=pd.merge(person,address,how="left",left_on="personId",right_on="personId")[["firstName","lastName","city","state"]]
    return merged
    