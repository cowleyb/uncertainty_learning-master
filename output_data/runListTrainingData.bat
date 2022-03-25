cd..
for /l %%x in (1, 1, 10) do dana ListClassTest.o data/adt/Array.o  workloads/list-10-90--90-10-c10sq.txt > C:\Users\minim\Downloads\uncertainty_learning-master\output_data\listTrainingData\list%%x.txt
for /l %%x in (11, 1, 20) do dana ListClassTest.o data/adt/Linked.o  workloads/list-10-90--90-10-c10sq.txt > C:\Users\minim\Downloads\uncertainty_learning-master\output_data\listTrainingData\list%%x.txt

