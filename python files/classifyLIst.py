import sklearn.metrics
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

from sklearn.metrics import RocCurveDisplay
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import csv
import pandas as pd

def confusionMatrix(classifier, xTest, yTest):
    plot_confusion_matrix(classifier, xTest, yTest)
    #plt.axis("off")
    plt.show()

def main():


    #column headers
    header = ['add()', 'remove()', 'getFirst()', 'update()', 'getNext()', 'getIndex()', 'setIndex()', 'getLength()']

    #read in csv files
    dataframe1 = pd.read_csv('C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\list.csv', header=None, names=header, delimiter=",", engine="python")
    dataframe2 = pd.read_csv('C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\list_class_stats_list-10-90--90-10-c10_500_1000_1000.txt',
                             header=None, delimiter=",", engine="python")

    #set data, the [3] signifies the env column
    X = dataframe1
    y = dataframe2[3]

    #split data into training and test data
    xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.9, random_state=None)

    print(xTrain)

    #decision tree
    classifier = DecisionTreeClassifier()
    classifier = classifier.fit(xTrain, yTrain)

    yPredDecisionTree = classifier.predict(xTest)

    confusionMatrix(classifier, xTest, yTest)
    #create predicitons values

    #evaluate predictions to get accuracy
    print("Decision tree accuracy :", metrics.accuracy_score(yTest, yPredDecisionTree))
    print("Decision tree recall score :", metrics.recall_score(yTest, yPredDecisionTree))
    print("Decision tree precision score", metrics.precision_score(yTest, yPredDecisionTree))
    print("K nearest neighbour accuracy :", metrics.f1_score(yTest, yPredDecisionTree))


    #k nearest neighbour
    classifier = KNeighborsClassifier()
    classifier = classifier.fit(xTrain, yTrain)

    yPredKnn = classifier.predict(xTest)

    confusionMatrix(classifier, xTest, yTest)

    print("K nearest neighbour accuracy :", metrics.accuracy_score(yTest, yPredKnn))
    print("K nearest neighbour accuracy :", metrics.recall_score(yTest, yPredKnn))
    print("K nearest neighbour accuracy :", metrics.precision_score(yTest, yPredKnn))
    print("K nearest neighbour accuracy :", metrics.f1_score(yTest, yPredKnn))
    #naive bayerns
    classifier = MultinomialNB()
    classifier = classifier.fit(xTrain, yTrain)

    yPredNaive = classifier.predict(xTest)

    confusionMatrix(classifier, xTest, yTest)
    print("Naive bayerns accuracy accuracy :", metrics.accuracy_score(yTest, yPredNaive))
    print("Naive bayerns accuracy accuracy :", metrics.recall_score(yTest, yPredNaive))
    print("Naive bayerns accuracy accuracy :", metrics.precision_score(yTest, yPredNaive))
    print("Naive bayerns accuracy accuracy :", metrics.f1_score(yTest, yPredNaive))


    fprNB, tprNB, _ = roc_curve(yTest, yPredNaive)
    aucNaives= auc(fprNB, tprNB)
    fprKNN, tprKNN, _ = roc_curve(yTest, yPredKnn)
    aucknn = auc(fprKNN, tprKNN)
    fprDT, tprDT, _ = roc_curve(yTest, yPredDecisionTree)
    aucdt= auc(fprDT, tprDT)

    plt.figure(1)
    plt.plot([0, 1], [0, 1], 'k--', label="random")
    plt.plot(fprDT, tprDT, label='Decision Tree ROC (AUC = {:.3f})'.format(aucdt))
    plt.plot(fprKNN, tprKNN, label='K-nearest Neighbour ROC (AUC = {:.3f})'.format(aucknn))
    plt.plot(fprNB, tprNB, label='Naives  Bayes ROC (AUC = {:.3f})'.format(aucNaives))
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
