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

# prior_female_ratings = []
# for img in control_female:
#     prior = []
#     for i in range(1,8):
#         prior.append(control_female[img].count(i)/len(control_female[img]))
#     prior_female_ratings = prior
# # print(prior_female_ratings)


# prior_rating_c1 = []
# prior_rating_c2 = []
# prior_rating_c3 = []
# prior_rating_c4 = []
# prior_rating_c5 = []
# prior_rating_c6 = []
# prior_rating_c7 = []
# prior_rating_c8 = []

# for i in range(1,8):
#     prior_rating_c1.append(list(control_data[c1]).count(i)/len(list(control_data[c1])))
#     prior_rating_c2.append(list(control_data[c2]).count(i)/len(list(control_data[c2])))
#     prior_rating_c3.append(list(control_data[c3]).count(i)/len(list(control_data[c3])))
#     prior_rating_c4.append(list(control_data[c4]).count(i)/len(list(control_data[c4])))
#     prior_rating_c5.append(list(control_data[c5]).count(i)/len(list(control_data[c5])))
#     prior_rating_c6.append(list(control_data[c6]).count(i)/len(list(control_data[c6])))
#     prior_rating_c7.append(list(control_data[c7]).count(i)/len(list(control_data[c7])))
#     prior_rating_c8.append(list(control_data[c8]).count(i)/len(list(control_data[c8])))

control1 = list(control_data[c1])
control2 = list(control_data[c2])
control3 = list(control_data[c3])
control4 = list(control_data[c4])
control5 = list(control_data[c5])
control6 = list(control_data[c6])
control7 = list(control_data[c7])
control8 = list(control_data[c8])

#score avg for all data
score_avg_c1 = sum(control1)/len(control1)
score_avg_c2 = sum(control2)/len(control2)
score_avg_c3 = sum(control3)/len(control3)
score_avg_c4 = sum(control4)/len(control4)
score_avg_c5 = sum(control5)/len(control5)
score_avg_c6 = sum(control6)/len(control6)
score_avg_c7 = sum(control7)/len(control7)
score_avg_c8 = sum(control8)/len(control8)


avg_c1 = (control1.count(5)+control1.count(6)+control1.count(7))/len(list(control_data[c1]))
avg_c2 = (control2.count(5)+control2.count(6)+control2.count(7))/len(control2)
avg_c3 = sum([control3.count(5),control3.count(6),control3.count(7)])/len(control3)
avg_c4 = sum([control4.count(5),control4.count(6),control4.count(7)])/len(control4)
avg_c5 = sum([control5.count(5),control5.count(6),control5.count(7)])/len(control5)
avg_c6 = sum([control6.count(5),control6.count(6),control6.count(7)])/len(control6)
avg_c7 = sum([control7.count(5),control7.count(6),control7.count(7)])/len(control7)
avg_c8 = sum([control8.count(5),control8.count(6),control8.count(7)])/len(control8)
avg_c = [avg_c1, avg_c2, avg_c3, avg_c4, avg_c5, avg_c6, avg_c7, avg_c8]
# print(avg_c)

