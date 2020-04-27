# 重复的数据随机选择一个保存
import pandas as pd
import datetime
import random

file = open('data/clean_eye.csv', 'r', encoding='utf-8', errors='ignore')
line = file.readline()
data_row = []
data_clean_list = []
last_Cus = ""
last_Che = ""
data_same_list = []
num = 0

while True:
    line = file.readline()
    if not line:
        break
    data = line.strip().split(',')
    if last_Cus != data[0] or (last_Che != data[1] and last_Cus == data[0]):
        if len(data_row) != 0:
            data_clean_list.append(data_row)
            data_row = []
        data_row.append(data[0])
        data_row.append(data[1])
        data_row.append(data[2])
        data_row.append(data[3])
        data_row.append(data[4])
        data_row.append(data[5])
        data_row.append(data[6])
        data_row.append(data[7])
        data_row.append(data[8])
        data_row.append(data[9])
        data_row.append(data[10])
        last_Cus = data[0]
        last_Che = data[1]
    else:
        while last_Che == data[1] and last_Cus == data[0]:
            data_same_list.append(data_row)
            num = num + 1
            data_row = []
            data_row.append(data[0])
            data_row.append(data[1])
            data_row.append(data[2])
            data_row.append(data[3])
            data_row.append(data[4])
            data_row.append(data[5])
            data_row.append(data[6])
            data_row.append(data[7])
            data_row.append(data[8])
            data_row.append(data[9])
            data_row.append(data[10])
            last_Che = data[1]
            last_Cus = data[0]
            line = file.readline()
            data = line.strip().split(',')
        data_same_list.append(data_row)
        data_row = []
        data_row.append(data[0])
        data_row.append(data[1])
        data_row.append(data[2])
        data_row.append(data[3])
        data_row.append(data[4])
        data_row.append(data[5])
        data_row.append(data[6])
        data_row.append(data[7])
        data_row.append(data[8])
        data_row.append(data[9])
        data_row.append(data[10])
        num = random.randint(0, num)
        data_clean_list.append(data_same_list[num])
        num = 0
        data_same_list = []

test = pd.DataFrame(data=data_clean_list)
test.to_csv('data/clean_clean_eye.csv', encoding='utf-8', index=False, header=False)

# import pandas as pd
# import datetime
#
# file = open('clean_eye.csv', 'r', encoding='utf-8', errors='ignore')
# line = file.readline()
# last_Cus = ""
# last_Che = ""
# last_Bal = ""
# last_Bal1 = ""
# last_Pos = ""
# last_Pos1 = ""
#
# while True:
#     line = file.readline()
#     data = line.strip().split(',')
#     Cus = data[0]
#     Che = data[1]
#     Bal = data[5]
#     Bal1 = data[6]
#     Pos = data[9]
#     Pos1 = data[10]
#     Che = datetime.datetime.strptime(Che, "%Y/%m/%d")