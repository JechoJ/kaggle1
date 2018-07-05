# -*- coding: utf-8 -*-
# @Author  : jiangxiyue
# @Software: PyCharm
import sys
sys.path.append(r'F:\fenqigo\script\collection_summary_proc')
from DBConn_pymysql import DBConn
import os
os.chdir(r'G:\Downloads\home_credit')
import pandas as pd
import numpy as np

train_id = pd.read_csv('input/application_train.csv')
bureau = pd.read_csv('input/bureau.csv')
bureau_balance = pd.read_csv('input/bureau_balance.csv')
credit_card_balance = pd.read_csv('input/credit_card_balance.csv')
installments_payments = pd.read_csv('input/installments_payments.csv')
POS_CASH_balance = pd.read_csv('input/POS_CASH_balance.csv')
previous_application = pd.read_csv('input/previous_application.csv')

bureau['DAYS_CREDIT_a'] = bureau['DAYS_CREDIT'].apply(lambda x:0-x)
bureau['DAYS_CREDIT_cut'] = pd.cut(bureau['DAYS_CREDIT_a'], bins=[    0.,   365.,   730.,  1095.,  1460.,  1825.,  2190.,  2555.,
        2920.,  3285.,  3650.],labels=[1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.])