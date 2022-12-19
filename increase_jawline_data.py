###IMPORTS####
# import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#columns
gender = 'Gender'
ethnicity = 'Ethnicity'
so = 'Sexual Preference'
c1 = 'white male'
c2 = 'asian female'
c3 = 'white female'
c4 = 'black female'
c5 = 'latino male'
c6 = 'black male'
c7 = 'asian male'
c8 = 'latina female'
columns = [c1,c2,c3,c4,c5,c6,c7,c8]

incr_jaw_data = pd.read_excel('Final Project\Increase Jawline.xlsx')
# index of each category

#gender
female = incr_jaw_data[incr_jaw_data[gender] == 'Female'].index.tolist()
male = incr_jaw_data[incr_jaw_data[gender] == 'Male'].index.tolist()
other = [i for i in range(len(incr_jaw_data.index)) if i not in female if i not in male]

#dict of category: rating for each
incr_jaw_female = {c:[] for c in columns}
incr_jaw_male = {c:[] for c in columns}
incr_jaw_other = {c:[] for c in columns}

for c in columns:
    for f in female:
        incr_jaw_female[c].append(incr_jaw_data.loc[f][c])
    for m in male:
        incr_jaw_male[c].append(incr_jaw_data.loc[m][c])
    for o in other:
        incr_jaw_other[c].append(incr_jaw_data.loc[o][c])

#ethnicity
white = incr_jaw_data[incr_jaw_data[ethnicity] == 'White'].index.tolist()
black = incr_jaw_data[incr_jaw_data[ethnicity] == 'Black'].index.tolist()
hispanic = incr_jaw_data[incr_jaw_data[ethnicity] == 'Hispanic'].index.tolist()
asian = incr_jaw_data[incr_jaw_data[ethnicity] == 'Asian'].index.tolist()
other_ethnicity = [i for i in range(len(incr_jaw_data.index)) if i not in white if i not in black if i not in hispanic if i not in asian]


incr_jaw_white = {c:[] for c in columns}
incr_jaw_black = {c:[] for c in columns}
incr_jaw_hispanic = {c:[] for c in columns}
incr_jaw_asian = {c:[] for c in columns}
incr_jaw_other_eth = {c:[] for c in columns}

for c in columns:
    for w in white:
        incr_jaw_white[c].append(incr_jaw_data.loc[w][c])
    for b in black:
        incr_jaw_black[c].append(incr_jaw_data.loc[b][c])
    for h in hispanic:
        incr_jaw_hispanic[c].append(incr_jaw_data.loc[h][c])
    for a in asian:
        incr_jaw_asian[c].append(incr_jaw_data.loc[a][c])
    for e in other_ethnicity:
        incr_jaw_other_eth[c].append(incr_jaw_data.loc[e][c])


#sexual preference
hetero = incr_jaw_data[incr_jaw_data[so] == 'Heterosexual'].index.tolist()
homo = incr_jaw_data[incr_jaw_data[so] == 'Homosexual'].index.tolist()
bi = incr_jaw_data[incr_jaw_data[so] == 'Bisexual'].index.tolist()
ace = incr_jaw_data[(incr_jaw_data[so] == 'Asexual') & (incr_jaw_data[so] == 'Aromantic')].index.tolist()
other_so = [i for i in range(len(incr_jaw_data.index)) if i not in hetero if i not in homo if i not in bi if i not in ace]

incr_jaw_hetero = {c:[] for c in columns}
incr_jaw_homo = {c:[] for c in columns}
incr_jaw_bi = {c:[] for c in columns}
incr_jaw_ace = {c:[] for c in columns}
incr_jaw_other_so = {c:[] for c in columns}

for c in columns:
    for h in hetero:
        incr_jaw_hetero[c].append(incr_jaw_data.loc[h][c])
    for o in homo:
        incr_jaw_homo[c].append(incr_jaw_data.loc[o][c])
    for b in bi:
        incr_jaw_bi[c].append(incr_jaw_data.loc[b][c])
    for a in ace:
        incr_jaw_ace[c].append(incr_jaw_data.loc[a][c])
    for e in other_so:
        incr_jaw_other_so[c].append(incr_jaw_data.loc[e][c])


'''
control_female
control_male
control_others

control_white
control_black
control_asian
control_hispanic
control_other_eth

control_hetero
control_homo
control_bi
control_ace
control_other_so
'''