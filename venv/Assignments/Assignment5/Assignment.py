'''
 * Created by filip on 10/03/2018

 * For better readability see on Github:
 https://github.com/zafodB/pythonAssignments/blob/master/venv/Assignments/Assignment5/Assignment.py
'''

import math
import random
import numpy


class Perceptron:
    learning_rate = 0
    iterations = 0
    weights = None

    def __init__(self, mu, tmax):
        # self.bias_number = M      # NEVER USED!!!
        self.learning_rate = mu
        self.iterations = tmax

        print("Initialised class with Learning rate = %f and Iterations = %d" % (mu, tmax))

    def train(self, XX, t):
        print("Training...")

        rows = len(XX)
        columns = len(XX[0])

        start_matrix = [[1 for i in range(columns + 1)] for j in range(rows)]

        # Add 1's to beginning
        m = 0
        while m < rows:
            n = 1
            while n < columns + 1:
                start_matrix[m][n] = XX[m][n - 1]

                n += 1
            m += 1

        # Initialise random weights
        weights_w = [(random.uniform(0.0001, 0.5)) for w in range(columns + 1)]

        order = list(range(rows))
        random.shuffle(order)

        k = 0
        while k < self.iterations:

            for i in order:
                x = start_matrix[i]
                sigma = self.sigmoid(numpy.matmul(weights_w, numpy.transpose(x)))
                delta = t[i] - sigma

                weights_w = weights_w + numpy.multiply(self.learning_rate * delta * sigma * (1 - sigma), x)

            k += 1

        self.weights = weights_w

    def sigmoid(self, z):
        try:
            length = len(z)
            i = 0
            output = [0 for l in range(length)]

            while i < length:
                output[i] = (1 / (1 + math.e ** -z[i]))
                i += 1

            return output

        except TypeError:
            return 1 / (1 + math.e ** -z)

    def predict(self, XX, w):
        print("Predicting...")

        rows = len(XX)
        columns = len(XX[0])

        x = [[1 for i in range(columns + 1)] for j in range(rows)]

        m = 0
        while m < rows:
            n = 1
            while n < columns + 1:
                x[m][n] = XX[m][n - 1]

                n += 1
            m += 1

        return self.sigmoid(numpy.matmul(x, w))

    def classify(self, XX, w):
        print("Classifying...")

        rows = len(XX)
        columns = len(XX[0])

        x = [[1 for i in range(columns + 1)] for j in range(rows)]

        m = 0
        while m < rows:
            n = 1
            while n < columns + 1:
                x[m][n] = XX[m][n - 1]

                n += 1
            m += 1

        output = []

        for z in self.sigmoid(numpy.matmul(x, w)):
            output.append((numpy.sign(z - 0.5) + 1) / 2)

        return output

    def mse(self, t, y):
        length = len(t)
        if not length == len(y):
            print("Lengths of data don't match.")
            return False

        square_error = 0

        i = 0
        while i < length:
            square_error += ((t[i] - y[i]) ** 2)
            i += 1

        return square_error / length


instance1 = Perceptron(100, 1000)

and_matrix = [[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]]
and_results = [0, 0, 0, 1]
instance1.train(and_matrix, and_results)

# predictions = instance1.predict(and_matrix, instance1.weights)
predictions = instance1.classify(and_matrix, instance1.weights)

print(predictions)
print("Mean square error is: " + str(instance1.mse(predictions, and_results)))
print()

