import pandas as pd
import os

f2 = pd.read_csv('no_add data.csv')

def transfer_frame(p_number, n, frame):
    #if int(p_number) > 3:
    #    return 0
    if int(p_number) < 10:
        fileName = os.path.join('frame','P0{}_{}.csv'.format(p_number, n))
    else:
        fileName = os.path.join('frame','P{}_{}.csv'.format(p_number, n))
    df = pd.read_csv(fileName, header = None)
    return df.loc[df[df.columns[1]] == frame].values[0][0]


f2['Starting Frame Num'] = f2.apply(lambda row: transfer_frame(row['Participant'],row['NbackLevel'],row['Starting Frame Num']), axis=1)
f2['Ending Frame Num'] = f2.apply(lambda row: transfer_frame(row['Participant'],row['NbackLevel'],row['Ending Frame Num']), axis=1)
f2.to_csv('no_add data_cleaned.csv',index=False)