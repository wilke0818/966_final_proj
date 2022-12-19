import control_data 
import increase_eyes_data
import increase_jawline_data
import decrease_eyes_data
import decrease_jawline_data
from matplotlib import pyplot as plt


# gender
#prior
prior_male = 0.52
prior_female = 0.48

#likelihood
likelihood_male = control_data.avg_male_c
likelihood_female = control_data.avg_female_c
c2_like_m = control_data.avg_male_c2
c2_like_f = control_data.avg_female_c2
c3_like_m = control_data.avg_male_c3
c3_like_f = control_data.avg_female_c3
c4_like_m = control_data.avg_male_c4
c4_like_f = control_data.avg_female_c4
c5_like_m = control_data.avg_male_c5
c5_like_f = control_data.avg_female_c5
c6_like_m = control_data.avg_male_c6
c6_like_f = control_data.avg_female_c6
c7_like_m = control_data.avg_male_c7
c7_like_f = control_data.avg_female_c7
c8_like_m = control_data.avg_male_c8
c8_like_f = control_data.avg_female_c8

# likelihood_male = control_data.male_avg_c1/7
# likelihood_female = control_data.female_avg_c1/7

# c2_like_m = control_data.male_avg_c2/7
# c2_like_f = control_data.female_avg_c2/7

# c3_like_m = control_data.male_avg_c3/7
# c3_like_f = control_data.female_avg_c3/7

# c4_like_m = control_data.male_avg_c4/7
# c4_like_f = control_data.female_avg_c4/7

# c5_like_m = control_data.male_avg_c5/7
# c5_like_f = control_data.female_avg_c5/7

# c6_like_m = control_data.male_avg_c6/7
# c6_like_f = control_data.female_avg_c6/7

# c7_like_m = control_data.male_avg_c7/7
# c7_like_f = control_data.female_avg_c7/7

# c8_like_m = control_data.male_avg_c8/7
# c8_like_f = control_data.female_avg_c8/7

#marginal prob for each img
marginal = sum([likelihood_male*prior_male, likelihood_female*prior_female])
marginalc2 = c2_like_f*prior_female + c2_like_m*prior_male
marginalc3 = c3_like_f*prior_female + c3_like_m*prior_male
marginalc4 = c4_like_f*prior_female + c4_like_m*prior_male
marginalc5 = c5_like_f*prior_female + c5_like_m*prior_male
marginalc6 = c6_like_f*prior_female + c6_like_m*prior_male
marginalc7 = c7_like_f*prior_female + c7_like_m*prior_male
marginalc8 = c8_like_f*prior_female + c8_like_m*prior_male

#posterior for each img and given gender
posterior_male = (likelihood_male * prior_male)/marginal
c2_post_m = (c2_like_m*prior_male)/marginalc2
c3_post_m = (c3_like_m*prior_male)/marginalc3
c4_post_m = (c4_like_m*prior_male)/marginalc4
c5_post_m = (c5_like_m*prior_male)/marginalc5
c6_post_m = (c6_like_m*prior_male)/marginalc6
c7_post_m = (c7_like_m*prior_male)/marginalc7
c8_post_m = (c8_like_m*prior_male)/marginalc8
posterior_female = (likelihood_female * prior_female)/marginal
c2_post_f = (c2_like_f*prior_female)/marginalc2
c3_post_f = (c3_like_f*prior_female)/marginalc3
c4_post_f = (c4_like_f*prior_female)/marginalc4
c5_post_f = (c5_like_f*prior_female)/marginalc5
c6_post_f = (c6_like_f*prior_female)/marginalc6
c7_post_f = (c7_like_f*prior_female)/marginalc7
c8_post_f = (c8_like_f*prior_female)/marginalc8

#graph
# label = ['F(WM)', 'M(WM)', 'F(AF)', 'M(AF)', 'F(WF)', 'M(WF)', 'F(BF)', 'M(BF)', 'F(LM)', 'M(LM)', 'F(BM)', 'M(BM)', 'F(AM)', 'M(AM)', 'F(LF)', 'M(LF)']
# data = [posterior_female, posterior_male, c2_post_f, c2_post_m, c3_post_f, c3_post_m, c4_post_f, c4_post_m, c5_post_f, c5_post_m, c6_post_f, c6_post_m, c7_post_f, c7_post_m, c8_post_f, c8_post_m]

