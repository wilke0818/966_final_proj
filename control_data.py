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

control_data = pd.read_excel('Final Project\Control.xlsx')
# index of each category

#gender
female = control_data[control_data[gender] == 'Female'].index.tolist()
male = control_data[control_data[gender] == 'Male'].index.tolist()
other = [i for i in range(len(control_data.index)) if i not in female if i not in male]

#dict of category: rating for each
control_female = {c:[] for c in columns}
control_male = {c:[] for c in columns}
control_other = {c:[] for c in columns}

for c in columns:
    for f in female:
        control_female[c].append(control_data.loc[f][c])
    for m in male:
        control_male[c].append(control_data.loc[m][c])
    for o in other:
        control_other[c].append(control_data.loc[o][c])

#ethnicity
white = control_data[control_data[ethnicity] == 'White'].index.tolist()
black = control_data[control_data[ethnicity] == 'Black'].index.tolist()
hispanic = control_data[control_data[ethnicity] == 'Hispanic'].index.tolist()
asian = control_data[control_data[ethnicity] == 'Asian'].index.tolist()
other_ethnicity = [i for i in range(len(control_data.index)) if i not in white if i not in black if i not in hispanic if i not in asian]


control_white = {c:[] for c in columns}
control_black = {c:[] for c in columns}
control_hispanic = {c:[] for c in columns}
control_asian = {c:[] for c in columns}
control_other_eth = {c:[] for c in columns}

for c in columns:
    for w in white:
        control_white[c].append(control_data.loc[w][c])
    for b in black:
        control_black[c].append(control_data.loc[b][c])
    for h in hispanic:
        control_hispanic[c].append(control_data.loc[h][c])
    for a in asian:
        control_asian[c].append(control_data.loc[a][c])
    for e in other_ethnicity:
        control_other_eth[c].append(control_data.loc[e][c])


#sexual preference
hetero = control_data[control_data[so] == 'Heterosexual'].index.tolist()
homo = control_data[control_data[so] == 'Homosexual'].index.tolist()
bi = control_data[control_data[so] == 'Bisexual'].index.tolist()
ace = control_data[(control_data[so] == 'Asexual') & (control_data[so] == 'Aromantic')].index.tolist()
other_so = [i for i in range(len(control_data.index)) if i not in hetero if i not in homo if i not in bi if i not in ace]

control_hetero = {c:[] for c in columns}
control_homo = {c:[] for c in columns}
control_bi = {c:[] for c in columns}
control_ace = {c:[] for c in columns}
control_other_so = {c:[] for c in columns}

for c in columns:
    for h in hetero:
        control_hetero[c].append(control_data.loc[h][c])
    for o in homo:
        control_homo[c].append(control_data.loc[o][c])
    for b in bi:
        control_bi[c].append(control_data.loc[b][c])
    for a in ace:
        control_ace[c].append(control_data.loc[a][c])
    for e in other_so:
        control_other_so[c].append(control_data.loc[e][c])


# for c in control_female:
#     plt.hist(np.array(control_female[c]))
#     plt.show()

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