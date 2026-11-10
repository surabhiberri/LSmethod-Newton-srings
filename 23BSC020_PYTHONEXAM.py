# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:24:26 2026

@author: Surabhi
"""

import math

wavelength = 589*10e-7 #in c metres

listn = [20,16,12,8,4]
left = [0.395,0.373,0.35,0.312,0.269]
right = [-0.067,-0.043,-0.017,0.012,0.064]


listn2 = []
for i in range(len(listn)):
    temp = listn[i]**2
    listn2.append(temp)
    
Dn = []
for i in range(len(right)) and range(len(left)):
    val = abs(left[i] - right[i])
    Dn.append(val)

Dn2 = []  
for i in range(len(Dn)):
    temp2 = Dn[i]**2
    Dn2.append(temp2)

totalsum_n = sum(listn)
totalsum_Dn2  = sum(Dn2)

xy = []
for i in range(len(listn)) and range(len(Dn2)):
    vall = listn[i]*Dn2[i]
    xy.append(vall)
slope = (5*sum(xy) - totalsum_n*totalsum_Dn2)/(5*sum(listn2) - math.pow(totalsum_n,2))
intercept = (totalsum_Dn2 - slope*totalsum_n)/5
    

Dn2_fit = []
residual = []
for i in range(len(listn)) and range(len(Dn2)):
    val1 = slope*listn[i] + intercept
    Dn2_fit.append(val1)
    val2 = Dn2[i] - Dn2_fit[i]
    residual.append(val2)

res2 = []
for i in range(len(residual)):
    val3 = residual[i]**2
    res2.append(val3)
    
stand_dev = math.sqrt((sum(res2)/3))

mean  = totalsum_n/5

sig=[]
for i in range(len(listn)):
    sig1 = (listn[i] - mean)**2
    sig.append(sig1)
    
totalsum_sig = sum(sig)

error = stand_dev/(math.sqrt(totalsum_sig))

uncert = error/(4*wavelength)

Radius = slope/(4*wavelength)

Rad_plus = Radius + error
Rad_minus = Radius - error

print("NEWTONS'S RINGS: LEAST SQUARES ANALYSIS")
print("\n-----------------------------------")
print(f"\nSlope                        : {slope.4f} m^2 per ring")
print(f"\nStandard error of slope      : {error.4f} m^2 per ring")
print(f"\nIntercept                    : {intercept.4f} m^2")
print(f"\nFitted equation              : Dn^2 = {slope.4f}*n + {intercept}")
print(f"\nRadius of curvature          : {Radius.4f} m")
print(f"\nUncertainty in Radius        : {uncert.4f} m")
print("\nFinal result: ")
print(f"\nR = {Rad_plus}+- {Rad_minus}")


    



    
    
    
