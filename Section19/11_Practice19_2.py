import random as r
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)
x = []
for i in range(0,101):
    x.append(i)
data1 = []
for i in range(0,101):
    data1.append(r.randrange(0,101))
data2 = []
for i in range(0,101):
    data2.append(r.randrange(0,101))

axes.bar(x,data1,color='green')
axes.plot(x,data2,color='red',marker='.')
plt.show()
