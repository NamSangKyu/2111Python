import matplotlib.pyplot as plt
figure = plt.figure()

axes = figure.add_subplot(111)
x = [1,2,3,4,5]
y = [1,6,3,6,2]
axes.plot(x,y,linestyle='dotted',linewidth=4)

y = [1,3,5,7,9]
axes.plot(x,y,linestyle='solid',linewidth=1, color='r',marker='v')

y=[1,3,2,1,7]
axes.plot(x,y,linestyle='dashed',linewidth=4)

plt.show()