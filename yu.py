#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from urllib.request import urlopen
import csv
import time
import matplotlib.pyplot as plt


def number_of_region(x):
    S = [24, 25, 5, 6, 27, 23, 26, 7, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 8, 9, 10, 1, 3, 2, 4]
    return S[x - 1]


def get_state_name(id):
    if (id == 1):
        state = 'Vinnitska'
        return state
    elif (id == 2):
        state = 'Volynska'
        return state
    elif (id == 3):
        state = 'Dniprovska'
        return state
    elif (id == 4):
        state = 'Donetska'
        return state
    elif (id == 5):
        state = 'Zhytomyrska'
        return state
    elif (id == 6):
        state = 'Zakarpatska'
        return state
    elif (id == 7):
        state = 'Zaporozhska'
        return state
    elif (id == 8):
        state = 'Ivano-Frankivska'
        return state
    elif (id == 9):
        state = 'Kyivska'
        return state
    elif (id == 10):
        state = 'Kirovogradska'
        return state
    elif (id == 11):
        state = 'Luganskska'
        return state
    elif (id == 12):
        state = 'Lvivska'
        return state
    elif (id == 13):
        state = 'Nikolaevska'
        return state
    elif (id == 14):
        state = 'Odessaska'
        return state
    elif (id == 15):
        state = 'Poltavaska'
        return state
    elif (id == 16):
        state = 'Rivnenska'
        return state
    elif (id == 17):
        state = 'Sumska'
        return state
    elif (id == 18):
        state = 'Ternopilska'
        return state
    elif (id == 19):
        state = 'Kharkovska'
        return state
    elif (id == 20):
        state = 'Khersonska'
        return state
    elif (id == 21):
        state = 'Khmelnytska'
        return state
    elif (id == 22):
        state = 'Cherkaska'
        return state
    elif (id == 23):
        state = 'Chernivetska'
        return state
    elif (id == 24):
        state = 'Chernihivska'
        return state
    elif (id == 25):
        state = 'Republic of Crimea'
        return state





# def save_all(id):
#
#     name = get_state_name(id)
#     index = str(id)
#     filename = index + '_' + name + '.csv'
#     appropriate_id = number_of_region(id)
#     url2 = r"https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=%s&year1=1981&year2=2018&type=Mean" % appropriate_id
#     vhi_url2 = urlopen(url2)
#     out2 = open(r"rawdata/%s" % filename, 'wb')
#     out2.write(vhi_url2.read())
#     out2.close()
#     col = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI']
#     df = pd.read_csv(r"rawdata/%s" % filename, index_col=False, header=1, sep=", {0,3}|\s+", engine='python')
#     df.columns = col
#     url1 = r"https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=%s&year1=1981&year2=2018&type=VHI_Parea" % appropriate_id
#     vhi_url1 = urlopen(url1)
#     out1 = open(r"raw1/%s" % filename, 'wb')
#     out1.write(vhi_url1.read())
#     out1.close()
#
#     col = ['Year', 'Week', '0', '5', '10', '15', '20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100',]
#     df = pd.read_csv(r"raw1/%s" % filename, index_col=False, header=1, sep=", {0,3}|\s+", engine='python')
#     df.columns = col


def name(index):
    index_string = str(index)
    filename = index_string + '_' + get_state_name(index) + '.csv'
    return filename

def min_VHI(index):
    filename = name(index)
    df = pd.read_csv(r"all/%s" % filename)
    print("\nMin for " + get_state_name(index) +" : " + str(df['VHI'].min()))


def max_VHI(index):
    filename= name(index)
    df = pd.read_csv(r"all/%s" % filename)
    print("\nMax for " + get_state_name(index) +" : " + str(df['VHI'].max()))

def VHI_drought1(index):
    filename = name(index)
    df = pd.read_csv(r"all/%s" % filename)
    df=df[(df['VHI']<15)]
    print('\nDrought in '+get_state_name(index))
    print (df[['Year','Week','VHI']])

def VHI_drought2(index,area):
    filename = name(index)
    df = pd.read_csv(r"all/%s" % filename)
    sum_rows = pd.DataFrame(np.zeros((1843, 1)))
    for i in range(0,3):
        print(i)
        print("..............start..............")
        n = i*5
        result = pd.concat([sum_rows,df[r"%s" % n]],axis=1)
        sum_rows = result.sum(axis=1)

    df['VHI<15'] = sum_rows
    print(df[df['VHI<15']>area])


for index in range(1,26):
    # save_all(index)
    min_VHI(index)
    max_VHI(index)











