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

increase_eyes = pd.read_excel('Final Project\Increase Eyes.xlsx')
# index of each category

#gender
female = increase_eyes[increase_eyes[gender] == 'Female'].index.tolist()
male = increase_eyes[increase_eyes[gender] == 'Male'].index.tolist()
other = [i for i in range(len(increase_eyes.index)) if i not in female if i not in male]

#dict of category: rating for each
incr_eyes_female = {c:[] for c in columns}
incr_eyes_male = {c:[] for c in columns}
incr_eyes_other = {c:[] for c in columns}

for c in columns:
    for f in female:
        incr_eyes_female[c].append(increase_eyes.loc[f][c])
    for m in male:
        incr_eyes_male[c].append(increase_eyes.loc[m][c])
    for o in other:
        incr_eyes_other[c].append(increase_eyes.loc[o][c])

#ethnicity
white = increase_eyes[increase_eyes[ethnicity] == 'White'].index.tolist()
black = increase_eyes[increase_eyes[ethnicity] == 'Black'].index.tolist()
hispanic = increase_eyes[increase_eyes[ethnicity] == 'Hispanic'].index.tolist()
asian = increase_eyes[increase_eyes[ethnicity] == 'Asian'].index.tolist()
other_ethnicity = [i for i in range(len(increase_eyes.index)) if i not in white if i not in black if i not in hispanic if i not in asian]


incr_eyes_white = {c:[] for c in columns}
incr_eyes_black = {c:[] for c in columns}
incr_eyes_hispanic = {c:[] for c in columns}
incr_eyes_asian = {c:[] for c in columns}
incr_eyes_other_eth = {c:[] for c in columns}

for c in columns:
    for w in white:
        incr_eyes_white[c].append(increase_eyes.loc[w][c])
    for b in black:
        incr_eyes_black[c].append(increase_eyes.loc[b][c])
    for h in hispanic:
        incr_eyes_hispanic[c].append(increase_eyes.loc[h][c])
    for a in asian:
        incr_eyes_asian[c].append(increase_eyes.loc[a][c])
    for e in other_ethnicity:
        incr_eyes_other_eth[c].append(increase_eyes.loc[e][c])


#sexual preference
hetero = increase_eyes[increase_eyes[so] == 'Heterosexual'].index.tolist()
homo = increase_eyes[increase_eyes[so] == 'Homosexual'].index.tolist()
bi = increase_eyes[increase_eyes[so] == 'Bisexual'].index.tolist()
ace = increase_eyes[(increase_eyes[so] == 'Asexual') & (increase_eyes[so] == 'Aromantic')].index.tolist()
other_so = [i for i in range(len(increase_eyes.index)) if i not in hetero if i not in homo if i not in bi if i not in ace]

incr_eyes_hetero = {c:[] for c in columns}
incr_eyes_homo = {c:[] for c in columns}
incr_eyes_bi = {c:[] for c in columns}
incr_eyes_ace = {c:[] for c in columns}
incr_eyes_other_so = {c:[] for c in columns}

for c in columns:
    for h in hetero:
        incr_eyes_hetero[c].append(increase_eyes.loc[h][c])
    for o in homo:
        incr_eyes_homo[c].append(increase_eyes.loc[o][c])
    for b in bi:
        incr_eyes_bi[c].append(increase_eyes.loc[b][c])
    for a in ace:
        incr_eyes_ace[c].append(increase_eyes.loc[a][c])
    for e in other_so:
        incr_eyes_other_so[c].append(increase_eyes.loc[e][c])



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