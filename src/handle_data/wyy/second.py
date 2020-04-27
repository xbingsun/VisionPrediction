# 这里干的是把同一个人检查日期在半年内的删掉，按年分，没有的补空值
import time
import pandas as pd
import datetime


def Caltime(date1, date2):
    date1 = time.strptime(date1, "%Y/%m/%d")
    date2 = time.strptime(date2, "%Y/%m/%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return date2-date1

def is_date(str):
    try:
        time.strptime(str, "%Y/%m/%d")
        return True
    except:
        return False

if __name__ == '__main__':
    file = open('data/clean_clean_eye.csv', 'r', encoding='utf-8', errors='ignore')
    line = file.readline()
    data = line.strip().split(',')
    last_cus = data[0]
    last_date = data[1]
    data_row = []
    data_clean_list = []
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
    data_clean_list.append(data_row)
    data_row = []
    data_null = []
    while True:
        line = file.readline()
        if not line:
            break
        data = line.strip().split(',')
        cur_cus = data[0]
        cur_date = data[1]
        if cur_cus != last_cus:
            last_cus = cur_cus
            last_date = cur_date
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
            data_clean_list.append(data_row)
            data_row = []
            continue
        else:
            if is_date(cur_date) and is_date(last_date):
                calculate = Caltime(last_date, cur_date)
                if calculate.days < 180:
                    continue
                else:
                    insert_null = (calculate.days - 180)//360
                    while insert_null != 0:
                        data_null.append(data[0])
                        data_null.append('NULL')
                        data_null.append(data[2])
                        data_null.append(data[3])
                        data_null.append(data[4])
                        data_null.append('NULL')
                        data_null.append('NULL')
                        data_null.append('NULL')
                        data_null.append('NULL')
                        data_null.append('NULL')
                        data_null.append('NULL')
                        data_clean_list.append(data_null)
                        insert_null = insert_null - 1
                        data_null = []
                    # if (calculate.days >= 180) and (calculate.days <= 540):
                    last_cus = cur_cus
                    last_date = cur_date
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
                    data_clean_list.append(data_row)
                    data_row = []
                        # continue
                    # else:

    test = pd.DataFrame(data=data_clean_list)
    test.to_csv('data/che_eye.csv', encoding='utf-8', index=False, header=False)

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


# # ��Ҫ�ǰ�������¼���ĸ���������
# # �����۷ֱ�鿴��һ�����ݺ���һ�����������������ݵľ���ֵ֮�ͣ�����Ҫ���Ĵ�,��Ҫ��������һ���ģ�������
#
# import pandas as pd
#
# file = open('clean_eye.csv', 'r', encoding='utf-8', errors='ignore')
# line = file.readline()
# last_Cus = ""
# last_Che = ""
# last_Bal = ""
# last_Bal1 = ""
# last_Pos = ""
# last_Pos1 = ""
# last_last_Cus = ""
# last_last_Che = ""
# last_last_Bal = ""
# last_last_Bal1 = ""
# last_last_Pos = ""
# last_last_Pos1 = ""
# row_data = []
# same_data = []
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
#     # if last_Cus == Cus:
#


