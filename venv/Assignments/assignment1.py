'''
 * Created by Filip Adamik on 11/02/2018
'''

import numpy as np
import matplotlib.pyplot as plotlib

# Read training and test data
trainingData = np.genfromtxt("irisred_tr.csv", delimiter=',')
testData = np.genfromtxt("irisred_tst.csv", delimiter=',')

# Plot data on Scatter plot, different colors for different classes.
i = 0
while i < trainingData.shape[0]:
    if trainingData[i, 2] == 1:
        plotlib.scatter(trainingData[i,0], trainingData[i,1], c = "r")
    else:
        plotlib.scatter(trainingData[i,0], trainingData[i,1], c = "g")
    i += 1

# Plot histogram
myHisto = plotlib.figure()
myHisto2 = myHisto.add_subplot(111)

ones = []
zeros = []
i = 0
while i < trainingData.shape[0]:
    if trainingData[i,2] == 1:
        # myHisto2.hist(trainingData[i, 0], bins=23, range=(4.9, 7.2), color="r")
        ones.append(trainingData[i, 0])
    else:
        # myHisto2.hist(trainingData[i, 0], bins=23, range=(4.9, 7.2), color="g")
        zeros.append(trainingData[i, 0])
    i += 1

myHisto2.hist(zeros, bins=23, range=(4.9, 7.2), alpha = 0.7, color="r", label="Iris Versicolor")
myHisto2.hist(ones, bins=23, range=(4.9, 7.2), alpha = 0.7, color="g", label="Iris Virginica")
myHisto2.legend(loc="upper right")

plotlib.show()


def lin_classifier(x, w, b):
    i = 0
    mList = []

    while i < x.shape[0]:
        if (x[i, 0:2]@w-b) >= 1:
            mList.append(1)
        else:
            mList.append(0)

        i += 1
    return mList


def acc(x, w, b, t):

    lengthOfData = x.shape[0]

    mList = lin_classifier(x, w, b)

    print(mList)

    i = 0
    msum = 0
    while i < lengthOfData:
        msum += abs(t[i] - mList[i])

        i += 1

    return 1 - ((1/lengthOfData)*msum)


paramVector = [0,1]
paramOffset = 0.7

print("accuracy is: " + str(acc(testData[:, 0:2], paramVector, paramOffset, testData[:,2])))

'''
The best parameters are offset b = 0.7 and normal vector of separation plane W = [0, 1].
For these parameters we achieve accuracy of 0.95 for the test data set.

Other tried parameters were as follows

+-------------------------+--------+----------+
| Separation Plane Vector | Offset | Accuracy |
+-------------------------+--------+----------+
| [0, 0]                  |    0.0 |      0.5 |
| [0, 0]                  |    0.7 |      0.5 |
| [1, 1]                  |    0.0 |      0.5 |
| [1, 1]                  |    0.7 |      0.5 |
| [1, 0]                  |    0.0 |      0.5 |
| [1, 0]                  |    0.7 |      0.5 |
| [0, 1]                  |    0.5 |    0.875 |
| [0, 1]                  |    0.6 |      0.9 |
|                         |        |          |
| [0, 1]                  |    0.7 |     0.95 |
| [0, 1]                  |    0.8 |     0.95 |
|                         |        |          |
| [0, 1]                  |    0.9 |      0.8 |
+-------------------------+--------+----------+

'''
