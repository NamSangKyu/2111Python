import matplotlib.pyplot as plt
figure = plt.figure()
axes1 = figure.add_subplot(121)
x = [1,2,3,4,5]
y = [3,6,1,3,2]
axes1.plot(x,y)

axes2 = figure.add_subplot(122)
y = [1,5,2,7,8]
axes2.plot(x,y)

plt.show()
