import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    if len(weather)<=1:
        return pd.DataFrame(columns=["Id"])
    weather.sort_values(by="recordDate",ignore_index=True,inplace=True)
    tem=weather["temperature"]
    ids=weather["id"]
    pst=[]
    for j in range(1,len(weather)):
        answer=(weather.iloc[j]["recordDate"]-weather.iloc[j-1]["recordDate"]).days
        pst.append(answer)
    print(pst)
    lst=[]
    for value in range(1,len(tem)):
        if tem[value-1]<tem[value] and pst[value-1]==1:
            lst.append(ids[value])
    print(lst)
    if not lst:
        return pd.DataFrame(columns=["Id"])
    else:
        return pd.DataFrame({"Id":lst})
    