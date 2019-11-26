# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:01:23 2019

@author: Ara
"""

import pandas as pd
cars = pd.read_csv('cars.csv')
x = cars.head()
a = x.iloc[:,1:12:2]
b = cars[(cars['Model'] == 'Mazda RX4')]
c = cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
d = cars.loc[(cars['Model']=='Mazda RX4 Wag')
| (cars['Model']=='Ford Pantera L') | (cars['Model']=='Honda Civic'),
['Model','cyl','gear']]

print('a) Odd numbered columns of first five rows: \n\n',a,'\n\n')
print('b) Row of the model Mazda RX4: \n\n',b,'\n\n')
print('c) Number of cylinders of Camaro Z28 \n\n',c,'\n\n')
print('d) Number of cylinders and gear of Mazda RX4 Wag, Honda Civic,' 
' and Ford Pantera L: \n\n',d,'\n\n')
