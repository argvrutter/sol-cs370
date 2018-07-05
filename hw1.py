# August 2013 High Temps for Knoxville,TN
# Hwk 1 for COSC 370
#
'''
Homework 1: Using Matplotlib to Graph Temperature Data
Author: Aiden Rutter
netid: arutter1
Description: 
'''
from numpy import arange
import matplotlib.pyplot as plt
xData = arange(1,32)    # Ranges for x and y axes must match
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
avg = [86.]  # First value for montly avg high temp is just Day 1 temp

## 1) CALCULATE A RUNNING MONTHLY AVERAGE AND PRINT IT OUT IN A TABLE
##    IT DOES NOT MATTER HOW THE TABLE IS FORMATTED
tSum = 0.0
avg = []

for i, t in enumerate(tData):
    tSum += t
    avg.append(tSum / (i+1))
    print('|','%.2d' % (i+1), '|', '%.2f' % avg[i], '|')

## 2) CREATE A GRAPH FOR THE DATA USING MATPLOTLIB
##	- PLOT RED POINTS WITH BLUE LINE FOR ORIGINAL DATA
##	- SHOW CHANGE IN AVERAGE HIGH WITH GREEN DASHED LINE
##	- SET DISPLAY RANGES FOR X AND Y AXES
##		- X SHOULD RANGE FROM 0 TO 32
##		- Y SHOULD RANGE FROM 70 TO 95
##	- ENABLE GRID DISPLAY
##	- LABEL AXES AND SET TITLE
##	- USE MATPLOTLIB.PYPLOT.TEXT() TO LABEL THE MONTHLY AVERAGE LINE

plt.show()

