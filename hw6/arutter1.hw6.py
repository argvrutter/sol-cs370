#!/usr/bin/env python3
#
# Template for Problem 10 from Problem Set 3.2
#

'''
Homework 6: Curve Fitting Thermal Efficiencies
Author: Aiden Rutter
netid: arutter1
Description: use least squares curve fitting to predict
the thermal efficiency of a year 2000 steam engine based on Problem 10 of Problem Set 3.2self.
determining the best polynomial fit to the data given and then using that polynomial for the prediction.
'''

from numpy import array,zeros
from polyFit import *
# import pylabs
import matplotlib.pyplot as pylab
def evalPoly(c,x): # c stores coefficients for polynomial
    m = len(c) - 1 # (copied from polyFit module)
    p = c[m]
    for j in range(m):
        p = p*x + c[m-j-1]
    return p

xData = array([1718,1767,1774,1775,1792,1816,1828,1834,1878,1906])
yData = array([0.5,0.8,1.4,2.7,4.5,7.5,12.0,17.0,17.2,23.0])

minsdev=float("inf")
minpoly=0
n=len(xData)
print('Degree  Stdev   2000P')
for m in range(1,6):   # Try m=1,2,3,4,5 (degree of polynomial)
    ys=zeros((n),dtype='float') # initialize y-coordinates for polynomial curve
    # Returns coefficients of polynomial
    coeff = polyFit(xData, yData, m) # get coefficients for n-th degree polynomial
    # Retrieves std. deviation between p(x) and the data
    stdev = stdDev(coeff, xData, yData) # get stdev of the error in the fit
    # Evaluates the polynomial at year 2000
    proj  = evalPoly(coeff, 2000) # evaluate the polynomial at year 2000
#
#   Year 2000 projections >= 100 or < 0 are meaniningless
#
    if (stdev < minsdev) and proj < 100 and proj > 0 :

        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'viable'))
        # List comprehension, compute x values by evaluating polynomial
        ys=  [evalPoly(coeff, x) for x in xData] # get y-coordinates of polynomial using x-coordinates in xData array
#
#       Use Matplotlib to plot original data points with validated curve fitting
#
        pylab.xlabel("x")
        pylab.ylabel("Thermal Efficiency")
        my_title= 'Fit with poly degree = ' + str(m) + '; green dot is 2000 projection'
        pylab.title(my_title)
        # Min and max of xData
        pylab.xlim((1710, 2015))            # x-axis values should range from 1710 to 2015
        pylab.plot(2000, proj, 'go')            # plot Year 2000 projection as a green dot
        pylab.plot(xData, yData, 'ro')            # plot the original data given in the xData and yData
                                   # arrays as red dots
        pylab.plot(xData, ys, 'b-')            # plot polynomial curve using xData and ys arrays
                                   # and make it blue.
        pylab.grid()
        pylab.show()
    else :
        print('{:3d}\t{:5.3f}\t{:5.3f}\t{:s}'.format(m,stdev,proj,'not viable'))

#--------------------------------------------------------------------------------------
# Table to stdout should look similar to this...
#
# Degree Stdev   2000P
#   1 	 2.855	 34.986	    viable
#   2	 2.768	 45.419	    viable
#   3	 2.266	 -6.602	    not viable
#   4	 2.234	 112.391	not viable
#   5	 2.496	 113.726	not viable
#--------------------------------------------------------------------------------------
