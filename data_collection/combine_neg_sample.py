#open the two neg sample files and combine them into one file
with open('het_neg_samples.txt', 'r') as f:
    het_neg_samples = f.read()
#close file
f.close()

with open('homo_neg_samples.txt', 'r') as f:
    homo_neg_samples = f.read()
#close file
f.close()

#combine the two lists
neg_samples = het_neg_samples + homo_neg_samples

#save the combined list to neg_samples.txt
with open('neg_samples.txt', 'w') as f:
    f.truncate(0)
    f.write(neg_samples)
#close file
f.close()
