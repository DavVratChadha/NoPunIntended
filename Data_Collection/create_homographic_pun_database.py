import xml.etree.ElementTree as ET

homo_pun_loc_dict = {}
homo_pun_sense_dict = {}
punct_set = {'.', ',', ':', "'", "?", "!"}

#reading .gold pun location file
with open('subtask2-homographic-test.gold', 'r') as f:
    lines = f.readlines()
    #for each line, append the line to the list
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        homo_pun_loc_dict[line[0]] = line[1]
#close the file
f.close()

#reading .gold pun sense file
with open('subtask3-homographic-test.gold', 'r') as f:
    lines = f.readlines()
    #for each line, append the line to the list
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        homo_pun_sense_dict[line[0]] = (line[1:])
#close the file
f.close()

#parsing the XML file to get each sentence, and apllying BPA tagging to each word
pun_sentence_list = []
neg_samples = []
pun_list = []

tree = ET.parse('subtask1-homographic-test.xml')

#getting the root element
root = tree.getroot()

#looping through each text element
for text in root.findall('./text'):
    neg = 0 #flag to indicate if the sentence is a negative sample
    # get the text id
    text_id = text.get('id')
    if text_id not in homo_pun_loc_dict: #sentence does not contain a pun
        #add the sentence to the list of negative samples
        neg = 1
    else:
        pun_loc = homo_pun_loc_dict[text_id]
        #use .get to get the pun sense, if it exists, else use the default value
        pun_sense = homo_pun_sense_dict.get(pun_loc, ['NA'])

    sentence = ""
    bpa_tagging = []
    pun_found = 0
    #looping through each word element
    for word in text.findall('./word'):
        # get the word id and content
        word_id = word.get('id')
        word_content = word.text
        if word_content in punct_set:
            sentence += word_content
        else:
            sentence += ' ' + word_content
        if not neg:
            if word_id == pun_loc:
                pun_list.append(word_content)
    if not neg:
        pun_sentence_list.append(sentence)
    else:
        neg_samples.append(sentence)

#write the pun tagged list to a txt file
with open('homo_pun_sentence_list.txt', 'w') as f:
    f.truncate(0)
    for item in pun_sentence_list:
        #each tuple is written as a string to the file in a new line
        f.write(str(item) + "\n")

#close the file
f.close()


#write the pun to a txt file
with open('homo_pun_list.txt', 'w') as f:
    f.truncate(0)
    for item in pun_list:
        #each tuple is written as a string to the file in a new line
        f.write(str(item) + "\n")

#close the file
f.close()


#write the negative samples to a txt file
with open('homo_neg_samples.txt', 'w') as f:
    f.truncate(0)
    for item in neg_samples:
        f.write(str(item) + "\n")
#close the file
f.close()
