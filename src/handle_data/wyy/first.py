# 主要是将不对的轴位数据改为零，表示未检查
# 将错误的置为0表示未检查
import pandas as pd

file = open('data/eye_data.csv', 'r', encoding='utf-8', errors='ignore')
line = file.readline()
Axe_list = []
Axe1_list = []
last_Cus = ""
last_Che = ""
last_Axe = ""
last_Axe1 = ""
data_list = []
data_error_list = []
data_same_list = []

while True:
    line = file.readline()
    if not line:
        break
    data = line.strip().split(',')
    Cus = data[0]
    Che = data[1]
    Axe = data[7]
    Axe1 = data[8]
    if last_Cus != Cus:
        # 根据范围，据我观察，轴位要不小于90，要不大于90，等于90的归小于90管
        large_Axe = False
        large_Axe1 = True
        large = 0
        small = 0
        for i in Axe_list:
            if int(i) > 90:
                large = large + 1
            else:
                small = small + 1
        if large > small:
            large_Axe = True
        else:
            large_Axe = False

        large = 0
        small = 0
        for i in Axe1_list:
            if int(i) > 90:
                large = large + 1
            else:
                small = small + 1
        if large > small:
            large_Axe1 = True
        else:
            large_Axe1 = False
        for i in range(len(data_same_list)):
            if (large_Axe and (int(data_same_list[i][2]) < 90)) or (not large_Axe and (int(data_same_list[i][2]) > 90)):
                data_same_list[i][2] = "0"
                data_error_list.append(data_same_list[i])
            elif (large_Axe1 and (int(data_same_list[i][3]) < 90)) or (not large_Axe1 and (int(data_same_list[i][3]) > 90)):
                data_same_list[i][3] = "0"
                data_error_list.append(data_same_list[i])
        data_same_list = []
        Axe_list = []
        Axe1_list = []
        data_list.append(Cus)
        data_list.append(Che)
        data_list.append(Axe)
        data_list.append(Axe1)
        data_same_list.append(data_list)
        last_Cus = Cus
        last_Che = Che
        last_Axe = Axe
        last_Axe1 = Axe1
        Axe_list.append(Axe)
        Axe1_list.append(Axe1)
        data_list = []

        # # 根据出现次数最多的来判断当前值是否正确
        # a = {}
        # for i in Axe_list:
        #     if i in a:
        #         a[i] = a[i]+1
        #     else:
        #         a[i] = 1
        # b = sorted(a, reverse=True)
        # if len(b) > 0:
        #     most_Axe = int(b[0])
        # a = {}
        # for i in Axe1_list:
        #     if i in a:
        #         a[i] = a[i]+1
        #     else:
        #         a[i] = 1
        # b = sorted(a, reverse=True)
        # if len(b) > 0:
        #     most_Axe1 = int(b[0])
        # for i in range(len(data_same_list)):
        #     if (int(data_same_list[i][2]) - most_Axe) > 50 or (int(data_same_list[i][2]) - most_Axe) < -50:
        #         data_same_list[i][2] = "0"
        #         data_error_list.append(data_same_list[i])
        #     elif (int(data_same_list[i][3]) - most_Axe1) > 50 or (int(data_same_list[i][3]) - most_Axe1) < -50:
        #         data_same_list[i][3] = "0"
        #         data_error_list.append(data_same_list[i])
        # data_same_list = []
        # Axe_list = []
        # Axe1_list = []
        # data_list.append(Cus)
        # data_list.append(Che)
        # data_list.append(Axe)
        # data_list.append(Axe1)
        # data_same_list.append(data_list)
        # last_Cus = Cus
        # last_Che = Che
        # last_Axe = Axe
        # last_Axe1 = Axe1
        # Axe_list.append(Axe)
        # Axe1_list.append(Axe1)
        # data_list = []
    elif last_Che != Che or (last_Che == Che and (last_Axe != Axe or last_Axe1 != Axe1)):
        Axe_list.append(Axe)
        Axe1_list.append(Axe1)
        data_list.append(Cus)
        data_list.append(Che)
        data_list.append(Axe)
        data_list.append(Axe1)
        data_same_list.append(data_list)
        data_list = []
        last_Che = Che
        last_Axe = Axe
        last_Axe1 = Axe1
    else:
        data_list.append(Cus)
        data_list.append(Che)
        data_list.append(Axe)
        data_list.append(Axe1)
        data_same_list.append(data_list)
        data_list = []
        last_Che = Che


file.close()
file = open('data/eye_data.csv', 'r', encoding='utf-8', errors='ignore')

data_clean_list = []
data_row = []
line = file.readline()
data = line.strip().split(',')
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
i = -1
while True:
    i = i + 1
    line = file.readline()
    if not line:
        break
    data = line.strip().split(',')
    if i < len(data_error_list) and data_error_list[i][0] == data[0] and data_error_list[i][1] == data[1]:
        data_row.append(data[0])
        data_row.append(data[1])
        data_row.append(data[2])
        data_row.append(data[3])
        data_row.append(data[4])
        data_row.append(data[5])
        data_row.append(data[6])
        data_row.append(data_error_list[i][2])
        data_row.append(data_error_list[i][3])
        data_row.append(data[9])
        data_row.append(data[10])
        data_clean_list.append(data_row)
        data_row = []
    else:
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
        i = i - 1

test = pd.DataFrame(data = data_clean_list)
test.to_csv('data/clean_eye.csv', encoding='utf-8', index=False, header=False)



# 加载数据
# eye_data_file = 'data/clean_data.csv'
# eye_data = pd.read_csv(eye_data_file)
#
# S_OP_IP_Cus = []
# S_OP_IP_Che = []
# S_ME_CI_Nam = []
# S_OP_IP_Axe = []
# S_OP_IP_Axe_Num = []
# S_OP_IP_Axe1 = []
# S_OP_IP_Axe1_Num = []
# S_OP_IP_Pos = []
# S_OP_IP_Pos1 = []
# S_OP_IP_Bal = []
# S_OP_IP_Bal1 = []
# temp_Cus = ""
# temp_Che = ""
# temp_num = 0
# all_list = []
#
# print(eye_data)
# for i in range(len(eye_data)):
#     Cus = eye_data["S_OP_IP_Cus"][i+1]
#
#     Che = eye_data["S_OP_IP_Che"][i+1]
#     # Nam = eye_data["S_ME_CI_Nam"][i+1]
#     # Sex = eye_data["S_ME_CI_Sex"][i+1]
#     # Bir = eye_data["S_ME_CI_Bir"][i+1]
#     # Bal = eye_data["S_OP_IP_Bal"][i+1]
#     # Bal1 = eye_data["S_OP_IP_Bal1"][i+1]
#     Axe = eye_data["S_OP_IP_Axe"][i+1]
#     Axe1 = eye_data["S_OP_IP_Axe1"][i+1]
#     # Pos = eye_data["S_OP_IP_Pos"][i+1]
#     # Pos1 = eye_data["S_OP_IP_Pos1"][i+1]
#     print(Cus)









