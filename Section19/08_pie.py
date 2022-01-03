import matplotlib.pyplot as plt

figure = plt.figure()

axes = figure.add_subplot(111)

data = [1,2,3]
label = ['Good','Bad','Normal']
axes.pie(data,labels=label,autopct='%.2f%%', explode=[0.1, 0, 0])
#0.0 ~ 1.0  좌표값 (x좌표, y좌표)
axes.legend(label,loc=(0.5,0.0))
plt.show()