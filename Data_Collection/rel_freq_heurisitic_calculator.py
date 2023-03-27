import pickle
import numpy as np
import matplotlib.pyplot as plt


def open_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
het_pun_processed = open_pickle('processed/het_list_processed.pickle')
homo_pun_processed = open_pickle('processed/homo_list_processed.pickle')

mega_list = het_pun_processed + homo_pun_processed

all_pos_tags = {}
pun_array = []
for sublist in mega_list:
    pun_array.append(sublist[2][0].split('/')[1])
    for word in sublist[0]:
        tag = word.split('/')[1]
        # if tag in punct_tag:
            # continue
        if tag in all_pos_tags:
            all_pos_tags[tag] += 1
        else:
            all_pos_tags[tag] = 1

pun_array = np.array(pun_array)


unique, counts = np.unique(pun_array, return_counts=True)
smooth_unique = []
smooth_counts = []

for tag in all_pos_tags:
    if tag in unique:
        smooth_unique.append(tag)
        #get index of tag in unique
        index = np.where(unique == tag)[0][0]
        smooth_counts.append(counts[index] + 1)
    else:
        smooth_unique.append(tag)
        smooth_counts.append(1)

smooth_freq = np.array(smooth_counts)/(np.sum(counts) + len(smooth_unique))

tick_locs = np.arange(0, len(smooth_unique), 2)

#sort smooth_unique and smooth_freq by smooth_unique in alphabetical order
smooth_unique, smooth_freq = zip(*sorted(zip(smooth_unique, smooth_freq)))

#plotting a histogram of the puns
plt.bar(smooth_unique, smooth_freq, width = 0.7)
plt.xticks(tick_locs, smooth_unique[::2], rotation=90)
plt.title("Relative Frequency of POS tags in puns")
plt.xlabel("POS tags")
plt.ylabel("Relative Frequency")
plt.show()

#create a dictionary of the unique tags and their relative frequencies
tag_dict = dict(zip(smooth_unique, smooth_freq))

#save tag_dict to a pickle file
with open('processed/tag_dict.pickle', 'wb') as f:
    f.truncate(0)
    pickle.dump(tag_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()