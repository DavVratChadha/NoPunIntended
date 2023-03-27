import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy
import os
import glob

images_folder = 'RedditImageScraper/images/*'

images_names = glob.glob(images_folder)
print(images_names)

pun_txt = open("full_puns.txt", "w")

images = []
for imname in images_names:
    print(imname)
    im = cv2.imread(imname)

    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(im)

    list_str = []

    for i in range(len(result)):
        list_str.append(result[i][1].lower())
        

    str_pun = " ".join(list_str)

    pun_txt.write(str_pun)
    pun_txt.write("\n")






#print(result)


#text file, newline is new pun