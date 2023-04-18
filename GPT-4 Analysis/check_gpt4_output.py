import re

def open_file(file_name):
    with open(file_name, "r") as f:
        return f.read()
    
homo_list = open_file("homo_done.txt").splitlines()
homo_pun_words = open_file("homo_pun_list.txt").splitlines()

count = 0
check_list = []

assert len(homo_list) == len(homo_pun_words), "Two files are of unequal lengths"
for index in range(len(homo_pun_words)):
    pun_word = homo_pun_words[index]
    sentence = homo_list[index]

    #using regex, delete everything except terms inside quotes, there are multiple quotes in a sentence
    sentence = re.findall(r'"([^"]*)"', sentence)
    if len(sentence[0]) != len(pun_word):
        count += 1
        check_list.append(index + 1)
print("Total sentence with incorrectly identified puns by GPT4: ", count)
print("You need to check GPT4 explanations at lines: ", check_list)
