from django.shortcuts import render
from user.models import *
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import logging
import time
import datetime
from sklearn.externals import joblib
from PROPATH import PROJECT
import math
def cal_time(date1, date2):
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return date2 - date1
def login_user(request):
    if request.method == 'GET':
        user_name = request.GET.get('username', None)
        user_password = request.GET.get('password', None)
        user = User.objects.filter(S_ME_CI_Nam=user_name)
        search_result = json.loads(serializers.serialize(
          'json', user, ensure_ascii=False))
        if search_result:
            check_pass = search_result[0]['fields']['S_ME_CI_PW']
        else:
            return HttpResponse('loginUserFailed')
        if check_pass == user_password:
            return HttpResponse('loginUserSuccess')
    return HttpResponse('loginUserFailed')
def login_admin(request):
    if request.method == 'GET':
        user_name = request.GET.get('username', None)
        user_password = request.GET.get('password', None)
        user = Admin.objects.filter(Admin_Name=user_name)
        search_result = json.loads(serializers.serialize(
          'json', user, ensure_ascii=False))
        if search_result:
            logging.debug(search_result)
            check_pass = search_result[0]['fields']['Admin_PW']
        else:
            return HttpResponse('loginAdminFailed')
        if check_pass == user_password:
            return HttpResponse('loginAdminSuccess')
    return HttpResponse('loginAdminFailed')
def add_user(request):
    if request.method == 'POST':
        user = json.loads(request.body.decode())
        ipCus = user['ipCus']
        name = user['name']
        if user['sex'] == 'male':
            sex = 0
        else:
            sex = 1
        bir = user['bir']
        pw = 123
        User.objects.create(
            S_OP_IP_Cus=ipCus,
            S_ME_CI_Nam=name,
            S_ME_CI_Sex=sex,
            S_ME_CI_Bir=bir,
            S_ME_CI_PW=pw
        )
        return HttpResponse('add user successful')
    return HttpResponse('add user failed')

def add_user_info(request):
    if request.method == 'POST':
        user_info = json.loads(request.body.decode())
        ipCus = user_info['ipCus']
        name = user_info['name']
        if user_info['sex'] == 'male':
            sex = 0
        else:
            sex = 1
        bir = user_info['bir']
        checkdate = user_info['checkdate']
        balL = user_info['balL']
        balR = user_info['balR']
        axeL = user_info['axeL']
        axeR = user_info['axeR']
        posL = user_info['posL']
        posR = user_info['posR']
        eqDegreeL =  round((balL + posL/2), 3)
        eqDegreeR = round((balR + posR/2), 3)
        age = cal_time(bir, checkdate).days // 365
        print(age)
        Info.objects.create(
            S_OP_IP_Cus=ipCus,
            S_OP_IP_Che=checkdate,
            S_ME_CI_Nam=name,
            S_ME_CI_Sex=sex,
            S_ME_CI_Bir=bir,
            S_OP_IP_Bal=balL,
            S_OP_IP_Bal1=balR,
            S_OP_IP_Axe=axeL,
            S_OP_IP_Axe1=axeR,
            S_OP_IP_Pos=posL,
            S_OP_IP_Pos1=posR,
            Eq_Degree=eqDegreeL,
            Eq_Degree1=eqDegreeR,
            Age=age
        )
        return HttpResponse('add userInfo successful')
    return HttpResponse('add userInfo failed')

def modify_doc_pass(request):
    if request.method == 'POST':
        doc_info = json.loads(request.body.decode())
        username = doc_info['username']
        oldpass = doc_info['oldpass']
        newpass = doc_info['newpass']
        res = Admin.objects.filter(Admin_Name=username)
        res = json.loads(serializers.serialize(
            'json', res, ensure_ascii=False))
        if res:
            check_pass = res[0]['fields']['Admin_PW']
            if oldpass != check_pass:
                return HttpResponse('Wrong Password')
            Admin.objects.filter(Admin_Name=username).update(
                Admin_PW=newpass
            )
            return HttpResponse('Modify successful')
        else:
            return HttpResponse('Admin not Found')
    return HttpResponse('Modify failed')

