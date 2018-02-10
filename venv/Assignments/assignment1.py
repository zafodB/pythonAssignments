import numpy
import matplotlib.pyplot as plotlib


fname = "irisred_tr.csv"

file = open(fname, 'r')

trainingData = numpy.genfromtxt(file, delimiter=',')

# print("Training data:")
# print(trainingData)

testData = numpy.genfromtxt("irisred_tst.csv", delimiter=',')

# print ()
# print("Test data:")
# print(testData)



i = 0

while i < trainingData.shape[0]:
    if trainingData[i,2] == 1 :
        plotlib.scatter(trainingData[i,0], trainingData[i,1], c = "r")
    else:
        plotlib.scatter(trainingData[i,0], trainingData[i,1], c = "g"
                        )
    i += 1

# plotlib.legend()
# plotlib.show()


myRange = numpy.arange(4.9, 7.2, 0.1)

myHisto = plotlib.figure()

myHisto2 = myHisto.add_subplot(111)

myHisto2.hist(trainingData[:, 0], bins=23, range=(4.9, 7.2))
# plotlib.show()

def lin_classifier(X, w, b):
    i = 0;
    mList = []

    while i < X.shape[0]:
        if (X[i,0:2]@w-b)>=1:
            mList.append(1)
        else:
            mList.append(0)

        i += 1
    return mList


# print(lin_classifier(trainingData[:,0:2], [0,1], 0.6 ))

def acc(X, w, b, t):

    lengthOfData = X.shape[0]

    mList = lin_classifier(X, w, b)

    print(mList)

    i = 0
    sum = 0
    while i < lengthOfData:
        sum += (t[i] - mList[i])

        i += 1

    return 1 - ((1/lengthOfData)*sum)


print("accuracy shall be: " + str(acc(testData[:, 0:2], [0,1], 0.7, testData[:,2])))
# print("accuracy shall be: " + str(acc(trainingData[:, 0:2], [0,1], 0.7, trainingData[:,2])))
