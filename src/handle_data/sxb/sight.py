import pandas as pd
import time
import datetime
def cal_time(date1, date2):
    date1 = time.strptime(date1, "%Y/%m/%d")
    date2 = time.strptime(date2, "%Y/%m/%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return date2 - date1
def add_record(new_record):
    new_data['ID'].append(new_record['ID'])
    new_data['Age'].append(new_record['Age'])
    length = len(new_record['left'])
    for i in range(9):
        col = 'year{}'.format(i)
        if i <= (length - 1):
            new_data[col + 'left'].append(new_record['left'][i])
            new_data[col + 'right'].append(new_record['right'][i])
        else:
            new_data[col + 'left'].append('NULL')
            new_data[col + 'right'].append('NULL')
file = pd.read_csv("./data.csv", encoding = 'utf-8')
# df = file.head(140)
df = file
da = df.to_dict(orient='records') #type is list
new_data = {'ID':[], 'Age':[]}
for i in range(9):
    col = 'year{}'.format(i)
    new_data[col + 'left'] = []
    new_data[col + 'right'] = []
lastId = da[0]['S_OP_IP_Cus']
lastTime = da[0]['S_OP_IP_Che']
lastLeftDegree = da[0]['Eq_Degree']
lastRightDegree = da[0]['Eq_Degree1']
new_record = {}
for record in da:
    if record['S_OP_IP_Cus'] != lastId:
        add_record(new_record)
        new_record = {}
        lastId = record['S_OP_IP_Cus']
    if ('ID' in new_record) == False:
        new_record['ID'] = record['S_OP_IP_Cus']
        new_record['Age'] = record['Age']
        new_record['left'] = []
        new_record['right'] = []
    interval = cal_time(lastTime, record['S_OP_IP_Che'])
    lastTime = record['S_OP_IP_Che']
    number = (interval.days - 180) // 360
    if number > 0:
        addLeft = round(((record['Eq_Degree'] - lastLeftDegree) / (number + 1)), 3)
        addRight = round(((record['Eq_Degree1'] - lastRightDegree) / (number + 1)), 3)
    for i in range(number):
        new_record['left'].append(round((lastLeftDegree + (i + 1) * addLeft), 3))
        new_record['right'].append(round((lastRightDegree + (i + 1) * addRight), 3))
    lastLeftDegree = round(record['Eq_Degree'], 3)
    lastRightDegree = round(record['Eq_Degree1'], 3)
    new_record['left'].append(round(record['Eq_Degree'], 3))
    new_record['right'].append(round(record['Eq_Degree1'], 3))

#写入csv
dw = pd.DataFrame(new_data, columns=['ID', 'Age', 'year0left', 'year0right', 'year1left', 'year1right', 'year2left', 'year2right', 'year3left', 'year3right', 'year4left', 'year4right', 'year5left', 'year5right', 'year6left', 'year6right', 'year7left', 'year7right', 'year8left', 'year8right'])
dw.to_csv("./clean_eye_tree.csv", index=False)



# S_OP_IP_Cus S_OP_IP_Che S_ME_CI_Nam S_ME_CI_Sex S_ME_CI_Bir S_OP_IP_Bal S_OP_IP_Bal1 S_OP_IP_Pos S_OP_IP_Pos1 Eq_Degree Eq_Degree1