plt.bar(['F(WM)', 'M(WM)'], [posterior_female, posterior_male], color='blue')
plt.bar(['F(AF)', 'M(AF)'], [c2_post_f, c2_post_m], color='red')
plt.bar(['F(WF)', 'M(WF)'], [c3_post_f, c3_post_m], color='yellow')
plt.bar(['F(BF)', 'M(BF)'], [c4_post_f, c4_post_m], color='orange')
plt.bar(['F(LM)', 'M(LM)'], [c5_post_f, c5_post_m], color='purple')
plt.bar(['F(BM)', 'M(BM)'], [c6_post_f, c6_post_m], color='cyan')
plt.bar(['F(AM)', 'M(AM)'], [c7_post_f, c7_post_m], color='pink')
plt.bar(['F(LF)', 'M(LF)'], [c8_post_f, c8_post_m], color='black')

# plt.bar(label, data)
# plt.xlabel('Gender(image gender and ethnicity)')
plt.ylabel('P(gender|finds image attractive)')
plt.show()



# Ethnicity
# priors
prior_white = 0.3148
prior_asian = 0.4066
prior_hispanic = 0.1952
prior_black = 0.0832

#likelihood
c1_w_like = control_data.avg_white_c1
c2_w_like = control_data.avg_white_c2
c3_w_like = control_data.avg_white_c3
c4_w_like = control_data.avg_white_c4
c5_w_like = control_data.avg_white_c5
c6_w_like = control_data.avg_white_c6
c7_w_like = control_data.avg_white_c7
c8_w_like = control_data.avg_white_c8

c1_a_like = control_data.avg_asian_c1
c2_a_like = control_data.avg_asian_c2
c3_a_like = control_data.avg_asian_c3
c4_a_like = control_data.avg_asian_c4
c5_a_like = control_data.avg_asian_c5
c6_a_like = control_data.avg_asian_c6
c7_a_like = control_data.avg_asian_c7
c8_a_like = control_data.avg_asian_c8

c1_b_like = control_data.avg_black_c1
c2_b_like = control_data.avg_black_c2
c3_b_like = control_data.avg_black_c3
c4_b_like = control_data.avg_black_c4
c5_b_like = control_data.avg_black_c5
c6_b_like = control_data.avg_black_c6
c7_b_like = control_data.avg_black_c7
c8_b_like = control_data.avg_black_c8

c1_h_like = control_data.avg_hispanic_c1
c2_h_like = control_data.avg_hispanic_c2
c3_h_like = control_data.avg_hispanic_c3
c4_h_like = control_data.avg_hispanic_c4
c5_h_like = control_data.avg_hispanic_c5
c6_h_like = control_data.avg_hispanic_c6
c7_h_like = control_data.avg_hispanic_c7
c8_h_like = control_data.avg_hispanic_c8

# marginal prob for each img
marginal_c1_ethnicity = c1_w_like*prior_white + c1_a_like*prior_asian + c1_b_like*prior_black + c1_h_like*prior_hispanic
marginal_c2_ethnicity = c2_w_like*prior_white + c2_a_like*prior_asian + c2_b_like*prior_black + c2_h_like*prior_hispanic
marginal_c3_ethnicity = c3_w_like*prior_white + c3_a_like*prior_asian + c3_b_like*prior_black + c3_h_like*prior_hispanic
marginal_c4_ethnicity = c4_w_like*prior_white + c4_a_like*prior_asian + c4_b_like*prior_black + c4_h_like*prior_hispanic
marginal_c5_ethnicity = c5_w_like*prior_white + c5_a_like*prior_asian + c5_b_like*prior_black + c5_h_like*prior_hispanic
marginal_c6_ethnicity = c6_w_like*prior_white + c6_a_like*prior_asian + c6_b_like*prior_black + c6_h_like*prior_hispanic
marginal_c7_ethnicity = c7_w_like*prior_white + c7_a_like*prior_asian + c7_b_like*prior_black + c7_h_like*prior_hispanic
marginal_c8_ethnicity = c8_w_like*prior_white + c8_a_like*prior_asian + c8_b_like*prior_black + c8_h_like*prior_hispanic

#posterior calculations
c1_w_post = (c1_w_like*prior_white)/marginal_c1_ethnicity
c2_w_post = (c2_w_like*prior_white)/marginal_c2_ethnicity
c3_w_post = (c3_w_like*prior_white)/marginal_c3_ethnicity
c4_w_post = (c4_w_like*prior_white)/marginal_c4_ethnicity
c5_w_post = (c5_w_like*prior_white)/marginal_c5_ethnicity
c6_w_post = (c6_w_like*prior_white)/marginal_c6_ethnicity
c7_w_post = (c7_w_like*prior_white)/marginal_c7_ethnicity
c8_w_post = (c8_w_like*prior_white)/marginal_c8_ethnicity

