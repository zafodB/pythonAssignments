'''
 * Created by filip on 10/03/2018
'''

import math
import random
import numpy


class Perceptron:

    bias_number = 0
    learnning_rate = 0
    iterations = 0

    def __init__(self, M, mu, tmax):
        self.bias_number = M
        self.learnning_rate = mu
        self.iterations = tmax

        print("Initialised class")

    def train(self, XX, t):
        print("wut")

        rows = len(XX)
        columns = len(XX[0])

        start_matrix = [[1 for i in range(columns + 1)] for j in range(rows)]

        m = 0
        while m < rows:
            n = 1
            while n < columns + 1:
                start_matrix[m][n] = XX[m][n - 1]

                n += 1
            m += 1

        weights_w = [(random.uniform(0.0001, 0.5))for w in range(columns+1)]

        print(weights_w)
        k = 0
        while k < self.iterations:
            random.shuffle(start_matrix)

            i = 0
            while i < len(start_matrix):
                x = start_matrix[i]
                xt = numpy.transpose(x)

                sigma = self.sigmoid(weights_w * xt)

                delta = [0 for nn in range(len(sigma))]
                n = 0
                while n < len(sigma):
                    delta[n] = t[i] - sigma[n]
                    n += 1

                mm = 0
                while mm < len(weights_w):
                    weights_w[mm] = weights_w[mm] + (1 * delta[mm] * sigma[mm] * (1 - sigma[mm]) * x[mm])
                    mm += 1

                i += 1
            k += 1

        print(weights_w)
        # print(start_matrix)

    def sigmoid(self, z):
        # print("ziiigmmaaa")
        length = len(z)
        i = 0
        output = [0 for l in range(length)]

        while i < length:
            output[i] = (1 / (1 + math.e ** -z[i]))
            i += 1

        return output

    def predict(self, XX, w):
        print("wut")

    def mse(self, t, y):
        print("Calculating mean square error.")

        length = len(t)
        if not length == len(y):
            return False

        square_error = 0

        i = 0
        while i < length:
            square_error += ((t[i] - y[i]) ** 2)
            i += 1

        return square_error / length

    def classify(self, XX, w):
        print("wut")


instance = Perceptron(0, 1, 10)

# print(instance.sigmoid([0, 0.1, 1, 10, 100]))

matrxx = [
    [1, 3, 54, 76, 3],
    [54, 65, 7, 76, 2],
    [87, 0, -1, 76, 6]
]

matrxx2 = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

training2 = [0, 0, 0, 1]
instance.train(matrxx2, training2)

# t = [2.001432074, 3.593956593, 8.439908051, 3.409160294, 6.82743551, 9.041002094, 7.341822748, 5.911280432, 1.509472891, 3.655158303, 7.663951458, 0.652352025, 7.967413895, 3.275054869, 2.157349194, 2.315865342, 1.906791492, 6.030138405, 8.384114734, 2.591674876, 2.67821344, 4.988229593, 8.185783656, 2.681385354, 6.770900328, 1.252404912, 8.499207465, 1.167087192]
# y =[ 1.001432074, 2.593956593, 7.439908051, 4.409160294, 8.82743551, 8.041002094, 6.341822748, 4.911280432, 0.509472891, 2.655158303, 6.663951458, -0.347647975, 6.967413895, 2.275054869, 1.157349194, 1.315865342, 0.906791492, 5.030138405, 7.384114734, 1.591674876, 1.67821344, 3.988229593, 7.185783656, 1.681385354, 5.770900328, 0.252404912, 7.499207465, 0.167087192]

# print(instance.mse(t, y))

