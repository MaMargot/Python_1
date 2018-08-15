# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 16:55:19 2018

@author: MaMargot
"""

#调用模块准备
import numpy as np
import pandas as pd

#1.数据准备工作
#样本公司数据
data_ST_2=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\\2ST.xls') ###ST
data_ST_3=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\\3ST.xls') ###*ST
data_2ST_3ST=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\\2STto3ST.xls') ###ST变*ST
data_3ST_2ST=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\\3STto2ST.xls') ###*ST变ST
#公司建模数据
data_is_all=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\is_all.xls') ###利润分配表
data_bs_all=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\\bs_all.xls') ###资产负债表
data_scf_all=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\scf_all.xls') ###现金流量表
data_yanfa=pd.read_excel('C:\Users\MaMargot\.spyder2\scrpit\FN_Fn023.xls')  ###研发支出费用

#2.数据预处理工作
### 2.1数据整理
data_ST_2.groupby('上市公司代码_ComCd')




