##Gender
avg_male_c = (control_male[c1].count(5)+control_male[c1].count(6)+control_male[c1].count(7))/len(control_male[c1])
avg_female_c = (control_female[c1].count(5)+control_female[c1].count(6)+control_female[c1].count(7))/len(control_female[c1])
avg_male_c2 = (control_male[c2].count(5)+control_male[c2].count(6)+control_male[c2].count(7))/len(control_male[c2])
avg_female_c2 = (control_female[c2].count(5)+control_female[c2].count(6)+control_female[c2].count(7))/len(control_female[c2])
avg_male_c3 = (control_male[c3].count(5)+control_male[c3].count(6)+control_male[c3].count(7))/len(control_male[c3])
avg_female_c3 = (control_female[c3].count(5)+control_female[c3].count(6)+control_female[c3].count(7))/len(control_female[c3])
avg_male_c4 = (control_male[c4].count(5)+control_male[c4].count(6)+control_male[c4].count(7))/len(control_male[c4])
avg_female_c4 = (control_female[c4].count(5)+control_female[c4].count(6)+control_female[c4].count(7))/len(control_female[c4])
avg_male_c5 = (control_male[c5].count(5)+control_male[c5].count(6)+control_male[c5].count(7))/len(control_male[c5])
avg_female_c5 = (control_female[c5].count(5)+control_female[c5].count(6)+control_female[c5].count(7))/len(control_female[c5])
avg_male_c6 = (control_male[c6].count(5)+control_male[c6].count(6)+control_male[c6].count(7))/len(control_male[c6])
avg_female_c6 = (control_female[c6].count(5)+control_female[c6].count(6)+control_female[c6].count(7))/len(control_female[c6])
avg_male_c7 = (control_male[c7].count(5)+control_male[c7].count(6)+control_male[c7].count(7))/len(control_male[c7])
avg_female_c7 = (control_female[c7].count(5)+control_female[c7].count(6)+control_female[c7].count(7))/len(control_female[c7])
avg_male_c8 = (control_male[c8].count(5)+control_male[c8].count(6)+control_male[c8].count(7))/len(control_male[c8])
avg_female_c8 = (control_female[c8].count(5)+control_female[c8].count(6)+control_female[c8].count(7))/len(control_female[c8])

#score
male_avg_c1 = sum(control_male[c1])/len(control_male[c1])
male_avg_c2 = sum(control_male[c2])/len(control_male[c2])
male_avg_c3 = sum(control_male[c3])/len(control_male[c3])
male_avg_c4 = sum(control_male[c4])/len(control_male[c4])
male_avg_c5 = sum(control_male[c5])/len(control_male[c5])
male_avg_c6 = sum(control_male[c6])/len(control_male[c6])
male_avg_c7 = sum(control_male[c7])/len(control_male[c7])
male_avg_c8 = sum(control_male[c8])/len(control_male[c8])

female_avg_c1 = sum(control_female[c1])/len(control_female[c1])
female_avg_c2 = sum(control_female[c2])/len(control_female[c2])
female_avg_c3 = sum(control_female[c3])/len(control_female[c3])
female_avg_c4 = sum(control_female[c4])/len(control_female[c4])
female_avg_c5 = sum(control_female[c5])/len(control_female[c5])
female_avg_c6 = sum(control_female[c6])/len(control_female[c6])
female_avg_c7 = sum(control_female[c7])/len(control_female[c7])
female_avg_c8 = sum(control_female[c8])/len(control_female[c8])

#ethnicity
avg_white_c1 =(control_white[c1].count(5) + control_white[c1].count(6) + control_white[c1].count(7))/len(control_white[c1])
avg_white_c2 =(control_white[c2].count(5) + control_white[c2].count(6) + control_white[c2].count(7))/len(control_white[c1])
avg_white_c3 =(control_white[c3].count(5) + control_white[c3].count(6) + control_white[c3].count(7))/len(control_white[c3])
avg_white_c4 =(control_white[c4].count(5) + control_white[c4].count(6) + control_white[c4].count(7))/len(control_white[c4])
avg_white_c5 =(control_white[c5].count(5) + control_white[c5].count(6) + control_white[c5].count(7))/len(control_white[c5])
avg_white_c6 =(control_white[c6].count(5) + control_white[c6].count(6) + control_white[c6].count(7))/len(control_white[c6])
avg_white_c7 =(control_white[c7].count(5) + control_white[c7].count(6) + control_white[c7].count(7))/len(control_white[c7])
avg_white_c8 =(control_white[c8].count(5) + control_white[c8].count(6) + control_white[c8].count(7))/len(control_white[c8])

