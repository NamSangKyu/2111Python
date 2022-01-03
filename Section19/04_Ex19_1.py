import matplotlib.pyplot as plt
figure = plt.figure()
axes = figure.add_subplot(111)
x = ['Jan','Feb','Mar','Apr','May','Jun']
y = [1200,800,500,400,700,800]

axes.plot(x,y,linestyle=':',marker='o')
plt.show()