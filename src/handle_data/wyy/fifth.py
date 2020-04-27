# 统计信息
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
    female = 0
    male = 0
    # 男女数量统计
    kid = 0
    # <=12
    child = 0
    # 12~18
    teenager = 0
    # 18~24
    adult = 0
    # >24
    # 年龄分布
    num = {}
    sum_Bal = {}
    sum_Bal1 = {}
    sum_Axe = {}
    sum_Axe1 = {}
    sum_Pos = {}
    sum_Pos1 = {}
    # 统计平均值
    file = open('data/clean_eye.csv', 'r', encoding='utf-8', errors='ignore')
    line = file.readline()
    data = line.strip().split(',')
    last_cus = data[0]
    if data[3] == '1':
        female += 1
    elif data[3] == '0':
        male += 1
    if is_date(data[1]) and is_date(data[4]):
        calculate = Caltime(data[4], data[1])
        if calculate.days <= (12 * 365):
            kid += 1
        elif calculate.days <= (18 * 365):
            child += 1
        elif calculate.days <= (24 * 365):
            teenager += 1
        elif calculate.days > (24 * 365):
            adult += 1
        age = calculate.days//365
        if age in num:
            num[age] += 1
            sum_Bal[age] += float(data[5])
            sum_Bal1[age] += float(data[6])
            sum_Axe[age] += float(data[7])
            sum_Axe1[age] += float(data[8])
            sum_Pos[age] += float(data[9])
            sum_Pos1[age] += float(data[10])
        else:
            num[age] = 1
            sum_Bal[age] = float(data[5])
            sum_Bal1[age] = float(data[6])
            sum_Axe[age] = float(data[7])
            sum_Axe1[age] = float(data[8])
            sum_Pos[age] = float(data[9])
            sum_Pos1[age] = float(data[10])
    while True:
        line = file.readline()
        if not line:
            break
        data = line.strip().split(',')
        if data[0] != last_cus:
            last_cus = data[0]
            if data[3] == '1':
                female += 1
            elif data[3] == '0':
                male += 1
            if is_date(data[1]) and is_date(data[4]):
                calculate = Caltime(data[4], data[1])
                if calculate.days <= (12 * 365):
                    kid += 1
                elif calculate.days <= (18 * 365):
                    child += 1
                elif calculate.days <= (24 * 365):
                    teenager += 1
                elif calculate.days > (24 * 365):
                    adult += 1
                age = calculate.days // 365
                if age in num:
                    num[age] += 1
                    sum_Bal[age] += float(data[5])
                    sum_Bal1[age] += float(data[6])
                    sum_Axe[age] += float(data[7])
                    sum_Axe1[age] += float(data[8])
                    sum_Pos[age] += float(data[9])
                    sum_Pos1[age] += float(data[10])
                else:
                    num[age] = 1
                    sum_Bal[age] = float(data[5])
                    sum_Bal1[age] = float(data[6])
                    sum_Axe[age] = float(data[7])
                    sum_Axe1[age] = float(data[8])
                    sum_Pos[age] = float(data[9])
                    sum_Pos1[age] = float(data[10])
    data_row = ['Age', 'Bal', 'Bal1', 'Axe', 'Axe1', 'Pos', 'Pos1']
    data_tj_list = []
    data_tj_list.append(data_row)
    data_row = []
    for i in sorted(num):
        data_row.append(i)
        data_row.append(sum_Bal[i]/num[i])
        data_row.append(sum_Bal1[i]/num[i])
        data_row.append(sum_Axe[i]/num[i])
        data_row.append(sum_Axe1[i]/num[i])
        data_row.append(sum_Pos[i]/num[i])
        data_row.append(sum_Pos1[i]/num[i])
        data_tj_list.append(data_row)
        data_row = []

    test = pd.DataFrame(data=data_tj_list)
    test.to_csv('data/tj_data.csv', encoding='utf-8', index=False, header=False)

    f = open('data/tj.txt', 'w', encoding='utf-8', errors='ignore')
    f.write('男：' + str(male) + '\n')
    f.write('女：' + str(female) + '\n')
    f.write('0~12:' + str(kid) + '\n')
    f.write('12~18:' + str(child) + '\n')
    f.write('18~24:' + str(teenager) + '\n')
    f.write('24以上:' + str(adult))