'''
Combination of tried learning rates and Max Iterations.

+---------------+----------------+-------------------+
| Learning Rate | Max Iterations | Mean Square Error |
+---------------+----------------+-------------------+
|             1 |             10 |              0.25 |
|             1 |            100 |               0.0 |
|             1 |           1000 |               0.0 |
|            10 |              1 |              0.25 |
|            10 |             10 |               0.0 |
|            10 |            100 |               0.0 |
|            10 |           1000 |               0.0 |
|           100 |             10 |              0.25 |
|           100 |            100 |              0.25 |
|           100 |           1000 |              0.25 |
+---------------+----------------+-------------------+

Console output for Learning rate = 100 and max iterations = 1000:

    Initialised class with Learning rate = 100 and Iterations = 1000
    Training...
    Classifying...
    [0.0, 0.0, 0.0, 0.0]
    Mean square error is: 0.25
    
In assignment it said we should use method 'predict' for classification of the data, but on Slack in an answer written 
by teacher it said we need to use method 'classify'. In here, I decided to use method 'Classify', which yielded 
mean square error to be either 0.0 or 0.25. If we used method 'predict', we would see greater variation of mean
square error.
'''

instance2 = Perceptron(0.5, 1000)
trainingDataIrisFeatures = numpy.genfromtxt("irisred_tr_features.csv", delimiter=',')
trainingDataIrisTargets = numpy.genfromtxt("irisred_tr_targets.csv", delimiter=',')
testDataIrisFeatures = numpy.genfromtxt("irisred_tst_features.csv", delimiter=',')
testDataIrisTargets = numpy.genfromtxt("irisred_tst_targets.csv", delimiter=',')

instance2.train(trainingDataIrisFeatures, trainingDataIrisTargets)

predictions2 = instance2.predict(testDataIrisFeatures, instance2.weights)
# predictions2 = instance2.classify(testDataIrisFeatures, instance2.weights)

print(predictions2)

print("Mean square error is: " + str(instance2.mse(predictions2, testDataIrisTargets)))

'''
Combination of tried Learning rates and max iterations. Best combinations indicated by (#) sign.

+---+---------------+----------------+--------------------+---+
|   | Learning Rate | Max Iterations | Mean square error* |   |
+---+---------------+----------------+--------------------+---+
|   |           0.1 |            100 |            0.08128 |   |
| # |           0.1 |           1000 |            0.05448 | # |
|   |           0.5 |            100 |            0.10843 |   |
| # |           0.5 |           1000 |            0.05887 | # |
|   |             1 |             10 |            0.45336 |   |
|   |             1 |            100 |            0.09566 |   |
|   |            10 |             10 |                0.5 |   |
|   |            10 |            100 |            0.49999 |   |
|   |            10 |           1000 |                0.5 |   |
+---+---------------+----------------+--------------------+---+


* values of mean square error only have 3 significant digits. The rest is influenced by the random initialisation of 
weights (see line #41)

For this exercise, we used method 'Predict' instead of classify. This resulted in bigger variation of mean square 
errors. The console output for Learning rate = 0.5 and max iterations = 1000:

    Initialised class with Learning rate = 0.500000 and Iterations = 1000
    Training...
    Predicting...
    [0.00012533531884559038, 2.2963975434349768e-05, 0.0005201427605457476, 0.27794955673996913, 0.10866039908881707, 
    0.27794955673996913, 0.03590302573947519, 0.001797026475157538, 0.0033976199134746043, 0.003720922583508456, 
    0.0006837568840026059, 0.011655962036702454, 0.0005201427605457476, 3.6234732965223386e-05, 0.0033976199134746043, 
    0.000569793819715706, 0.0031023208189339176, 0.0019683244736913054, 0.00018051633427445095, 0.0031023208189339176, 
    0.9458208280408328, 0.9837106498480438, 0.9998585568336825, 0.0509079568213671, 0.011655962036702454, 
    0.9999151692194553, 0.9999956660584434, 0.8884294018104969, 0.9198035887088403, 0.9987830599498689, 
    0.9999937576340384, 0.9999591079824521, 0.9868655031220751, 0.9999626729785944, 0.9999988563830569, 
    0.9999659271863433, 0.9794310048128838, 0.995403776324168, 0.9999784061707594, 0.9262799930492598]
    
    Mean square error is: 0.051838531506984496
'''