avg_black_c1 =(control_black[c1].count(5) + control_black[c1].count(6) + control_black[c1].count(7))/len(control_black[c1])
avg_black_c2 =(control_black[c2].count(5) + control_black[c2].count(6) + control_black[c2].count(7))/len(control_black[c2])
avg_black_c3 =(control_black[c3].count(5) + control_black[c3].count(6) + control_black[c3].count(7))/len(control_black[c3])
avg_black_c4 =(control_black[c4].count(5) + control_black[c4].count(6) + control_black[c4].count(7))/len(control_black[c4])
avg_black_c5 =(control_black[c5].count(5) + control_black[c5].count(6) + control_black[c5].count(7))/len(control_black[c5])
avg_black_c6 =(control_black[c6].count(5) + control_black[c6].count(6) + control_black[c6].count(7))/len(control_black[c6])
avg_black_c7 =(control_black[c7].count(5) + control_black[c7].count(6) + control_black[c7].count(7))/len(control_black[c7])
avg_black_c8 =(control_black[c8].count(5) + control_black[c8].count(6) + control_black[c8].count(7))/len(control_black[c8])

avg_asian_c1 =(control_asian[c1].count(5) + control_asian[c1].count(6) + control_asian[c1].count(7))/len(control_asian[c1])
avg_asian_c2 =(control_asian[c2].count(5) + control_asian[c2].count(6) + control_asian[c2].count(7))/len(control_asian[c2])
avg_asian_c3 =(control_asian[c3].count(5) + control_asian[c3].count(6) + control_asian[c3].count(7))/len(control_asian[c3])
avg_asian_c4 =(control_asian[c4].count(5) + control_asian[c4].count(6) + control_asian[c4].count(7))/len(control_asian[c4])
avg_asian_c5 =(control_asian[c5].count(5) + control_asian[c5].count(6) + control_asian[c5].count(7))/len(control_asian[c5])
avg_asian_c6 =(control_asian[c6].count(5) + control_asian[c6].count(6) + control_asian[c6].count(7))/len(control_asian[c6])
avg_asian_c7 =(control_asian[c7].count(5) + control_asian[c7].count(6) + control_asian[c7].count(7))/len(control_asian[c7])
avg_asian_c8 =(control_asian[c8].count(5) + control_asian[c8].count(6) + control_asian[c8].count(7))/len(control_asian[c8])

avg_hispanic_c1 =(control_hispanic[c1].count(5) + control_hispanic[c1].count(6) + control_hispanic[c1].count(7))/len(control_hispanic[c1])
avg_hispanic_c2 =(control_hispanic[c2].count(5) + control_hispanic[c2].count(6) + control_hispanic[c2].count(7))/len(control_hispanic[c2])
avg_hispanic_c3 =(control_hispanic[c3].count(5) + control_hispanic[c3].count(6) + control_hispanic[c3].count(7))/len(control_hispanic[c3])
avg_hispanic_c4 =(control_hispanic[c4].count(5) + control_hispanic[c4].count(6) + control_hispanic[c4].count(7))/len(control_hispanic[c4])
avg_hispanic_c5 =(control_hispanic[c5].count(5) + control_hispanic[c5].count(6) + control_hispanic[c5].count(7))/len(control_hispanic[c5])
avg_hispanic_c6 =(control_hispanic[c6].count(5) + control_hispanic[c6].count(6) + control_hispanic[c6].count(7))/len(control_hispanic[c6])
avg_hispanic_c7 =(control_hispanic[c7].count(5) + control_hispanic[c7].count(6) + control_hispanic[c7].count(7))/len(control_hispanic[c7])
avg_hispanic_c8 =(control_hispanic[c8].count(5) + control_hispanic[c8].count(6) + control_hispanic[c8].count(7))/len(control_hispanic[c8])


## Sexual orientation

