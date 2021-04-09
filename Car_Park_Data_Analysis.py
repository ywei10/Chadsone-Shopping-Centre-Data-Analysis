#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:08:35 2019

@author: yuanwei
"""
import pandas as pd
from pylab import *
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import scipy
import scipy.stats

data = pd.read_csv('Shopping Centre Parking.csv')
Date = pd.to_datetime(data['Date'], format='%d/%m/%y')
#fig = plt.figure(figsize=[7,5])
#plt.show()


#x = data.Date
#y = data.NE
#plt.scatter(x,y)

#Sum_All_Parking = data.sum(axis=1)
data['Sum_All_Parking'] = data.iloc[:,-4:].sum(axis=1)
#sum([data.NE, data.SE, data.S, data.SW])
#print(data)


# =============================================================================
# q2 T-test
# =============================================================================
Start_T1 = datetime.strptime('2018-1-29', '%Y-%m-%d')
End_T1 = datetime.strptime('2018-3-29', '%Y-%m-%d')
T1_classtime = (Date>=Start_T1) & (Date<=End_T1)
T1_schooldays = data.Sum_All_Parking[T1_classtime].sum()
print(T1_schooldays)

Start_T2 = datetime.strptime('2018-4-16', '%Y-%m-%d')
End_T2 = datetime.strptime('2018-6-29', '%Y-%m-%d')
T2_classtime = (Date>=Start_T2) & (Date<=End_T2)
T2_schooldays = data.Sum_All_Parking[T2_classtime].sum()
print(T2_schooldays)

Start_T3 = datetime.strptime('2018-7-16', '%Y-%m-%d')
End_T3 = datetime.strptime('2018-9-21', '%Y-%m-%d')
T3_classtime = (Date>=Start_T3) & (Date<=End_T3)
T3_schooldays = data.Sum_All_Parking[T3_classtime].sum()
print(T3_schooldays)

Start_T4= datetime.strptime('2018-10-8', '%Y-%m-%d')
End_T4= datetime.strptime('2018-12-21', '%Y-%m-%d')
Start_new_T1 = datetime.strptime('2019-1-28', '%Y-%m-%d')
T4_classtime = (Date>=Start_T4) & (Date<=End_T4)
T4_schooldays = data.Sum_All_Parking[T4_classtime].sum()
print(T4_schooldays)

T1_holidayrange = (Date>End_T1) & (Date<Start_T2)
T1_holiday = data.Sum_All_Parking[T1_holidayrange].sum()
print(T1_holiday)

T2_holidayrange = (Date>End_T2) & (Date<Start_T3)
T2_holiday = data.Sum_All_Parking[T2_holidayrange].sum()
print(T2_holiday)

T3_holidayrange = (Date>End_T3) & (Date<Start_T4)
T3_holiday = data.Sum_All_Parking[T3_holidayrange].sum()
print(T3_holiday)

T4_holidayrange = (Date>End_T4) & (Date<=Start_new_T1)
T4_holiday = data.Sum_All_Parking[T4_holidayrange].sum()
print(T4_holiday)
# =============================================================================
# bar chart
# =============================================================================
height2 = [T1_schooldays, T2_schooldays, T3_schooldays, T4_schooldays]
height1 = [T1_holiday, T2_holiday, T3_holiday, T4_holiday]
# Choose the names of the bars
bars = ('Term1', 'Term2', 'Term3', 'Term4')
positions1 = [0, 1, 2, 3]
positions2 = [0.3, 1.3, 2.3, 3.3]
positions3 = [0.15, 1.15, 2.15, 3.15]
# Create bars
plt.bar(positions1, height1, width=0.3, color='green')
plt.bar(positions2, height2, width=0.3)
plt.title('School-holidays vs Non-school-holidays')
# Create names on the x-axis
plt.xticks(positions3, bars)
#plt.yticks(color='orange')
# Show graphic
plt.show()

# =============================================================================
# q2 t-test
# =============================================================================
c1 = data.Sum_All_Parking[T1_classtime] 
c2 = data.Sum_All_Parking[T2_classtime] 
c3 = data.Sum_All_Parking[T3_classtime] 
c4 = data.Sum_All_Parking[T4_classtime] 
t_schooldays = pd.concat([c1, c2, c3, c4])

c5 = data.Sum_All_Parking[T1_holidayrange]
c6 = data.Sum_All_Parking[T2_holidayrange]
c7 = data.Sum_All_Parking[T3_holidayrange]
c8 = data.Sum_All_Parking[T4_holidayrange]
t_holidays = pd.concat([c5, c6, c7, c8])
#print(t_schooldays)
#print(t_holidays)
print ('--------q2 t-test-------------')
w, pvalue = scipy.stats.shapiro(t_holidays)
print(w, pvalue)
w, pvalue = scipy.stats.shapiro(t_schooldays)
print(w, pvalue)
t, pvalue = scipy.stats.ttest_ind(t_holidays, t_schooldays)
print(t, pvalue)

#bp = boxplot([t_holidays, t_schooldays], labels=['holidays','non-holidays'])
#print(bp)


# =============================================================================
# box-plot
# =============================================================================

bp = boxplot([A, B, C, D], labels=['NE','SE','S','SW'])
print(bp)
# =============================================================================
# box plot
# =============================================================================

NE_mean = np.mean(data['NE'])
SE_mean = np.mean(data['SE'])
S_mean = np.mean(data['S'])
SW_mean = np.mean(data['SW'])

NE_std = np.std(data['NE'])
SE_std = np.std(data['SE'])
S_std = np.std(data['S'])
SW_std = np.std(data['SW'])

A = data['NE']
B = data['SE']
C = data['S']
D = data['SW']

materials = ['NE', 'SE', 'S', 'SW']
CTEs = [NE_mean, SE_mean, S_mean, SW_mean]
error = [NE_std, SE_std, S_std, SW_std]
x_pos = np.arange(len(materials))

fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)
# =============================================================================
# 
# =============================================================================
#bp = boxplot([A, B, C, D], labels=['NE','SE','S','SW'])
#print(bp)

# =============================================================================
# q3 Nomal distribution 
# =============================================================================
print ('--------q3 Nomal distribution-------------')
w, pvalue = scipy.stats.shapiro(data['NE'])
print(w, pvalue)
w, pvalue = scipy.stats.shapiro(data['SE'])
print(w, pvalue)
w, pvalue = scipy.stats.shapiro(data['S']) 
print(w, pvalue)
w, pvalue = scipy.stats.shapiro(data['SW']) 
print(w, pvalue)
# =============================================================================
#  Anova test (faulty)
# =============================================================================
print ('-------- Anova test (faulty)-------------')
fvalue, pvalue = stats.f_oneway(A, B, C, D)
print(fvalue, pvalue)

# =============================================================================
#   replace Anova test (not nomal)
# =============================================================================
print ('--------replace Anova test (not nomal)-------------')
h, pvalue = stats.kruskal(A, B, C, D)
print(h, pvalue)
# =============================================================================
# t-test (faulty)
# =============================================================================
print ('--------t-test (faulty)-------------')
tstats, pvalue = stats.ttest_ind(A, B, equal_var=False)
print(tstats, pvalue)
tstats, pvalue = stats.ttest_ind(A, C, equal_var=False)
print(tstats, pvalue)
tstats, pvalue = stats.ttest_ind(A, D, equal_var=False)
print(tstats, pvalue)
tstats, pvalue = stats.ttest_ind(B, C, equal_var=False)
print(tstats, pvalue)
tstats, pvalue = stats.ttest_ind(B, D, equal_var=False)
print(tstats, pvalue)
tstats, pvalue = stats.ttest_ind(C, D, equal_var=False)
print(tstats, pvalue)
# =============================================================================
# replace t-test
# =============================================================================
print ('--------replace t-test-------------')
u, pvalue = stats.mannwhitneyu(A, B)
print(u, pvalue)
u, pvalue = stats.mannwhitneyu(A, C)
print(u, pvalue)
u, pvalue = stats.mannwhitneyu(A, D)
print(u, pvalue)
u, pvalue = stats.mannwhitneyu(B, C)
print(u, pvalue)
u, pvalue = stats.mannwhitneyu(B, D)
print(u, pvalue)
u, pvalue = stats.mannwhitneyu(C, D)
print(u, pvalue)

stats.probplot(data, dist='norm', plot=plt)
plt.show()