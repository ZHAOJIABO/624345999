import numpy as np
import matplotlib.pyplot as plt  # plt 用于显示图片
import os
import matplotlib.image as mpimg  # mpimg 用于读取图片
def model_test(pic_add):
    path = os.path.join('D:\PycharmProjects\mysite\pic',pic_add)

    lena = mpimg.imread(path)  # 读取和代码处于同一目录下的 lena.png
    # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
    # lena.shape  # (512, 512, 3)

    print(lena.shape)
    result =lena.shape
    return result


