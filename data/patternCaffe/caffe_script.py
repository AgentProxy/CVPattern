#!/usr/bin/python
import os
import csv

def csvReader(pathname):
    ifile = open(pathname, "rt")
    reader = csv.reader(ifile)

    return ifile,reader

def findImages():
    ifile, reader = csvReader("decor.csv")
    rownum = 0
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
        currPath = "decor/"+filename
        destPath = "decor/"+type_pp+"/"+filename
        print currPath, destPath
        os.rename(currPath, destPath)


if __name__ == '__main__':
    findImages()