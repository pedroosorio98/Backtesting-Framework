import pandas as pd

def rets_yearly_returns(rets):
    if isinstance(rets,pd.DataFrame) or isinstance(rets,pd.Series):
        return pd.DataFrame(((rets.groupby(rets.index.year).apply(cummulated_returns))*100).round(2),columns=["Returns"])
    else:
        raise TypeError("This function is supposed to receive a pd.DataFrame object.")
        
        
def fill_between(base):
        first = base.first_valid_index()
        last = base.last_valid_index()
        base.loc[first:last] = base.loc[first:last].fillna(method="ffill")
        return base
        
def cummulated_returns(rets):
    if isinstance(rets,pd.Series) or isinstance(rets,pd.DataFrame):
        return rets.add(1).prod()-1
    else: 
        raise TypeError("This function is supposed to receive a pd.DataFrame or pd.Series object.")