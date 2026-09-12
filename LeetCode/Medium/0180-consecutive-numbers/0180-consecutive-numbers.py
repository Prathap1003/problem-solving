import pandas as pd
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    nums=logs['num']
    lst=set()
    count=1
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            count+=1
            if count==3:
                lst.add(nums[i])
        else:
            count=1
    return pd.DataFrame({'ConsecutiveNums':list(lst)})
