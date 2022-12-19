import csv
import numpy as np
import matplotlib.pyplot as plt

def contain(words, searchString):
    for word in words:
        if searchString in word: return True

    return False


is_first = True

data = {"control": [], "increased_eyes": [], "increased_jaw": [], "decreased_eyes": [], "decreased_jaw": []}

with open('control.csv', newline='') as control_csv:
    control_data = csv.reader(control_csv, delimiter=',', quotechar='\"')
    for row in control_data:
        if is_first:
            is_first = False 
            continue
        gender = np.array([i.strip() for i in row[1].lower().split(',')])
        ethnicity = np.array([i.strip() for i in row[2].lower().split(',')])
        sexuality = np.array([i.strip() for i in row[3].lower().split(',')])
        face_ratings = np.array([int(rating) for rating in row[4:12]])
        data['control'].append({'gender': gender, 'ethnicity': ethnicity, 'sexuality': sexuality, 'ratings': face_ratings})

g_control = set([g for x in data['control'] for g in x['gender']])
e_control = set([e for x in data['control'] for e in x['ethnicity']])
s_control = set([s for x in data['control'] for s in x['sexuality']])
is_first = True

with open('decreased_eyes.csv', newline='') as decreased_eyes_csv:
    decreased_eyes_data = csv.reader(decreased_eyes_csv, delimiter=',', quotechar='\"')
    for row in decreased_eyes_data:
        if is_first:
            is_first = False 
            continue
        gender = np.array([i.strip() for i in row[1].lower().split(',')])
        ethnicity = np.array([i.strip() for i in row[2].lower().split(',')])
        sexuality = np.array([i.strip() for i in row[3].lower().split(',')])
        face_ratings = np.array([int(rating) for rating in row[4:12]])
        data['decreased_eyes'].append({'gender': gender, 'ethnicity': ethnicity, 'sexuality': sexuality, 'ratings': face_ratings})

g_deyes = set([g for x in data['decreased_eyes'] for g in x['gender']])
e_deyes = set([e for x in data['decreased_eyes'] for e in x['ethnicity']])
s_deyes = set([s for x in data['decreased_eyes'] for s in x['sexuality']])
is_first = True

with open('decreased_jaw.csv', newline='') as decreased_jaw_csv:
    decreased_jaw_data = csv.reader(decreased_jaw_csv, delimiter=',', quotechar='\"')
    for row in decreased_jaw_data:
        if is_first:
            is_first = False 
            continue
        gender = np.array([i.strip() for i in row[1].lower().split(',')])
        ethnicity = np.array([i.strip() for i in row[2].lower().split(',')])
        sexuality = np.array([i.strip() for i in row[3].lower().split(',')])
        face_ratings = np.array([int(rating) for rating in row[4:12]])
        data['decreased_jaw'].append({'gender': gender, 'ethnicity': ethnicity, 'sexuality': sexuality, 'ratings': face_ratings})

g_djaw = set([g for x in data['decreased_jaw'] for g in x['gender']])
e_djaw = set([e for x in data['decreased_jaw'] for e in x['ethnicity']])
s_djaw = set([s for x in data['decreased_jaw'] for s in x['sexuality']])
is_first = True

with open('increased_eyes.csv', newline='') as increased_eyes_csv:
    increased_eyes_data = csv.reader(increased_eyes_csv, delimiter=',', quotechar='\"')
    for row in increased_eyes_data:
        if is_first:
            is_first = False 
            continue
        gender = np.array([i.strip() for i in row[1].lower().split(',')])
        ethnicity = np.array([i.strip() for i in row[2].lower().split(',')])
        sexuality = np.array([i.strip() for i in row[3].lower().split(',')])
        face_ratings = np.array([int(rating) for rating in row[4:12]])
        data['increased_eyes'].append({'gender': gender, 'ethnicity': ethnicity, 'sexuality': sexuality, 'ratings': face_ratings})

