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

dec_eyes_data = pd.read_excel('Final Project\Decrease Eyes.xlsx')
# index of each category

#gender
female = dec_eyes_data[dec_eyes_data[gender] == 'Female'].index.tolist()
male = dec_eyes_data[dec_eyes_data[gender] == 'Male'].index.tolist()
other = [i for i in range(len(dec_eyes_data.index)) if i not in female if i not in male]

#dict of category: rating for each
dec_eyes_female = {c:[] for c in columns}
dec_eyes_male = {c:[] for c in columns}
dec_eyes_other = {c:[] for c in columns}

for c in columns:
    for f in female:
        dec_eyes_female[c].append(dec_eyes_data.loc[f][c])
    for m in male:
        dec_eyes_male[c].append(dec_eyes_data.loc[m][c])
    for o in other:
        dec_eyes_other[c].append(dec_eyes_data.loc[o][c])

#ethnicity
white = dec_eyes_data[dec_eyes_data[ethnicity] == 'White'].index.tolist()
black = dec_eyes_data[dec_eyes_data[ethnicity] == 'Black'].index.tolist()
hispanic = dec_eyes_data[dec_eyes_data[ethnicity] == 'Hispanic'].index.tolist()
asian = dec_eyes_data[dec_eyes_data[ethnicity] == 'Asian'].index.tolist()
other_ethnicity = [i for i in range(len(dec_eyes_data.index)) if i not in white if i not in black if i not in hispanic if i not in asian]


dec_eyes_white = {c:[] for c in columns}
dec_eyes_black = {c:[] for c in columns}
dec_eyes_hispanic = {c:[] for c in columns}
dec_eyes_asian = {c:[] for c in columns}
dec_eyes_other_eth = {c:[] for c in columns}

for c in columns:
    for w in white:
        dec_eyes_white[c].append(dec_eyes_data.loc[w][c])
    for b in black:
        dec_eyes_black[c].append(dec_eyes_data.loc[b][c])
    for h in hispanic:
        dec_eyes_hispanic[c].append(dec_eyes_data.loc[h][c])
    for a in asian:
        dec_eyes_asian[c].append(dec_eyes_data.loc[a][c])
    for e in other_ethnicity:
        dec_eyes_other_eth[c].append(dec_eyes_data.loc[e][c])


#sexual preference
hetero = dec_eyes_data[dec_eyes_data[so] == 'Heterosexual'].index.tolist()
homo = dec_eyes_data[dec_eyes_data[so] == 'Homosexual'].index.tolist()
bi = dec_eyes_data[dec_eyes_data[so] == 'Bisexual'].index.tolist()
ace = dec_eyes_data[(dec_eyes_data[so] == 'Asexual') & (dec_eyes_data[so] == 'Aromantic')].index.tolist()
other_so = [i for i in range(len(dec_eyes_data.index)) if i not in hetero if i not in homo if i not in bi if i not in ace]

dec_eyes_hetero = {c:[] for c in columns}
dec_eyes_homo = {c:[] for c in columns}
dec_eyes_bi = {c:[] for c in columns}
dec_eyes_ace = {c:[] for c in columns}
dec_eyes_other_so = {c:[] for c in columns}

for c in columns:
    for h in hetero:
        dec_eyes_hetero[c].append(dec_eyes_data.loc[h][c])
    for o in homo:
        dec_eyes_homo[c].append(dec_eyes_data.loc[o][c])
    for b in bi:
        dec_eyes_bi[c].append(dec_eyes_data.loc[b][c])
    for a in ace:
        dec_eyes_ace[c].append(dec_eyes_data.loc[a][c])
    for e in other_so:
        dec_eyes_other_so[c].append(dec_eyes_data.loc[e][c])


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