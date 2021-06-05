import hashlib
import time

import matplotlib.pyplot as plt
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from mysite import settings
from recognition_app.model.model_test import model_test
import os

def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
        print("144444")
    return render(request,"index.html",)


    # return HttpResponse("ok")

def test(request):
    html = "<h1>this is it</h1>"
    return HttpResponse(html)

def result(request,a):
    b= model_test(a)
    return HttpResponse(b)
def comput(request,a,fuhao,b):
    if fuhao == "+":
        c=a+b
    else:
        if fuhao == "-":
            c=a-b
        else:
            if fuhao =="*":
                c=a*b
            else:
                c="sorry"
    return HttpResponse("结果为%s"%c)


def upimage(request):
    if request.method == 'POST':
        file = request.FILES['file'].read()
        mytime0 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        mytime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        img_name = mytime0 + '.jpg'
        mypath = "D:/PycharmProjects/mysite/pic/" + img_name
        path = mypath.encode('utf-8')
        f = open(path, 'wb');  # 代开一个文件，准备以二进制写入文件
        f.write(file);  # write并不是直接将数据写入文件，而是先写入内存中特定的缓冲区
        f.flush();  # 将缓冲区的数据立即写入缓冲区，并清空缓冲区
        f.close();  # 关闭文件

        # print(file)qa2
        print(img_name)

        result_final = model_test(img_name)
        # plt.savefig()
        # message = '这是关于post方法'
    return HttpResponse(result_final)






