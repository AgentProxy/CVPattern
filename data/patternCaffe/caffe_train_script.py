#!/usr/bin/python
import os
import csv
import sys
import shutil

def csvReader(pathname):
    ifile = open(pathname, "rt")
    reader = csv.reader(ifile)

    return ifile,reader

def findImages(option):
    print(option)
    ifile, reader = csvReader(option + ".csv")
    rownum = 0
    files = []
    for row in reader:
        if rownum == 0:
            rownum += 1
            continue
        country_label = row[0]
        country = row[1]
        decor_label = row[2]
        decor = row[3]
        type_label = row[4]
        type_pp = row[5]
        filename = row[6]

        if(type_pp==option):
            currPath = "../../examples/patternCaffe/decor/"+option+"/"+filename
            # destPath = "../../examples/patternCaffe/decor/"+option+"/train/"+filename
            # print currPath, destPath
            # shutil.copy(currPath,destPath)

    for file_name in os.listdir("../../examples/patternCaffe/decor/"+option+"/"):
        files.append(file_name)
    for i in files:
        print i


            

if __name__ == '__main__':
    findImages(sys.argv[1])