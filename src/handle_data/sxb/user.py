import pandas as pd
import time
import datetime
file = pd.read_csv("./data.csv", encoding = 'utf-8')
# df = file.head(140)
df = file
da = df.to_dict(orient='records') #type is list
new_data = {'ID':[], 'S_OP_IP_Cus':[], 'S_ME_CI_Nam':[], 'S_ME_CI_Sex':[], 'S_ME_CI_Bir':[], 'S_ME_CI_PW':[]}
i = 1
for record in da:
    if len(new_data['S_OP_IP_Cus']) == 0:
        new_data['ID'].append(i)
        i += 1
        new_data['S_OP_IP_Cus'].append(record['S_OP_IP_Cus'])
        new_data['S_ME_CI_Nam'].append(record['S_ME_CI_Nam'])
        new_data['S_ME_CI_Sex'].append(record['S_ME_CI_Sex'])
        new_data['S_ME_CI_Bir'].append(record['S_ME_CI_Bir'])
        new_data['S_ME_CI_PW'].append('123')
    else:
        if record['S_OP_IP_Cus'] ==  new_data['S_OP_IP_Cus'][-1]:
            continue
        new_data['ID'].append(i)
        i += 1
        new_data['S_OP_IP_Cus'].append(record['S_OP_IP_Cus'])
        new_data['S_ME_CI_Nam'].append(record['S_ME_CI_Nam'])
        new_data['S_ME_CI_Sex'].append(record['S_ME_CI_Sex'])
        new_data['S_ME_CI_Bir'].append(record['S_ME_CI_Bir'])
        new_data['S_ME_CI_PW'].append('123')
#写入csv
dw = pd.DataFrame(new_data, columns=['ID', 'S_OP_IP_Cus', 'S_ME_CI_Nam', 'S_ME_CI_Sex', 'S_ME_CI_Bir', 'S_ME_CI_PW'])
dw.to_csv("./user.csv", index=False, encoding="utf_8_sig")



# S_OP_IP_Cus S_OP_IP_Che S_ME_CI_Nam S_ME_CI_Sex S_ME_CI_Bir S_OP_IP_Bal S_OP_IP_Bal1 S_OP_IP_Pos S_OP_IP_Pos1 Eq_Degree Eq_Degree1