c1_a_post = (c1_a_like*prior_asian)/marginal_c1_ethnicity
c2_a_post = (c2_a_like*prior_asian)/marginal_c2_ethnicity
c3_a_post = (c3_a_like*prior_asian)/marginal_c3_ethnicity
c4_a_post = (c4_a_like*prior_asian)/marginal_c4_ethnicity
c5_a_post = (c5_a_like*prior_asian)/marginal_c5_ethnicity
c6_a_post = (c6_a_like*prior_asian)/marginal_c6_ethnicity
c7_a_post = (c7_a_like*prior_asian)/marginal_c7_ethnicity
c8_a_post = (c8_a_like*prior_asian)/marginal_c8_ethnicity

c1_b_post = (c1_b_like*prior_black)/marginal_c1_ethnicity
c2_b_post = (c2_b_like*prior_black)/marginal_c2_ethnicity
c3_b_post = (c3_b_like*prior_black)/marginal_c3_ethnicity
c4_b_post = (c4_b_like*prior_black)/marginal_c4_ethnicity
c5_b_post = (c5_b_like*prior_black)/marginal_c5_ethnicity
c6_b_post = (c6_b_like*prior_black)/marginal_c6_ethnicity
c7_b_post = (c7_b_like*prior_black)/marginal_c7_ethnicity
c8_b_post = (c8_b_like*prior_black)/marginal_c8_ethnicity

c1_h_post = (c1_h_like*prior_hispanic)/marginal_c1_ethnicity
c2_h_post = (c2_h_like*prior_hispanic)/marginal_c2_ethnicity
c3_h_post = (c3_h_like*prior_hispanic)/marginal_c3_ethnicity
c4_h_post = (c4_h_like*prior_hispanic)/marginal_c4_ethnicity
c5_h_post = (c5_h_like*prior_hispanic)/marginal_c5_ethnicity
c6_h_post = (c6_h_like*prior_hispanic)/marginal_c6_ethnicity
c7_h_post = (c7_h_like*prior_hispanic)/marginal_c7_ethnicity
c8_h_post = (c8_h_like*prior_hispanic)/marginal_c8_ethnicity

#graph
label_ethnicity = ['WM', 'AF', 'WF', 'BF', 'LM', 'BM', 'AM', 'LF']
data_white = [c1_w_post, c2_w_post, c3_w_post, c4_w_post, c5_w_post, c6_w_post, c7_w_post, c8_w_post]
data_asian = [c1_a_post, c2_a_post, c3_a_post, c4_a_post, c5_a_post, c6_a_post, c7_a_post, c8_a_post]
data_black = [c1_b_post, c2_b_post, c3_b_post, c4_b_post, c5_b_post, c6_b_post, c7_b_post, c8_b_post]
data_hispanic = [c1_h_post, c2_h_post, c3_h_post, c4_h_post, c5_h_post, c6_h_post, c7_h_post, c8_h_post]

# plt.bar(label_ethnicity, data_white)
# plt.ylabel('P(White|image found attractive')
# plt.show()

# plt.bar(label_ethnicity, data_asian)
# plt.ylabel('P(Asian|image found attractive')
# plt.show()

# plt.bar(label_ethnicity, data_black)
# plt.ylabel('P(Black|image found attractive')
# plt.show()

# plt.bar(label_ethnicity, data_hispanic)
# plt.ylabel('P(Hispanic|image found attractive')
# plt.show()



##Sexual Orientation
#prior
prior_hetero = control_data.prior_heter
prior_homo = control_data.prior_homo
prior_bi = control_data.prior_bi

#likelihood
c1_heter_like = control_data.avg_hetero_c1
c2_heter_like = control_data.avg_hetero_c2
c3_heter_like = control_data.avg_hetero_c3
c4_heter_like = control_data.avg_hetero_c4
c5_heter_like = control_data.avg_hetero_c5
c6_heter_like = control_data.avg_hetero_c6
c7_heter_like = control_data.avg_hetero_c8
c8_heter_like = control_data.avg_hetero_c8

c1_homo_like = control_data.avg_homo_c1
c2_homo_like = control_data.avg_homo_c2
c3_homo_like = control_data.avg_homo_c3
c4_homo_like = control_data.avg_homo_c4
c5_homo_like = control_data.avg_homo_c5
c6_homo_like = control_data.avg_homo_c6
c7_homo_like = control_data.avg_homo_c8
c8_homo_like = control_data.avg_homo_c8

c1_bi_like = control_data.avg_bi_c1
c2_bi_like = control_data.avg_bi_c2
c3_bi_like = control_data.avg_bi_c3
c4_bi_like = control_data.avg_bi_c4
c5_bi_like = control_data.avg_bi_c5
c6_bi_like = control_data.avg_bi_c6
c7_bi_like = control_data.avg_bi_c8
c8_bi_like = control_data.avg_bi_c8

