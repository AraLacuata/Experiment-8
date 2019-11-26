# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:01:23 2019

@author: Ara
"""

import pandas as pd
cars = pd.read_csv('cars.csv')
x = cars.head()
y = cars.tail()
print('First five rows: \n',x)
print('Last five rows: \n',y)