g_ieyes = set([g for x in data['increased_eyes'] for g in x['gender']])
e_ieyes = set([e for x in data['increased_eyes'] for e in x['ethnicity']])
s_ieyes = set([s for x in data['increased_eyes'] for s in x['sexuality']])
is_first = True

with open('increased_jaw.csv', newline='') as increased_jaw_csv:
    increased_jaw_data = csv.reader(increased_jaw_csv, delimiter=',', quotechar='\"')
    for row in increased_jaw_data:
        if is_first:
            is_first = False 
            continue
        gender = np.array([i.strip() for i in row[1].lower().split(',')])
        ethnicity = np.array([i.strip() for i in row[2].lower().split(',')])
        sexuality = np.array([i.strip() for i in row[3].lower().split(',')])
        face_ratings = np.array([int(rating) for rating in row[4:12]])
        data['increased_jaw'].append({'gender': gender, 'ethnicity': ethnicity, 'sexuality': sexuality, 'ratings': face_ratings})

g_ijaw = set([g for x in data['increased_jaw'] for g in x['gender']])
e_ijaw = set([e for x in data['increased_jaw'] for e in x['ethnicity']])
s_ijaw = set([s for x in data['increased_jaw'] for s in x['sexuality']])

# for k in data.keys():
#     print(len(data[k]))

#Gives a better idea of what choices were used for others/not all forms used the same phrasing/spelling

# print(g_control.union(g_deyes).union(g_djaw).union( g_ieyes).union( g_ijaw))
# print(e_control.union(e_deyes).union(e_djaw).union(e_ieyes).union(e_ijaw))
# print(s_control.union(s_deyes).union(s_djaw).union(s_ieyes).union( s_ijaw))

stats = {}