def get_visual_data(request):
    if request.method == 'GET':
        userName = request.GET.get('username', None)
        info = Info.objects.filter(S_ME_CI_Nam=userName)
        info = json.loads(serializers.serialize(
            'json', info, ensure_ascii=False))
        if info:
            res = []
            for item in info:
                res.append(item['fields'])
            res = json.dumps(res)
            return HttpResponse(res)
        else:
            return HttpResponse('None')
    return HttpResponse("Get info failed")

def get_user_info(request):
    if request.method == 'GET':
        userName = request.GET.get('username', None)
        info = User.objects.filter(S_ME_CI_Nam=userName)
        info = json.loads(serializers.serialize(
            'json', info, ensure_ascii=False))
        if info:
            res = []
            for item in info:
                res.append(item['fields'])
            res = json.dumps(res)
            return HttpResponse(res)
        else:
            return HttpResponse('None')
    return HttpResponse("Get info failed")

def modify_user_pass(request):
    if request.method == 'POST':
        user_info = json.loads(request.body.decode())
        username = user_info['username']
        oldpass = user_info['oldpass']
        newpass = user_info['newpass']
        res = User.objects.filter(S_ME_CI_Nam=username)
        res = json.loads(serializers.serialize(
            'json', res, ensure_ascii=False))
        if res:
            check_pass = res[0]['fields']['S_ME_CI_PW']
            if oldpass != check_pass:
                return HttpResponse('Wrong Password')
            User.objects.filter(S_ME_CI_Nam=username).update(
                S_ME_CI_PW=newpass
            )
            return HttpResponse('Modify successful')
        else:
            return HttpResponse('User not Found')
    return HttpResponse('Modify failed')

def get_prediction(request):
    if request.method == 'GET':
        userName = request.GET.get('username', None)
        info = User.objects.filter(S_ME_CI_Nam=userName)
        info = json.loads(serializers.serialize(
            'json', info, ensure_ascii=False))
        if info:
            cus_id = info[0]['fields']['S_OP_IP_Cus']
            pre_data = Prediction.objects.filter(ID=cus_id)
            pre_data = json.loads(serializers.serialize(
            'json', pre_data, ensure_ascii=False))
            if pre_data:
                pre_data = pre_data[0]['fields']
                X = []
                X.append(pre_data['Age'])
                for i in range(9):
                    name = 'year{}'.format(i)
                    if pre_data[name + 'left'] == 'NULL':
                        break
                    X.append(pre_data[name + 'left'])
                    X.append(pre_data[name + 'right'])
                if len(X) == 7:
                    path_str1 = PROJECT + "user/model/model1.m"
                    clf1 = joblib.load(path_str1)
                    pre3to4 = clf1.predict([X])[0]
                    X.append(round(pre3to4[0], 3))
                    X.append(round(pre3to4[1], 3))
                if len(X) == 9:
                    path_str2 = PROJECT + "user/model/model2.m"
                    clf2 = joblib.load(path_str2)
                    pre4to5 = clf2.predict([X])[0]
                    X.append(round(pre4to5[0], 3))
                    X.append(round(pre4to5[1], 3))
                if len(X) == 11:
                    path_str3 = PROJECT + "user/model/model3.m"
                    clf3 = joblib.load(path_str3)
                    pre5to6 = clf3.predict([X])[0]
                    X.append(round(pre5to6[0], 3))
                    X.append(round(pre5to6[1], 3))
                print(X)
                res = json.dumps(X)
                return HttpResponse(res)
    return HttpResponse("GET Failed")

def get_user_age(request):
    if request.method == 'GET':
        userName = request.GET.get('username', None)
        info = User.objects.filter(S_ME_CI_Nam=userName)
        info = json.loads(serializers.serialize(
            'json', info, ensure_ascii=False))
        if info:
            birthday = info[0]['fields']['S_ME_CI_Bir'][:10]
            birthday = time.strptime(birthday, "%Y-%m-%d")
            birthday = datetime.datetime(birthday[0], birthday[1], birthday[2])
            now_time = datetime.datetime.now()
            age = (now_time - birthday).days // 365
            age = json.dumps(age)
            return HttpResponse(age)
        return HttpResponse("Get info failed")

def get_stat(request):
    if request.method == 'GET':
        info = Stat.objects.all()
        info = json.loads(serializers.serialize(
            'json', info, ensure_ascii=False))
        if info:
            res = info[len(info) - 1]['fields']
            print(res)
            res = json.dumps(res)
            return HttpResponse(res)
        return HttpResponse("Get info failed")