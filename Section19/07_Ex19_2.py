import matplotlib.pyplot as plt

figure = plt.figure()

axes = figure.add_subplot(111)

x = [20,25,30,35,40,45,50,55,60,65,70]
y = [10,11,15,20,30,42,55,70,88,110,150]
axes.scatter(x,y,s=y)
plt.xlabel('noise')
plt.ylabel('stress')

plt.show()