import pandas as pd
import time
import datetime
import math
file = pd.read_csv("./clean_eye_tree.csv", encoding = 'utf-8')
df = file
da = df.to_dict(orient='records') #type is list
# # 4->5
# new_data = {'ID':[], 'Age':[]}
# for i in range(5):
#     col = 'year{}'.format(i)
#     new_data[col + 'left'] = []
#     new_data[col + 'right'] = []
# for record in da:
#     if ((record['year4left'] != 'NULL') and (record['year4right']) != 'NULL' and (math.isnan(record['year4left']) == False) and (math.isnan(record['year4right']) == False) ):
#         new_data['ID'].append(record['ID'])
#         new_data['Age'].append(record['Age'])
#         new_data['year0left'].append(record['year0left'])
#         new_data['year0right'].append(record['year0right'])
#         new_data['year1left'].append(record['year1left'])
#         new_data['year1right'].append(record['year1right'])
#         new_data['year2left'].append(record['year2left'])
#         new_data['year2right'].append(record['year2right'])
#         new_data['year3left'].append(record['year3left'])
#         new_data['year3right'].append(record['year3right'])
#         new_data['year4left'].append(record['year4left'])
#         new_data['year4right'].append(record['year4right'])
# #写入csv
# dw = pd.DataFrame(new_data, columns=['ID', 'Age', 'year0left', 'year0right', 'year1left', 'year1right', 'year2left', 'year2right', 'year3left', 'year3right', 'year4left', 'year4right'])
# dw.to_csv("./4to5.csv", index=False)


# 5 -> 6
new_data = {'ID':[], 'Age':[]}
for i in range(6):
    col = 'year{}'.format(i)
    new_data[col + 'left'] = []
    new_data[col + 'right'] = []
for record in da:
    if (record['year5left'] != 'NULL' and record['year5right'] != 'NULL' and (math.isnan(record['year5left']) == False) and (math.isnan(record['year5right']) == False)) :
        new_data['ID'].append(record['ID'])
        new_data['Age'].append(record['Age'])
        new_data['year0left'].append(record['year0left'])
        new_data['year0right'].append(record['year0right'])
        new_data['year1left'].append(record['year1left'])
        new_data['year1right'].append(record['year1right'])
        new_data['year2left'].append(record['year2left'])
        new_data['year2right'].append(record['year2right'])
        new_data['year3left'].append(record['year3left'])
        new_data['year3right'].append(record['year3right'])
        new_data['year4left'].append(record['year4left'])
        new_data['year4right'].append(record['year4right'])
        new_data['year5left'].append(record['year5left'])
        new_data['year5right'].append(record['year5right'])
#写入csv
dw = pd.DataFrame(new_data, columns=['ID', 'Age', 'year0left', 'year0right', 'year1left', 'year1right', 'year2left', 'year2right', 'year3left', 'year3right', 'year4left', 'year4right', 'year5left', 'year5right'])
dw.to_csv("./5to6.csv", index=False)