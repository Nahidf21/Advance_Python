#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:20:46 2023

@author: nahidferdous
"""
## Data visualizetion with pandas 
## Data Link: 
## https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download

import pandas as pd
myData=pd.read_csv("vgsales.csv")

var1=myData["Platform"]

#create bar chart
import matplotlib.pyplot as plt

var1.value_counts().plot.bar()
plt.show()

#Histogram
var1.value_counts().plot.hist(orientation='vertical')
plt.show()

#area plot 
second_data=myData[["EU_Sales","JP_Sales"]]
second_data.plot.area(stacked=False)
plt.show()

second_data=myData[["EU_Sales","JP_Sales"]]
second_data.plot.area(stacked=True)
plt.show()

#Pie Chart

var2=myData["Platform"].head(200)
var2.value_counts().plot.pie(figsize=(8,8))
plt.show()

## Next customize Matplotlib ...... 











