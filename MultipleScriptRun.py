import os
import sys
import xlrd
import configparser
import pathlib
import subprocess
import pandas as pd
import xlrd

import threading
import time

from selenium import webdriver
import multiprocessing
config = configparser.RawConfigParser()
config.read('C:/Users/User/Desktop/DATAS/conf/expert.properties')
dir = config.get('GlobalConfig', 'expert.global.Scripts.path')
filterEngine = config.get('GlobalConfig', 'expert.global.FilterScripts.path')
DataPath = config.get('GlobalConfig','expert.global.DataPath.path')
EmailPath = config.get('GlobalConfig', 'expert.global.EmailPath.path')
ChromeDriver = config.get('GlobalConfig','expert.global.ChromeDriver.path')
Excel = config.get('GlobalConfig','expert.global.Keyword.path')
workbook = xlrd.open_workbook(Excel)
state = workbook.sheet_by_name("StateUSA")
UState = state.cell_value(0, 0)
Material = workbook.sheet_by_name("Keyword")
keyword = Material.cell_value(0, 0)
#print(sys.path)
#print("success")

# list = os.listdir(dir) # dir is your directory path
# number_files = len(list)
# print(number_files)
# arr = os.listdir(".")
# print(arr)

# py = pathlib.Path().glob("*.py")
# for file in py:
#     print(file)


def worker(file):
    # subprocess.Popen("python3 RDAT.py & python3 YP.py", shell=True)
    print("file======",file)
    print("script======", file)

    process1 = subprocess.Popen(["python", file])
    process1.wait()
    print("proces======", file)


if __name__ == '__main__':
    py = pathlib.Path().glob("*.py")
    for bot in py:
      p = multiprocessing.Process(target=worker, args=(bot,))
      p.start()

print("main script")