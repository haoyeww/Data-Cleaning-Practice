import pandas as pd
import os

def generate_ID(p, s):
    if p < 10:
        return '0{}{}'.format(p,s)
    else:
        return '{}{}'.format(p,s)
    
df = pd.read_csv('no_add data_cleaned.csv')
df['ID'] = df.apply(lambda row: generate_ID(row['Participant'],row['NbackLevel']),  axis=1)
starting = df.groupby('ID')['Starting Frame Num'].apply(list).to_dict()
ending = df.groupby('ID')['Ending Frame Num'].apply(list).to_dict()

df2 = pd.read_csv('data.csv', converters={'p_number': lambda x: str(x)})
df2['ID'] = df2['p_number']+ df2['stage'].astype(str)
grouped = df2.groupby('ID')
df3 = pd.DataFrame()
for name, group in grouped:
    startFrames = starting[name]
    endFrames = ending[name]
    group = group[((group['FRAME_NUM'] > startFrames[0]) & (group['FRAME_NUM'] < endFrames[0])) |
                  ((group['FRAME_NUM'] > startFrames[1]) & (group['FRAME_NUM'] < endFrames[1])) |
                  ((group['FRAME_NUM'] > startFrames[2]) & (group['FRAME_NUM'] < endFrames[2])) |
                  ((group['FRAME_NUM'] > startFrames[3]) & (group['FRAME_NUM'] < endFrames[3]))]
    print(len(group))
    df3 = df3.append(group)
df3.to_csv('result.csv',index=False)