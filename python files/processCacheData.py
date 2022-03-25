
import pandas as pd


import fileinput
import re

def main():
    #loop through all files produced
    maxCount = 0
    for i in range(1, 31):

        #remove file path for readability
        for line in fileinput.input(
                "C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cacheTrainingData\\cache%s.txt" % i, inplace=True):
            print(re.sub("tmp\/file|.txt", "", line))

        #count the number of columns
        with open("C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cacheTrainingData\\cache%s.txt" % i) as f:
            columnCount = [len(l.split(",")) for l in f.readlines()]

        #get largest column count and create column header counting up to that value
        columnNames = [i for i in range(0, max(columnCount))]

        maxCount = max(columnCount)
        print(maxCount)

        #create data frame
        dataframe1 = pd.read_csv(
            "C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cacheTrainingData\\cache%s.txt" % i, header=None,
            names=columnNames, delimiter=",", engine='python').fillna(value=0)
        #remove unwanted column
        dataframe1 = dataframe1.iloc[:-1, :]

        #append to csv file
        dataframe1.to_csv("C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cache.csv", mode='a',
                          index=None, header=False)




if __name__ == '__main__':
    main()