avg_hetero_c1 = (control_hetero[c1].count(5) + control_hetero[c1].count(6) + control_hetero[c1].count(7))/len(control_hetero[c1])
avg_hetero_c2 = (control_hetero[c2].count(5) + control_hetero[c2].count(6) + control_hetero[c2].count(7))/len(control_hetero[c2])
avg_hetero_c3 = (control_hetero[c3].count(5) + control_hetero[c3].count(6) + control_hetero[c3].count(7))/len(control_hetero[c3])
avg_hetero_c4 = (control_hetero[c4].count(5) + control_hetero[c4].count(6) + control_hetero[c4].count(7))/len(control_hetero[c4])
avg_hetero_c5 = (control_hetero[c5].count(5) + control_hetero[c5].count(6) + control_hetero[c5].count(7))/len(control_hetero[c5])
avg_hetero_c6 = (control_hetero[c6].count(5) + control_hetero[c6].count(6) + control_hetero[c6].count(7))/len(control_hetero[c6])
avg_hetero_c7 = (control_hetero[c7].count(5) + control_hetero[c7].count(6) + control_hetero[c7].count(7))/len(control_hetero[c7])
avg_hetero_c8 = (control_hetero[c8].count(5) + control_hetero[c8].count(6) + control_hetero[c8].count(7))/len(control_hetero[c8])

avg_homo_c1 = (control_homo[c1].count(5) + control_homo[c1].count(6) + control_homo[c1].count(7))/len(control_homo[c1])
avg_homo_c2 = (control_homo[c2].count(5) + control_homo[c2].count(6) + control_homo[c2].count(7))/len(control_homo[c2])
avg_homo_c3 = (control_homo[c3].count(5) + control_homo[c3].count(6) + control_homo[c3].count(7))/len(control_homo[c3])
avg_homo_c4 = (control_homo[c4].count(5) + control_homo[c4].count(6) + control_homo[c4].count(7))/len(control_homo[c4])
avg_homo_c5 = (control_homo[c5].count(5) + control_homo[c5].count(6) + control_homo[c5].count(7))/len(control_homo[c5])
avg_homo_c6 = (control_homo[c6].count(5) + control_homo[c6].count(6) + control_homo[c6].count(7))/len(control_homo[c6])
avg_homo_c7 = (control_homo[c7].count(5) + control_homo[c7].count(6) + control_homo[c7].count(7))/len(control_homo[c7])
avg_homo_c8 = (control_homo[c8].count(5) + control_homo[c8].count(6) + control_homo[c8].count(7))/len(control_homo[c8])

avg_bi_c1 = (control_bi[c1].count(5) + control_bi[c1].count(6) + control_bi[c1].count(7))/len(control_bi[c1])
avg_bi_c2 = (control_bi[c2].count(5) + control_bi[c2].count(6) + control_bi[c2].count(7))/len(control_bi[c2])
avg_bi_c3 = (control_bi[c3].count(5) + control_bi[c3].count(6) + control_bi[c3].count(7))/len(control_bi[c3])
avg_bi_c4 = (control_bi[c4].count(5) + control_bi[c4].count(6) + control_bi[c4].count(7))/len(control_bi[c4])
avg_bi_c5 = (control_bi[c5].count(5) + control_bi[c5].count(6) + control_bi[c5].count(7))/len(control_bi[c5])
avg_bi_c6 = (control_bi[c6].count(5) + control_bi[c6].count(6) + control_bi[c6].count(7))/len(control_bi[c6])
avg_bi_c7 = (control_bi[c7].count(5) + control_bi[c7].count(6) + control_bi[c7].count(7))/len(control_bi[c7])
avg_bi_c8 = (control_bi[c8].count(5) + control_bi[c8].count(6) + control_bi[c8].count(7))/len(control_bi[c8])

#priors for sexuality
total = len(control_hetero[c1]) + len(control_homo[c1]) + len(control_bi[c1])
prior_heter = len(control_hetero[c1])/total
prior_homo = len(control_homo[c1])/total
prior_bi = len(control_bi[c1])/total
# print(prior_heter)
# print(prior_homo)
# print(prior_bi)
# print(prior_rating_c1)
# print(prior_rating_c2)
# print(prior_rating_c3)
# print(prior_rating_c4)
# print(prior_rating_c5)
# print(prior_rating_c6)
# print(prior_rating_c7)
# print(prior_rating_c8)

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