#marginal prob for each img
marginal_c1_sexuality = c1_heter_like*prior_hetero + c1_homo_like*prior_homo + c1_bi_like*prior_bi
marginal_c2_sexuality = c2_heter_like*prior_hetero + c2_homo_like*prior_homo + c2_bi_like*prior_bi
marginal_c3_sexuality = c3_heter_like*prior_hetero + c3_homo_like*prior_homo + c3_bi_like*prior_bi
marginal_c4_sexuality = c4_heter_like*prior_hetero + c4_homo_like*prior_homo + c4_bi_like*prior_bi
marginal_c5_sexuality = c5_heter_like*prior_hetero + c5_homo_like*prior_homo + c5_bi_like*prior_bi
marginal_c6_sexuality = c6_heter_like*prior_hetero + c6_homo_like*prior_homo + c6_bi_like*prior_bi
marginal_c7_sexuality = c7_heter_like*prior_hetero + c7_homo_like*prior_homo + c7_bi_like*prior_bi
marginal_c8_sexuality = c8_heter_like*prior_hetero + c8_homo_like*prior_homo + c8_bi_like*prior_bi

#posterior prob
c1_hetero_post = (c1_heter_like*prior_hetero)/marginal_c1_sexuality
c2_hetero_post = (c2_heter_like*prior_hetero)/marginal_c2_sexuality
c3_hetero_post = (c3_heter_like*prior_hetero)/marginal_c3_sexuality
c4_hetero_post = (c4_heter_like*prior_hetero)/marginal_c4_sexuality
c5_hetero_post = (c5_heter_like*prior_hetero)/marginal_c5_sexuality
c6_hetero_post = (c6_heter_like*prior_hetero)/marginal_c6_sexuality
c7_hetero_post = (c7_heter_like*prior_hetero)/marginal_c7_sexuality
c8_hetero_post = (c8_heter_like*prior_hetero)/marginal_c8_sexuality

c1_homo_post = (c1_homo_like*prior_homo)/marginal_c1_sexuality
c2_homo_post = (c2_homo_like*prior_homo)/marginal_c2_sexuality
c3_homo_post = (c3_homo_like*prior_homo)/marginal_c3_sexuality
c4_homo_post = (c4_homo_like*prior_homo)/marginal_c4_sexuality
c5_homo_post = (c5_homo_like*prior_homo)/marginal_c5_sexuality
c6_homo_post = (c6_homo_like*prior_homo)/marginal_c6_sexuality
c7_homo_post = (c7_homo_like*prior_homo)/marginal_c7_sexuality
c8_homo_post = (c8_homo_like*prior_homo)/marginal_c8_sexuality

c1_bi_post = (c1_bi_like*prior_bi)/marginal_c1_sexuality
c2_bi_post = (c2_bi_like*prior_bi)/marginal_c2_sexuality
c3_bi_post = (c3_bi_like*prior_bi)/marginal_c3_sexuality
c4_bi_post = (c4_bi_like*prior_bi)/marginal_c4_sexuality
c5_bi_post = (c5_bi_like*prior_bi)/marginal_c5_sexuality
c6_bi_post = (c6_bi_like*prior_bi)/marginal_c6_sexuality
c7_bi_post = (c7_bi_like*prior_bi)/marginal_c7_sexuality
c8_bi_post = (c8_bi_like*prior_bi)/marginal_c8_sexuality

#graph
labels_sexuality = ['WM', 'AF', 'WF', 'BF', 'LM', 'BM', 'AM', 'LF']
data_hetero = [c1_hetero_post, c2_hetero_post, c3_hetero_post, c4_hetero_post, c5_hetero_post, c6_hetero_post, c7_hetero_post, c8_hetero_post]
data_homo = [c1_homo_post, c2_homo_post, c3_homo_post, c4_homo_post, c5_homo_post, c6_homo_post, c7_homo_post, c8_homo_post]
data_bi = [c1_bi_post, c2_bi_post, c3_bi_post, c4_bi_post, c5_bi_post, c6_bi_post, c7_bi_post, c8_bi_post]

# plt.bar(labels_sexuality, data_hetero)
# plt.ylabel('P(heterosexuality|image found attractive)')
# plt.show()

# plt.bar(labels_sexuality, data_homo)
# plt.ylabel('P(homosexuality|image found attractive')
# plt.show()

# plt.bar(labels_sexuality, data_bi)
# plt.ylabel('P(bi|image found attractive)')
# plt.show()