for test_type in data.keys():
    stats[test_type] = {}
    #Gender variables
    male = {'vals': [[],[],[],[],[],[],[],[]]}
    female = {'vals': [[],[],[],[],[],[],[],[]]}
    # Non-binary response rate too low to use; averaging with other non male/female identifying individuals and unspecified response
    # nonb = {'sum': [0]*8}
    other_g = {'vals': [[],[],[],[],[],[],[],[]]}

    #Ethnicity variables
    white = {'vals': [[],[],[],[],[],[],[],[]]}
    black = {'vals': [[],[],[],[],[],[],[],[]]}
    # Response rate too low between different sub-ethnicities of what is generally considered Asian so combining together
    asian = {'vals': [[],[],[],[],[],[],[],[]]}
    hispanic = {'vals': [[],[],[],[],[],[],[],[]]}
    other_e = {'vals': [[],[],[],[],[],[],[],[]]}

    #Sexuality variables
    homo = {'vals': [[],[],[],[],[],[],[],[]]}
    hetero = {'vals': [[],[],[],[],[],[],[],[]]}
    bi = {'vals': [[],[],[],[],[],[],[],[]]}
    ace = {'vals': [[],[],[],[],[],[],[],[]]}
    # a combination of non-heteros
    queer = {'vals': [[],[],[],[],[],[],[],[]]}
    other_s = {'vals': [[],[],[],[],[],[],[],[]]}

    for response in data[test_type]:
        #gender
        if contain(response['gender'], 'male') and not contain(response['gender'], 'female'):
            for i in range(len(response['ratings'])):
                male['vals'][i].append(response['ratings'][i])
        if contain(response['gender'], 'female'):
            for i in range(len(response['ratings'])):
                female['vals'][i].append(response['ratings'][i])
        if not contain(response['gender'], 'female') and not contain(response['gender'], 'male'):
            for i in range(len(response['ratings'])):
                other_g['vals'][i].append(response['ratings'][i])
        
        #ethnicity
        if contain(response['ethnicity'], 'white') or contain(response['ethnicity'], 'european') or contain(response['ethnicity'], 'slavic'):
            for i in range(len(response['ratings'])):
                white['vals'][i].append(response['ratings'][i])
        if contain(response['ethnicity'], 'black'):
            for i in range(len(response['ratings'])):
                black['vals'][i].append(response['ratings'][i])
        if contain(response['ethnicity'], 'hispanic') or contain(response['ethnicity'], 'latinx'):
            for i in range(len(response['ratings'])):
                hispanic['vals'][i].append(response['ratings'][i])
        if contain(response['ethnicity'], 'asian') or contain(response['ethnicity'], 'indian') or contain(response['ethnicity'], 'chinese'):
            for i in range(len(response['ratings'])):
                asian['vals'][i].append(response['ratings'][i])
        if not contain(response['ethnicity'], 'asian') and not contain(response['ethnicity'], 'indian') and not contain(response['ethnicity'], 'chinese') and \
            not contain(response['ethnicity'], 'hispanic') and not contain(response['ethnicity'], 'latinx') and not contain(response['ethnicity'], 'black') and \
            not contain(response['ethnicity'], 'white') and not contain(response['ethnicity'], 'european') and not contain(response['ethnicity'], 'slavic'):
            for i in range(len(response['ratings'])):
                other_e['vals'][i].append(response['ratings'][i])
        
        #Sexuality
        if contain(response['sexuality'], 'hetero'):
            for i in range(len(response['ratings'])):
                hetero['vals'][i].append(response['ratings'][i])
        if (contain(response['sexuality'], 'homo') and not contain(response['sexuality'], 'homoromantic')) or contain(response['sexuality'], 'gay') or contain(response['sexuality'], 'lesbian'):
            for i in range(len(response['ratings'])):
                homo['vals'][i].append(response['ratings'][i])
        if ((contain(response['sexuality'], 'bi') or contain(response['sexuality'], 'pan')) and not (contain(response['sexuality'], 'biromantic') or contain(response['sexuality'], 'panromantic'))):
            for i in range(len(response['ratings'])):
                bi['vals'][i].append(response['ratings'][i])
        if contain(response['sexuality'], 'asexual') or contain(response['sexuality'], 'demi') or (contain(response['sexuality'], 'romantic') and not contain(response['sexuality'], 'sexual')):
            for i in range(len(response['ratings'])):
                ace['vals'][i].append(response['ratings'][i])
        if contain(response['sexuality'], 'queer'):
            for i in range(len(response['ratings'])):
                queer['vals'][i].append(response['ratings'][i])
        if not (contain(response['sexuality'], 'asexual') or contain(response['sexuality'], 'demi') or (contain(response['sexuality'], 'romantic') and not contain(response['sexuality'], 'sexual')) or \
            ((contain(response['sexuality'], 'bi') or contain(response['sexuality'], 'pan')) and not (contain(response['sexuality'], 'biromantic') or contain(response['sexuality'], 'panromantic'))) or \
                (contain(response['sexuality'], 'homo') and not contain(response['sexuality'], 'homoromantic')) or contain(response['sexuality'], 'gay') or contain(response['sexuality'], 'lesbian') or \
                    contain(response['sexuality'], 'hetero') or contain(response['sexuality'], 'queer')):
            for i in range(len(response['ratings'])):
                other_s['vals'][i].append(response['ratings'][i])
    
    for i in range(len(homo['vals'])):
        for j in range(len(homo['vals'][i])):
            queer['vals'][i].append(homo['vals'][i][j])
    
    for i in range(len(bi['vals'])):
        for j in range(len(bi['vals'][i])):
            queer['vals'][i].append(bi['vals'][i][j])
    
    for i in range(len(ace['vals'])):
        for j in range(len(ace['vals'][i])):
            queer['vals'][i].append(ace['vals'][i][j])

    stats[test_type].update({'gender': {'male': male, 'female': female, 'other': other_g}})
    stats[test_type].update({'ethnicity': {'white': white, 'black': black, 'asian': asian, 'hispanic': hispanic, 'other': other_e}})
    stats[test_type].update({'sexuality': {'heterosexual': hetero, 'homosexual': homo, 'bisexual': bi, 'asexual': ace, 'other': other_s, 'queer': queer}})

