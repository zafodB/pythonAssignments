# print('hello world')


import matplotlib.pyplot as plt
import numpy as np
# x = np.linspace(-5,5,101)
# mu=0;
# sig=1;
# # y = 1/math.sqrt(2* math.pi) * sig
# y = np.exp(-(x-mu)**2/(2*sig**2))
# plt.plot(x,y)
# plt.show()

xx= np.random.normal(0,1,100)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.hist(xx)
plt.title("Histogram")
plt.xlabel("Feature")
plt.ylabel("Frequency Count")
plt.show()

# condition = "test Var"
#
# condition2 = 123

# print("lol" + " wut" + ' noope',"braiiins")
# while condition2 > 10:
#     print (condition + ' ' + str(condition2))
#     condition2 /= 2
#
# lolList = [44, 22, 4, 6, 23, 21, 75, 54,2, 53, 5]
#
# for e in lolList:
#     print("Dat number be: " + str(e))
#
# while 0:
#     print ("BRAAAAIIIINNSSSSS")
#     print(       condition2    )
#
#     condition2 += 100
#     if condition2 > 12000:
#         break
#
