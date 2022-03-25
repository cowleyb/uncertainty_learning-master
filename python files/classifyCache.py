import keras.optimizers
import tensorflow as tf
from numpy import loadtxt
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import pandas as pd

from sklearn.model_selection import train_test_split # Import train_test_split function
from keras.preprocessing import sequence
import numpy as np
import matplotlib.pyplot as plt
from keras.utils.vis_utils import plot_model
from keras_visualizer import visualizer
from keras.layers.embeddings import Embedding
from keras import initializers

from sklearn.utils import class_weight

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report

from sklearn.metrics import roc_curve
from sklearn.metrics import auc

import fileinput
import string
import re
def confusionMatrix(yTest, yPred):
    cm = confusion_matrix(yTest, yPred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    #.axis("off")
    plt.show()

def main():

    #count the number of columns
    with open("C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cache.csv" ) as f:
        columnCount = [len(l.split(",")) for l in f.readlines()]

    maxColumns = max(columnCount)
    #get largest column count and create column header counting up to that value
    columnNames = [i for i in range(0, maxColumns)]

    print(maxColumns)
    maxColumns = max(columnCount)

    #read dataframes
    dataframe1 = pd.read_csv("C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cache.csv", header=None, delimiter=",", engine='python', names=columnNames).fillna(value=0)
    print ("yo")
    dataframe2 = pd.read_csv("C:\\Users\\minim\\Downloads\\uncertainty_learning-master\\output_data\\cache_class_stats_cache-10--200-500000-400000_500_1000_1000.txt",engine='python', delimiter=",", header=None)

    #get x y
    X = dataframe1.values
    y = dataframe2[3].values

    padValue = 20000

    X = sequence.pad_sequences(X, maxlen=padValue)


    #split into test train
    xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.3, random_state=None)

    classWeights = dict(enumerate(class_weight.compute_class_weight(class_weight='balanced',classes=np.unique(yTrain), y=yTrain)))

    model = Sequential()
    print(xTrain.shape, yTrain.shape)


    #initializer = tf.keras.initializers.RandomNormal(mean=50, stddev=1.)

    #layers
    model.add(Dense(1000, input_dim=padValue, activation='relu'))
    model.add(Dropout(0.6))
    #model.add(Dense(100, activation='relu'))
    #model.add(Dropout(0.2))
    #model.add(Dense(2, activation='relu'))
    #model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))

    #moments
    optimezer = tf.keras.optimizers.Adam(0.001)

    model.compile(loss='binary_crossentropy', optimizer=optimezer, metrics=['accuracy'])

    #run
    model.fit(xTrain, yTrain, epochs=50, batch_size=1000, verbose=1, class_weight=classWeights)
    _, accuracy = model.evaluate(xTrain, yTrain)
    print('Accuracy: %.2f' % (accuracy * 100))

    #plot network
    'plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
    'model.summary()
    'visualizer(model, format='png', view=True)

    yPred = (model.predict(xTest) > 0.5).astype(int)

    #confusionMatrix(yTest, yPred)

    #accuracy
    count = 0
    for i in range(len(yTest)):
        print('%d (expected %d)' % (yPred[i], yTest[i]))
        if (yPred[i] == yTest[i]):
            count += 1
    print(count / len(yTest)*100)

    print(classification_report(yTest, yPred))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



    """
    h = model.fit(xTrain, yTrain, epochs=50, batch_size=1000, verbose=1, class_weight=classWeights,validation_split=0.33)

    plt.plot(h.history['accuracy'])
    plt.plot(h.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='lower right')
    plt.show()
    # summarize history for loss
    plt.plot(h.history['loss'])
    plt.plot(h.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='lower right')
    plt.show()
    
    
    
    
    fpr, tpr, _ = roc_curve(yTest, yPred)
    auc_keras = auc(fpr, tpr)

    plt.figure(1)
    plt.plot([0, 1], [0, 1], 'k--', label="random")
    plt.plot(fpr, tpr, label='ROC (AUC = {:.3f})'.format(auc_keras))
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc='best')
    plt.show()
    # Zoom in view of the upper left corner.

    """
