import pandas as pd
from .minorfunc import split_comma, count_ppl

def transformResult(df):
    
    df['for'] = df['for'].apply(split_comma)
    df['ppl'] = df['for'].apply(count_ppl)
    df['divided_amount'] = df['amount']/df['ppl']
    df_ex = df.explode('for', ignore_index=True)

    corrected_list = []
    for i in range(df_ex.shape[0]):
        if df_ex['paid'][i] == df_ex['for'][i]:
            corrected_list.append(0)
        else:
            corrected_list.append(df_ex['divided_amount'][i])

    df_ex['divided_amount'] = corrected_list
    df_pivot = pd.pivot_table(df_ex, index='paid', columns='for', values='divided_amount', aggfunc='sum', fill_value=0)
    
    full_list = []
    for i in df_pivot.index:
        row_result = []
        for j in df_pivot.columns:
            if i==j:
                row_result.append(0)
            else:
                try:
                    num = df_pivot.loc[i,j] - df_pivot.loc[j,i]
                    row_result.append(num)
                except:
                    row_result.append(df_pivot.loc[i,j])
        full_list.append(row_result)

    result = pd.DataFrame(full_list, columns=df_pivot.columns, index=df_pivot.index)
    
    return result

df = pd.read_excel('sharedExpenses.xlsx')
print(transformResult(df))