import matplotlib.pyplot as plt

figure = plt.figure()

axes = figure.add_subplot(111)

x = [1,2,3,4,5,6]
y = [6,4,1,2,7,5]

area = [50,100,150,200,250,300]
color = ['red','green','blue','orange','aqua','crimson']
axes.scatter(x,y,s=area,c=color)

plt.show()