


import csv


def main():

    #create column header names
    header = ['add()', 'remove()', 'getFirst()', 'update()', 'getNext()','getIndex()','setIndex()', 'getLength()']

    #initialise counter variables
    add = remove = getFirst = update = getNext = getIndex = setIndex = getLength = 0


    for i in range(1, 21):
        file = open('C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\listTrainingData\\list%s.txt' % i, 'r')
        lines = file.readlines()
        with open('C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\list.csv', 'a', encoding='UTF8',
                  newline='') as f:
            writer = csv.writer(f)
            for line in lines:
                if line == "add()\n":
                    add +=1
                elif line == "remove()\n":
                    remove += 1
                elif line == "getFirst()\n":
                    getFirst += 1
                elif line == "update()\n":
                    update += 1
                elif line == "getNext()\n":
                    getNext += 1
                elif line == "getIndex()\n":
                    getIndex += 1
                elif line == "setIndex()\n":
                    setIndex += 1
                elif line == "getLength()\n":
                    getLength += 1
                elif line == "next\n":
                    data = [add, remove, getFirst, update, getNext, getIndex, setIndex, getLength]
                    writer.writerow(data)
                    add = remove = getFirst = update = getNext = getIndex = setIndex = getLength = 0





if __name__ == '__main__':
    main()