# print(stats)
for experiment in stats.keys():
    for cat in stats[experiment].keys():
        for subcat in stats[experiment][cat].keys():
            stats[experiment][cat][subcat]['averages'] = np.average(stats[experiment][cat][subcat]['vals'], axis=1)
            stats[experiment][cat][subcat]['std'] = np.std(stats[experiment][cat][subcat]['vals'], axis=1)

for experiment in stats.keys():
    print(experiment)
    for cat in stats[experiment].keys():
        print(" ",cat)
        for subcat in stats[experiment][cat].keys():
            print("  ", subcat, stats[experiment][cat][subcat]['averages'], '+/-', stats[experiment][cat][subcat]['std'])
            


# set width of bar
barWidth = 0.1
# fig, axs = plt.subplots(figsize =(12, 8))
 
avg_keys = None
# set height of bars
for face_idx in range(1):
    fig, axs = plt.subplots(figsize =(14, 10))
    avg_keys = stats.keys()

    male_avg = [stats[face_var]['gender']['male']['averages'][face_idx] for face_var in avg_keys]
    # male_std = [stats[face_var]['gender']['male']['std'][face_idx] for face_var in stats.keys()]
    female_avg = [stats[face_var]['gender']['female']['averages'][face_idx] for face_var in avg_keys]
    # female_std = [stats[face_var]['gender']['female']['std'][face_idx] for face_var in stats.keys()]
    g_other_avg = [stats[face_var]['gender']['other']['averages'][face_idx] for face_var in avg_keys]
    # g_other_std = [stats[face_var]['gender']['other']['std'][face_idx] for face_var in stats.keys()]

    white_avg = [stats[face_var]['ethnicity']['white']['averages'][face_idx] for face_var in avg_keys]
    # white_std = [stats[face_var]['ethnicity']['white']['std'][face_idx] for face_var in stats.keys()]
    black_avg = [stats[face_var]['ethnicity']['black']['averages'][face_idx] for face_var in avg_keys]
    # black_std = [stats[face_var]['ethnicity']['black']['std'][face_idx] for face_var in stats.keys()]
    hispanic_avg = [stats[face_var]['ethnicity']['hispanic']['averages'][face_idx] for face_var in avg_keys]
    # hispanic_std = [stats[face_var]['ethnicity']['hispanic']['std'][face_idx] for face_var in stats.keys()]
    asian_avg = [stats[face_var]['ethnicity']['asian']['averages'][face_idx] for face_var in avg_keys]
    # asian_std = [stats[face_var]['ethnicity']['asian']['std'][face_idx] for face_var in stats.keys()]
    e_other_avg = [stats[face_var]['ethnicity']['other']['averages'][face_idx] for face_var in avg_keys]
    # e_other_std = [stats[face_var]['ethnicity']['other']['std'][face_idx] for face_var in stats.keys()]

    homo_avg = [stats[face_var]['sexuality']['homosexual']['averages'][face_idx] for face_var in avg_keys]
    # homo_std = [stats[face_var]['sexuality']['homosexual']['std'][face_idx] for face_var in stats.keys()]
    hetero_avg = [stats[face_var]['sexuality']['heterosexual']['averages'][face_idx] for face_var in avg_keys]
    # hetero_std = [stats[face_var]['sexuality']['heterosexual']['std'][face_idx] for face_var in stats.keys()]
    bi_avg = [stats[face_var]['sexuality']['bisexual']['averages'][face_idx] for face_var in avg_keys]
    # bi_std = [stats[face_var]['sexuality']['bisexual']['std'][face_idx] for face_var in stats.keys()]
    ace_avg = [stats[face_var]['sexuality']['asexual']['averages'][face_idx] for face_var in avg_keys]
    # ace_std = [stats[face_var]['sexuality']['asexual']['std'][face_idx] for face_var in stats.keys()]
    queer_avg = [stats[face_var]['sexuality']['queer']['averages'][face_idx] for face_var in avg_keys]
    # queer_std = [stats[face_var]['sexuality']['queer']['std'][face_idx] for face_var in stats.keys()]
    s_other_avg = [stats[face_var]['sexuality']['other']['averages'][face_idx] for face_var in avg_keys]
    # s_other_std = [stats[face_var]['sexuality']['other']['std'][face_idx] for face_var in stats.keys()]
    exps_names = [face_var for face_var in avg_keys]

    exps = []
    for i in range(5):
        exps.append([
            male_avg[i], 
            female_avg[i], 
            g_other_avg[i], 
            white_avg[i],
            black_avg[i],
            asian_avg[i],
            hispanic_avg[i],
            e_other_avg[i],
            homo_avg[i],
            hetero_avg[i],
            bi_avg[i],
            ace_avg[i],
            queer_avg[i],
            s_other_avg[i]
        ])
    

    br1 = np.arange(14)
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    # br6 = [x + barWidth for x in br5]
    # br7 = [x + barWidth for x in br6]
    # br8 = [x + barWidth for x in br7]
    # br9 = [x + barWidth for x in br8]
    # br10 = [x + barWidth for x in br9]
    # br11 = [x + barWidth for x in br10]
    # br12 = [x + barWidth for x in br11]
    # br13 = [x + barWidth for x in br12]
    # br14 = [x + barWidth for x in br13]

    axs.bar(br1, exps[0], color ='C0', width = barWidth,
            edgecolor ='grey', label =exps_names[0])
    axs.bar(br2, exps[1], color ='C1', width = barWidth,
            edgecolor ='grey', label = exps_names[1])
    axs.bar(br3, exps[2], color ='C2', width = barWidth,
            edgecolor ='grey', label = exps_names[2])
    axs.bar(br4, exps[3], color ='C3', width = barWidth,
            edgecolor ='grey', label = exps_names[3])
    axs.bar(br5, exps[4], color ='C4', width = barWidth,
            edgecolor ='grey', label = exps_names[4])

    # axs.bar(br1, male_avg, color ='C0', width = barWidth,
    #         edgecolor ='grey', label ='Male')
    # axs.bar(br2, female_avg, color ='C1', width = barWidth,
    #         edgecolor ='grey', label ='Female')
    # axs.bar(br3, g_other_avg, color ='C2', width = barWidth,
    #         edgecolor ='grey', label ='Other gender')
    # axs.bar(br4, white_avg, color ='C3', width = barWidth,
    #         edgecolor ='grey', label ='White')
    # axs.bar(br5, black_avg, color ='C4', width = barWidth,
    #         edgecolor ='grey', label ='Black')
    # axs.bar(br6, asian_avg, color ='C5', width = barWidth,
    #         edgecolor ='grey', label ='Asian', yerr=asian_std)
    # axs.bar(br7, hispanic_avg, color ='C6', width = barWidth,
    #         edgecolor ='grey', label ='Hispanic', yerr=hispanic_std)
    # axs.bar(br8, e_other_avg, color ='C7', width = barWidth,
    #         edgecolor ='grey', label ='Other Ethnicity', yerr=e_other_std)
    # axs.bar(br9, hetero_avg, color ='C8', width = barWidth,
    #         edgecolor ='grey', label ='Heterosexual', yerr=hetero_std)
    # axs.bar(br10, homo_avg, color ='C9', width = barWidth,
    #         edgecolor ='grey', label ='Homosexual', yerr=homo_std)
    # axs.bar(br11, bi_avg, color ='C10', width = barWidth,
    #         edgecolor ='grey', label ='Bisexual', yerr=bi_std)
    # axs.bar(br12, ace_avg, color ='C11', width = barWidth,
    #         edgecolor ='grey', label ='Asexual', yerr=ace_std)
    # axs.bar(br13, queer_avg, color ='C12', width = barWidth,
    #         edgecolor ='grey', label ='Queer', yerr=queer_std)
    # axs.bar(br14, s_other_avg, color ='C13', width = barWidth,
    #         edgecolor ='grey', label ='Other sexuality', yerr=s_other_std)

 
# Adding Xticks
# plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
# plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
# plt.xticks([r + barWidth for r in range(len(IT))],
#         ['2015', '2016', '2017', '2018', '2019'])
 
plt.legend()
plt.show()