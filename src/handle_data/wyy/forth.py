# 这里要干的是把前几年的不为空的数据提出来
import pandas as pd

file = open('data/clean_eye_tree.csv', 'r', encoding='utf-8', errors='ignore')
data_row = []
data_clean_list = []
m = 7
# 年数
n = 0
line = file.readline()
data = line.split(',')
data_row.append(data[0])
data_row.append(data[1])
while n < m:
    data_row.append(data[2*n+2])
    data_row.append(data[2*n+3])
    n = n + 1
n = 0
data_clean_list.append(data_row)
data_row = []
while True:
    line = file.readline()
    if not line:
        break
    data = line.split(',')
    while n < m:
        if (data[2*n+2] == "NULL") and (data[2*n+3] == "NULL"):
            break
        n = n + 1
    if n == m:
        data_row.append(data[0])
        data_row.append(data[1])
        n = 0
        while n < m:
            data_row.append(data[2 * n + 2])
            data_row.append(data[2 * n + 3])
            n = n + 1
        data_clean_list.append(data_row)
        data_row = []
    n = 0

test = pd.DataFrame(data=data_clean_list)
test.to_csv('data/hh_eye.csv', encoding='utf-8', index=False, header=False)