import pandas as pd
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values('score',ascending=False,inplace=True)
    score=scores['score']
    dic={}
    i=1
    rank=[]
    for val in score:
        if val in dic:
            rank.append(dic[val])
            continue
        else:
            dic[val]=i
            rank.append(dic[val])
            i+=1
    return pd.DataFrame({'score':score,'rank':rank})